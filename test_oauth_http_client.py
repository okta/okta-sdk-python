"""
Comprehensive unit tests for OAuth and HTTP client fixes

Tests cover:
1. OAuth token request formatting (no duplicate parameters)
2. Form data encoding for application/x-www-form-urlencoded
3. Header isolation between requests (no mutation)
4. File upload functionality still works
5. Multiple sequential requests maintain isolated state
"""

import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, patch, mock_open
import pytest
import aiohttp

from okta.http_client import HTTPClient
from okta.oauth import OAuth
from okta.request_executor import RequestExecutor


class TestOAuthTokenRequest:
    """Test OAuth token request formatting"""

    @pytest.mark.asyncio
    async def test_oauth_parameters_in_body_not_url(self):
        """Verify all OAuth parameters are sent in request body, not URL query string"""

        config = {
            "client": {
                "orgUrl": "https://test.okta.com",
                "clientId": "test_client_id",
                "scopes": ["okta.users.read", "okta.groups.read"],
                "privateKey": "test_private_key",
                "kid": "test_kid",
                "oauthTokenRenewalOffset": 5
            }
        }

        mock_executor = MagicMock()
        mock_executor._config = config
        # create_request should return (request_dict, None)
        mock_executor.create_request = AsyncMock(return_value=({}, None))
        mock_executor.fire_request = AsyncMock(return_value=(
            None,
            MagicMock(status=200, content_type="application/json"),
            '{"access_token": "test_token", "expires_in": 3600}',
            None
        ))

        oauth = OAuth(mock_executor, config)

        # Mock JWT creation
        with patch.object(oauth, 'get_JWT', return_value='test_jwt_token'):
            await oauth.get_access_token()

        # Verify create_request was called
        assert mock_executor.create_request.called
        call_args = mock_executor.create_request.call_args

        # Extract arguments
        method = call_args[0][0]
        url = call_args[0][1]
        kwargs = call_args[1]

        # Verify POST method
        assert method == "POST"

        # Verify URL has NO query parameters
        assert "?" not in url, "URL should not contain query parameters"
        assert url == "https://test.okta.com/oauth2/v1/token"

        # Verify all parameters are in form body
        assert "form" in kwargs
        form_data = kwargs["form"]

        assert form_data["grant_type"] == "client_credentials"
        assert form_data["scope"] == "okta.users.read okta.groups.read"
        assert form_data["client_assertion_type"] == "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
        assert form_data["client_assertion"] == "test_jwt_token"

        # Verify no duplicate parameters
        assert "client_assertion" not in url, "client_assertion should not be in URL"

    @pytest.mark.asyncio
    async def test_oauth_request_headers(self):
        """Verify OAuth request has correct headers"""

        config = {
            "client": {
                "orgUrl": "https://test.okta.com",
                "clientId": "test_client_id",
                "scopes": ["okta.users.read"],
                "privateKey": "test_private_key",
                "oauthTokenRenewalOffset": 5
            }
        }

        mock_executor = MagicMock()
        mock_executor._config = config
        # create_request should return (request_dict, None)
        mock_executor.create_request = AsyncMock(return_value=({}, None))
        mock_executor.fire_request = AsyncMock(return_value=(
            None,
            MagicMock(status=200, content_type="application/json"),
            '{"access_token": "test_token", "expires_in": 3600}',
            None
        ))

        oauth = OAuth(mock_executor, config)

        with patch.object(oauth, 'get_JWT', return_value='test_jwt_token'):
            await oauth.get_access_token()

        call_kwargs = mock_executor.create_request.call_args[1]

        # Verify headers
        assert "headers" in call_kwargs
        headers = call_kwargs["headers"]
        assert headers["Accept"] == "application/json"
        assert headers["Content-Type"] == "application/x-www-form-urlencoded"


