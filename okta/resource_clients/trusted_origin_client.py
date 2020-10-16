"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from urllib.parse import urlencode
from okta.models.trusted_origin\
    import TrustedOrigin
from okta.utils import format_url
from okta.api_client import APIClient


class TrustedOriginClient(APIClient):
    """
    A Client object for the TrustedOrigin resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_origins(
            self, query_params={}
    ):
        """
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.filter] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of TrustedOrigin instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/trustedOrigins
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, TrustedOrigin)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(TrustedOrigin(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_origin(
            self, trusted_origin
    ):
        """
        Args:
            {trusted_origin}
        Returns:
            TrustedOrigin
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/trustedOrigins
            """)

        if isinstance(trusted_origin, dict):
            body = trusted_origin
        else:
            body = trusted_origin.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, TrustedOrigin)

        if error:
            return (None, response, error)

        try:
            result = TrustedOrigin(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_origin(
            self, trustedOriginId
    ):
        """
        Args:
            trusted_origin_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/trustedOrigins/{trustedOriginId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_origin(
            self, trustedOriginId
    ):
        """
        Args:
            trusted_origin_id {str}
        Returns:
            TrustedOrigin
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/trustedOrigins/{trustedOriginId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, TrustedOrigin)

        if error:
            return (None, response, error)

        try:
            result = TrustedOrigin(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_origin(
            self, trustedOriginId, trusted_origin
    ):
        """
        Args:
            trusted_origin_id {str}
            {trusted_origin}
        Returns:
            TrustedOrigin
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/trustedOrigins/{trustedOriginId}
            """)

        if isinstance(trusted_origin, dict):
            body = trusted_origin
        else:
            body = trusted_origin.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, TrustedOrigin)

        if error:
            return (None, response, error)

        try:
            result = TrustedOrigin(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_origin(
            self, trustedOriginId
    ):
        """
        Args:
            trusted_origin_id {str}
        Returns:
            TrustedOrigin
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/trustedOrigins/{trustedOriginId}/lifecycle
                /activate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, TrustedOrigin)

        if error:
            return (None, response, error)

        try:
            result = TrustedOrigin(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def deactivate_origin(
            self, trustedOriginId
    ):
        """
        Args:
            trusted_origin_id {str}
        Returns:
            TrustedOrigin
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/trustedOrigins/{trustedOriginId}/lifecycle
                /deactivate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, TrustedOrigin)

        if error:
            return (None, response, error)

        try:
            result = TrustedOrigin(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
