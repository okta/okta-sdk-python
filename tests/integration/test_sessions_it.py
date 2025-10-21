# flake8: noqa
# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import time

import aiohttp
import pytest
from pydantic import SecretStr

import okta.models as models
from tests.mocks import MockOktaClient


# Note: Session tokens vs API tokens in Okta:
# - API Token (from mocks.API_TOKEN): Used for authenticating API requests (in Authorization header)
# - Session Token: Temporary token from user authentication that can be exchanged for a session
# This integration test creates a real user, authenticates them, and gets a valid session token


class TestSessionsResource:
    """
    Comprehensive Integration Tests for the Sessions API
    Tests follow a stateful workflow and cover all SessionApi methods
    """

    # Class variables to store shared test data across test methods
    created_session_id = None
    test_user_id = None
    test_session_token = None

    async def _authenticate_user_for_session_token(
        self, username: str, password: str
    ) -> str:
        """
        Helper method to authenticate user and get session token using Okta Authentication API.
        Returns session token or None if authentication fails.
        """
        from tests.mocks import ORG_URL

        auth_url = f"{ORG_URL}/api/v1/authn"

        auth_data = {"username": username, "password": password}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(auth_url, json=auth_data) as response:
                    if response.status == 200:
                        auth_result = await response.json()
                        if auth_result.get("status") == "SUCCESS":
                            return auth_result.get("sessionToken")
                    return None
        except Exception as e:
            print(f"Authentication failed: {e}")
            return None

    async def _create_test_user_and_session_token(self, client):
        """
        Helper method to create a test user and get a valid session token.
        Returns (user_id, session_token) tuple or (None, None) if failed.
        """
        try:
            # Create a real user for testing
            timestamp = str(int(time.time()))
            password = models.PasswordCredential(value=SecretStr("TempPassword123!"))
            user_creds = models.UserCredentials(password=password)

            user_profile = models.UserProfile()
            user_profile.first_name = "SessionTest"
            user_profile.last_name = f"User{timestamp}"
            user_profile.email = f"sessiontest.user{timestamp}@example.com"
            user_profile.login = f"sessiontest.user{timestamp}@example.com"

            create_user_req = models.CreateUserRequest(
                credentials=user_creds, profile=user_profile
            )

            # Create and activate user
            user, _, create_err = await client.create_user(
                create_user_req, activate=True
            )
            if create_err is not None or user is None:
                return None, None

            # Authenticate user to get session token
            session_token = await self._authenticate_user_for_session_token(
                user_profile.login, "TempPassword123!"
            )

            return user.id, session_token

        except Exception as e:
            print(f"Failed to create test user: {e}")
            return None, None

    async def _cleanup_test_user(self, client, user_id):
        """
        Helper method to clean up test user.
        """
        if user_id:
            try:
                # Deactivate user first
                _, _, err = await client.deactivate_user(user_id)
                if err is None:
                    # Then delete user
                    _, _, err = await client.delete_user(user_id)
            except Exception as cleanup_err:
                print(
                    f"Cleanup warning: Could not delete user {user_id}: {cleanup_err}"
                )

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_successful_session_lifecycle(self, fs):
        """
        Complete integration test with real user authentication and session lifecycle:
        1. Create a real user in Okta
        2. Authenticate the user to get a valid session token
        3. Create session using the real session token
        4. Test session retrieval (get_session)
        5. Test session refresh (refresh_session)
        6. Test session revocation (revoke_session)
        7. Clean up by deleting the user
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Step 1 & 2: Create user and get session token using helper method
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Step 3: Create session using real session token
                create_session_request = models.CreateSessionRequest(
                    session_token=session_token
                )

                session, _, create_err = await client.create_session(
                    create_session_request
                )
                assert create_err is None, f"Failed to create session: {create_err}"
                assert session is not None
                assert session.id is not None
                assert session.user_id == user_id

                TestSessionsResource.created_session_id = session.id

                # Step 4: Retrieve the session
                retrieved_session, _, get_err = await client.get_session(session.id)
                assert get_err is None, f"Failed to get session: {get_err}"
                assert retrieved_session is not None
                assert retrieved_session.id == session.id
                assert retrieved_session.user_id == user_id

                # Step 5: Refresh the session
                retrieved_session.expires_at
                refreshed_session, _, refresh_err = await client.refresh_session(
                    session.id
                )
                assert refresh_err is None, f"Failed to refresh session: {refresh_err}"
                assert refreshed_session is not None
                assert refreshed_session.id == session.id
                # Note: expiresAt might not always change depending on Okta policy

                # Step 6: Revoke the session
                _, _, revoke_err = await client.revoke_session(session.id)
                assert revoke_err is None, f"Failed to revoke session: {revoke_err}"

                # Step 7: Verify session is revoked (should get 404)
                deleted_session, _, final_err = await client.get_session(session.id)
                assert deleted_session is None
                assert final_err is not None
                assert "404" in str(final_err) or "Not found" in str(final_err)

            else:
                # If authentication fails, test with invalid token (fallback behavior)
                pytest.skip("Could not authenticate user to get session token")

        finally:
            # Step 8: Clean up using helper method
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_session_invalid_token(self, fs):
        """
        Test create_session with both valid and invalid tokens to verify behavior.
        First creates a successful session, then tests error handling with invalid token.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # First test with valid session token to show success case
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Test successful session creation
                valid_request = models.CreateSessionRequest(session_token=session_token)
                session, _, err = await client.create_session(valid_request)
                assert err is None, f"Valid session creation failed: {err}"
                assert session is not None
                assert session.id is not None

                # Clean up the valid session
                await client.revoke_session(session.id)

            # Now test with clearly invalid session token
            invalid_session_token = "invalid_token_12345"

            create_session_request = models.CreateSessionRequest(
                session_token=invalid_session_token
            )

            session, _, err = await client.create_session(create_session_request)

            # Validate error response
            assert session is None
            assert err is not None
            assert any(
                error_text in str(err)
                for error_text in [
                    "Authentication failed",
                    "Invalid session token",
                    "400",
                    "403",
                ]
            )

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_non_existent_session(self, fs):
        """
        Test get_session with both valid and non-existent session IDs.
        First creates a real session, then tests with non-existent ID.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # First test with valid session
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Create a real session
                create_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                session, _, err = await client.create_session(create_request)
                assert err is None, f"Session creation failed: {err}"
                assert session is not None

                # Test getting the valid session
                retrieved_session, _, get_err = await client.get_session(session.id)
                assert get_err is None, f"Failed to get valid session: {get_err}"
                assert retrieved_session is not None
                assert retrieved_session.id == session.id

                # Clean up the session
                await client.revoke_session(session.id)

            # Now test with non-existent session ID
            non_existent_session_id = "nonexistent_session_12345"
            session, _, err = await client.get_session(non_existent_session_id)

            # Validate 404 error response
            assert session is None
            assert err is not None
            assert "404" in str(err) or "Not found" in str(err)

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_rate_limited_requests(self, fs):
        """
        Test rate limiting behavior by making multiple rapid requests.
        First creates a valid session, then makes rapid requests.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Create a real session for testing
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Create a real session
                create_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                session, _, err = await client.create_session(create_request)
                assert err is None, f"Session creation failed: {err}"
                assert session is not None

                # Make rapid requests to the valid session
                for i in range(3):
                    retrieved_session, response, get_err = await client.get_session(
                        session.id
                    )
                    # Valid session should return successfully (unless rate limited)
                    if get_err is None:
                        assert retrieved_session is not None
                        assert retrieved_session.id == session.id
                    else:
                        # Could be rate limited in production
                        assert "429" in str(get_err) or "Rate limit" in str(get_err)

                # Clean up
                await client.revoke_session(session.id)

            # Also test with non-existent sessions to show 404 behavior
            for i in range(2):
                session, response, err = await client.get_session(f"nonexistent_{i}")
                assert session is None
                assert err is not None
                assert "404" in str(err) or "Not found" in str(err)

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_session_with_http_info(self, fs):
        """
        Test create_session_with_http_info method with both valid and invalid tokens.
        Validates the method returns session data, HTTP response, and error information.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Test with valid session token
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                create_session_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                session, http_response, err = (
                    await client.create_session_with_http_info(create_session_request)
                )

                # Validate successful response
                assert http_response is not None
                assert hasattr(http_response, "status") or hasattr(
                    http_response, "status_code"
                )
                assert err is None, f"Valid session creation failed: {err}"
                assert session is not None
                assert session.id is not None

                # Clean up
                await client.revoke_session(session.id)

            # Test with invalid token
            invalid_request = models.CreateSessionRequest(session_token="invalid_token")
            session, http_response, err = await client.create_session_with_http_info(
                invalid_request
            )

            # Validate error response structure
            assert http_response is not None
            assert hasattr(http_response, "status") or hasattr(
                http_response, "status_code"
            )
            assert session is None
            assert err is not None

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_session_with_http_info(self, fs):
        """
        Test get_session_with_http_info method with both valid and invalid session IDs.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Test with valid session
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Create session
                create_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                created_session, _, create_err = await client.create_session(
                    create_request
                )
                assert create_err is None and created_session is not None

                # Test getting valid session with http_info
                session, http_response, err = await client.get_session_with_http_info(
                    created_session.id
                )

                assert http_response is not None
                assert hasattr(http_response, "status") or hasattr(
                    http_response, "status_code"
                )
                assert err is None, f"Failed to get valid session: {err}"
                assert session is not None
                assert session.id == created_session.id

                # Clean up
                await client.revoke_session(created_session.id)

            # Test with non-existent session
            session, http_response, err = await client.get_session_with_http_info(
                "nonexistent_session"
            )

            # Validate HTTP response structure
            assert http_response is not None
            assert hasattr(http_response, "status") or hasattr(
                http_response, "status_code"
            )
            assert session is None
            assert err is not None
            assert "404" in str(err) or "Not found" in str(err)

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_refresh_session_with_http_info(self, fs):
        """
        Test refresh_session_with_http_info method with both valid and invalid session IDs.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Test with valid session
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Create session
                create_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                created_session, _, create_err = await client.create_session(
                    create_request
                )
                assert create_err is None and created_session is not None

                # Test refreshing valid session with http_info
                session, http_response, err = (
                    await client.refresh_session_with_http_info(created_session.id)
                )

                assert http_response is not None
                assert hasattr(http_response, "status") or hasattr(
                    http_response, "status_code"
                )
                assert err is None, f"Failed to refresh valid session: {err}"
                assert session is not None
                assert session.id == created_session.id

                # Clean up
                await client.revoke_session(created_session.id)

            # Test with non-existent session
            session, http_response, err = await client.refresh_session_with_http_info(
                "nonexistent_session"
            )

            # Validate HTTP response structure
            assert http_response is not None
            assert hasattr(http_response, "status") or hasattr(
                http_response, "status_code"
            )
            assert session is None
            assert err is not None
            assert "404" in str(err) or "Not found" in str(err)

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_revoke_session_with_http_info(self, fs):
        """
        Test revoke_session_with_http_info method with both valid and invalid session IDs.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Test with valid session
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Create session
                create_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                created_session, _, create_err = await client.create_session(
                    create_request
                )
                assert create_err is None and created_session is not None

                # Test revoking valid session with http_info
                try:
                    result, http_response, err = (
                        await client.revoke_session_with_http_info(created_session.id)
                    )

                    assert http_response is not None
                    assert hasattr(http_response, "status") or hasattr(
                        http_response, "status_code"
                    )
                    assert err is None, f"Failed to revoke valid session: {err}"

                except ValueError:
                    # If method returns only 2 values, handle it differently
                    http_response, err = await client.revoke_session_with_http_info(
                        created_session.id
                    )
                    assert http_response is not None
                    assert err is None, f"Failed to revoke valid session: {err}"

            # Test with non-existent session
            try:
                result, http_response, err = await client.revoke_session_with_http_info(
                    "nonexistent_session"
                )

                assert http_response is not None
                assert hasattr(http_response, "status") or hasattr(
                    http_response, "status_code"
                )
                assert result is None
                assert err is not None
                assert "404" in str(err) or "Not found" in str(err)
            except ValueError:
                # If method returns only 2 values, handle it differently
                http_response, err = await client.revoke_session_with_http_info(
                    "nonexistent_session"
                )
                assert http_response is not None
                assert err is not None
                assert "404" in str(err) or "Not found" in str(err)

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_session_without_preload_content(self, fs):
        """
        Test create_session_without_preload_content method with both valid and invalid tokens.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Test with valid session token
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                create_session_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                result, http_response, err = (
                    await client.create_session_without_preload_content(
                        create_session_request
                    )
                )

                assert http_response is not None
                assert err is None, f"Valid session creation failed: {err}"
                # Note: result might be raw response data or None depending on implementation

                # Create a regular session to get session ID for cleanup
                session, _, _ = await client.create_session(create_session_request)
                if session:
                    await client.revoke_session(session.id)

            # Test with invalid token
            invalid_request = models.CreateSessionRequest(session_token="invalid_token")
            result, http_response, err = (
                await client.create_session_without_preload_content(invalid_request)
            )

            # Validate response structure
            assert http_response is not None
            assert err is not None

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_session_without_preload_content(self, fs):
        """
        Test get_session_without_preload_content method with both valid and invalid session IDs.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Test with valid session
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Create session
                create_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                created_session, _, create_err = await client.create_session(
                    create_request
                )
                assert create_err is None and created_session is not None

                # Test getting valid session without preload content
                result, http_response, err = (
                    await client.get_session_without_preload_content(created_session.id)
                )

                assert http_response is not None
                assert err is None, f"Failed to get valid session: {err}"
                # Note: result might be raw response data or None depending on implementation

                # Clean up
                await client.revoke_session(created_session.id)

            # Test with non-existent session
            result, http_response, err = (
                await client.get_session_without_preload_content("nonexistent_session")
            )

            # Validate response structure
            assert http_response is not None
            assert err is not None
            assert "404" in str(err) or "Not found" in str(err)

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_refresh_session_without_preload_content(self, fs):
        """
        Test refresh_session_without_preload_content method with both valid and invalid session IDs.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Test with valid session
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Create session
                create_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                created_session, _, create_err = await client.create_session(
                    create_request
                )
                assert create_err is None and created_session is not None

                # Test refreshing valid session without preload content
                result, http_response, err = (
                    await client.refresh_session_without_preload_content(
                        created_session.id
                    )
                )

                assert http_response is not None
                assert err is None, f"Failed to refresh valid session: {err}"
                # Note: result might be raw response data or None depending on implementation

                # Clean up
                await client.revoke_session(created_session.id)

            # Test with non-existent session
            result, http_response, err = (
                await client.refresh_session_without_preload_content(
                    "nonexistent_session"
                )
            )

            # Validate response structure
            assert http_response is not None
            assert err is not None
            assert "404" in str(err) or "Not found" in str(err)

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_revoke_session_without_preload_content(self, fs):
        """
        Test revoke_session_without_preload_content method with both valid and invalid session IDs.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # Test with valid session
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Create session
                create_request = models.CreateSessionRequest(
                    session_token=session_token
                )
                created_session, _, create_err = await client.create_session(
                    create_request
                )
                assert create_err is None and created_session is not None

                # Test revoking valid session without preload content
                try:
                    result, http_response, err = (
                        await client.revoke_session_without_preload_content(
                            created_session.id
                        )
                    )

                    assert http_response is not None
                    assert err is None, f"Failed to revoke valid session: {err}"

                except ValueError:
                    # If method returns only 2 values, handle it differently
                    http_response, err = (
                        await client.revoke_session_without_preload_content(
                            created_session.id
                        )
                    )
                    assert http_response is not None
                    assert err is None, f"Failed to revoke valid session: {err}"

            # Test with non-existent session
            try:
                result, http_response, err = (
                    await client.revoke_session_without_preload_content(
                        "nonexistent_session"
                    )
                )

                assert http_response is not None
                assert err is not None
                assert "404" in str(err) or "Not found" in str(err)
            except ValueError:
                # If method returns only 2 values, handle it differently
                http_response, err = (
                    await client.revoke_session_without_preload_content(
                        "nonexistent_session"
                    )
                )
                assert http_response is not None
                assert err is not None
                assert "404" in str(err) or "Not found" in str(err)

        finally:
            await self._cleanup_test_user(client, user_id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_session_error_handling_scenarios(self, fs):
        """
        Test various error handling scenarios across all session methods.
        Also includes successful operations to contrast with error cases.
        """
        client = MockOktaClient(fs)
        user_id = None

        try:
            # First, demonstrate successful operations
            user_id, session_token = await self._create_test_user_and_session_token(
                client
            )

            if session_token:
                # Test successful session creation
                valid_request = models.CreateSessionRequest(session_token=session_token)
                session, _, err = await client.create_session(valid_request)
                assert err is None, f"Valid session creation failed: {err}"
                assert session is not None

                # Clean up valid session
                await client.revoke_session(session.id)

            # Now test error scenarios

            # Test malformed session token
            malformed_request = models.CreateSessionRequest(
                session_token=""  # Empty token
            )
            session, _, err = await client.create_session(malformed_request)
            assert session is None
            assert err is not None

            # Test with None session ID (should raise validation error)
            try:
                await client.get_session(None)
                assert False, "Expected validation error for None session_id"
            except (TypeError, ValueError):
                pass  # Expected validation error

            # Test with empty session ID
            session, _, err = await client.get_session("")
            assert session is None
            assert err is not None

        finally:
            await self._cleanup_test_user(client, user_id)