class TestHTTPClientFormData:
    """Test HTTP client form data handling"""

    @pytest.mark.asyncio
    async def test_form_data_encoding_without_file(self):
        """Test that regular form data (non-file) is properly encoded"""

        http_config = {
            "headers": {
                "User-Agent": "test-client",
                "Accept": "application/json"
            }
        }
        http_client = HTTPClient(http_config)

        request = {
            "method": "POST",
            "url": "https://test.okta.com/api/endpoint",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": None,
            "form": {
                "grant_type": "client_credentials",
                "scope": "okta.users.read",
                "client_assertion": "test_jwt"
            }
        }

        # Mock aiohttp session
        mock_response = AsyncMock()
        mock_response.request_info = MagicMock()
        mock_response.status = 200
        mock_response.text = AsyncMock(return_value='{"success": true}')

        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = AsyncMock()
            mock_session.request = AsyncMock(return_value=mock_response)
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock()
            mock_session_class.return_value = mock_session

            await http_client.send_request(request)

            # Verify request was made
            assert mock_session.request.called
            call_kwargs = mock_session.request.call_args[1]

            # Verify data is set
            assert "data" in call_kwargs
            assert call_kwargs["data"] == request["form"]

            # Verify Content-Type was removed from headers (let aiohttp handle it)
            assert "Content-Type" not in call_kwargs["headers"]

    @pytest.mark.asyncio
    async def test_file_upload_still_works(self):
        """Test that file upload functionality is not broken"""

        http_config = {
            "headers": {
                "User-Agent": "test-client",
                "Content-Type": "application/json"
            }
        }
        http_client = HTTPClient(http_config)

        request = {
            "method": "POST",
            "url": "https://test.okta.com/api/upload",
            "headers": {},
            "data": None,
            "form": {
                "file": "/tmp/test_file.txt"
            }
        }

        mock_response = AsyncMock()
        mock_response.request_info = MagicMock()
        mock_response.status = 200
        mock_response.text = AsyncMock(return_value='{"success": true}')

        with patch('aiohttp.ClientSession') as mock_session_class, \
             patch('builtins.open', mock_open(read_data=b"test file content")):

            mock_session = AsyncMock()
            mock_session.request = AsyncMock(return_value=mock_response)
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock()
            mock_session_class.return_value = mock_session

            await http_client.send_request(request)

            # Verify request was made
            assert mock_session.request.called
            call_kwargs = mock_session.request.call_args[1]

            # Verify data is FormData for file uploads
            assert "data" in call_kwargs
            assert isinstance(call_kwargs["data"], aiohttp.FormData)


class TestHeaderIsolation:
    """Test that headers are properly isolated between requests"""

    @pytest.mark.asyncio
    async def test_headers_not_mutated_after_form_request(self):
        """Verify that _default_headers is not mutated after a form data request"""

        http_config = {
            "headers": {
                "User-Agent": "okta-sdk-python",
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        }
        http_client = HTTPClient(http_config)

        # Capture initial headers
        initial_headers = dict(http_client._default_headers)

        request = {
            "method": "POST",
            "url": "https://test.okta.com/oauth2/v1/token",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": None,
            "form": {
                "grant_type": "client_credentials",
                "client_assertion": "test_jwt"
            }
        }

        mock_response = AsyncMock()
        mock_response.request_info = MagicMock()
        mock_response.status = 200
        mock_response.text = AsyncMock(return_value='{"access_token": "token"}')

        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = AsyncMock()
            mock_session.request = AsyncMock(return_value=mock_response)
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock()
            mock_session_class.return_value = mock_session

            await http_client.send_request(request)

        # Verify headers are unchanged
        assert http_client._default_headers == initial_headers
        assert "Content-Type" in http_client._default_headers
        assert http_client._default_headers["Content-Type"] == "application/json"

    @pytest.mark.asyncio
    async def test_multiple_requests_maintain_isolated_headers(self):
        """Test that multiple sequential requests maintain header isolation"""

        http_config = {
            "headers": {
                "User-Agent": "okta-sdk-python",
                "Accept": "application/json"
            }
        }
        http_client = HTTPClient(http_config)

        initial_headers = dict(http_client._default_headers)

        # Request 1: OAuth request with form data
        request1 = {
            "method": "POST",
            "url": "https://test.okta.com/oauth2/v1/token",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": None,
            "form": {
                "grant_type": "client_credentials"
            }
        }

        # Request 2: Regular JSON API request
        request2 = {
            "method": "GET",
            "url": "https://test.okta.com/api/v1/users",
            "headers": {
                "Authorization": "Bearer test_token",
                "Content-Type": "application/json"
            },
            "data": None,
            "form": None
        }

        # Request 3: Another OAuth request
        request3 = {
            "method": "POST",
            "url": "https://test.okta.com/oauth2/v1/token",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": None,
            "form": {
                "grant_type": "refresh_token"
            }
        }

        mock_response = AsyncMock()
        mock_response.request_info = MagicMock()
        mock_response.status = 200
        mock_response.text = AsyncMock(return_value='{"success": true}')

        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = AsyncMock()
            mock_session.request = AsyncMock(return_value=mock_response)
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock()
            mock_session_class.return_value = mock_session

            # Execute all requests
            await http_client.send_request(request1)
            assert http_client._default_headers == initial_headers, \
                "Headers mutated after request 1"

            await http_client.send_request(request2)
            assert http_client._default_headers == initial_headers, \
                "Headers mutated after request 2"

            await http_client.send_request(request3)
            assert http_client._default_headers == initial_headers, \
                "Headers mutated after request 3"

    @pytest.mark.asyncio
    async def test_custom_headers_per_request(self):
        """Test that each request can have custom headers without affecting others"""

        http_config = {
            "headers": {
                "User-Agent": "okta-sdk-python"
            }
        }
        http_client = HTTPClient(http_config)

        captured_headers = []

        # Create a factory function for the context manager
        def create_request_context(**kwargs):
            # Capture headers when request is created
            captured_headers.append(dict(kwargs.get("headers", {})))

            # Create async context manager
            mock_response = AsyncMock()
            mock_response.request_info = MagicMock()
            mock_response.status = 200
            mock_response.text = AsyncMock(return_value='{"success": true}')

            mock_context = MagicMock()
            mock_context.__aenter__ = AsyncMock(return_value=mock_response)
            mock_context.__aexit__ = AsyncMock(return_value=False)
            return mock_context

        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = MagicMock()
            mock_session.request = MagicMock(side_effect=create_request_context)
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock()
            mock_session_class.return_value = mock_session

            # Request 1 with custom header
            request1 = {
                "method": "GET",
                "url": "https://test.okta.com/api/v1/users",
                "headers": {"X-Custom-1": "value1"},
                "data": None,
                "form": None
            }
            await http_client.send_request(request1)

            # Request 2 with different custom header
            request2 = {
                "method": "GET",
                "url": "https://test.okta.com/api/v1/groups",
                "headers": {"X-Custom-2": "value2"},
                "data": None,
                "form": None
            }
            await http_client.send_request(request2)

        # Verify we captured headers
        assert len(captured_headers) == 2, f"Expected 2 captured headers, got {len(captured_headers)}"

        # Verify each request had only its own custom headers
        assert "X-Custom-1" in captured_headers[0]
        assert "X-Custom-2" not in captured_headers[0]

        assert "X-Custom-2" in captured_headers[1]
        assert "X-Custom-1" not in captured_headers[1]

        # Verify default headers not polluted
        assert "X-Custom-1" not in http_client._default_headers
        assert "X-Custom-2" not in http_client._default_headers


class TestFormDataBranching:
    """Test the branching logic between file uploads and regular form data"""

    @pytest.mark.asyncio
    async def test_form_with_file_key_uses_formdata(self):
        """Test that forms with 'file' key use aiohttp.FormData"""

        http_config = {"headers": {"User-Agent": "test"}}
        http_client = HTTPClient(http_config)

        request = {
            "method": "POST",
            "url": "https://test.okta.com/upload",
            "headers": {"Content-Type": "multipart/form-data"},
            "data": None,
            "form": {"file": "/tmp/test.txt"}
        }

        mock_response = AsyncMock()
        mock_response.request_info = MagicMock()
        mock_response.status = 200
        mock_response.text = AsyncMock(return_value='{}')

        with patch('aiohttp.ClientSession') as mock_session_class, \
             patch('builtins.open', mock_open(read_data=b"content")):

            mock_session = AsyncMock()
            mock_session.request = AsyncMock(return_value=mock_response)
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock()
            mock_session_class.return_value = mock_session

            await http_client.send_request(request)

            call_kwargs = mock_session.request.call_args[1]
            assert isinstance(call_kwargs["data"], aiohttp.FormData)

    @pytest.mark.asyncio
    async def test_form_without_file_key_uses_dict(self):
        """Test that forms without 'file' key use plain dict"""

        http_config = {"headers": {"User-Agent": "test"}}
        http_client = HTTPClient(http_config)

        request = {
            "method": "POST",
            "url": "https://test.okta.com/api",
            "headers": {"Content-Type": "application/x-www-form-urlencoded"},
            "data": None,
            "form": {"key1": "value1", "key2": "value2"}
        }

        mock_response = AsyncMock()
        mock_response.request_info = MagicMock()
        mock_response.status = 200
        mock_response.text = AsyncMock(return_value='{}')

        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = AsyncMock()
            mock_session.request = AsyncMock(return_value=mock_response)
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock()
            mock_session_class.return_value = mock_session

            await http_client.send_request(request)

            call_kwargs = mock_session.request.call_args[1]
            assert isinstance(call_kwargs["data"], dict)
            assert call_kwargs["data"] == {"key1": "value1", "key2": "value2"}


if __name__ == "__main__":
    # Run tests with pytest
    import sys
    sys.exit(pytest.main([__file__, "-v", "-s"]))




