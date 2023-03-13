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
from okta.models.authenticator\
    import Authenticator
from okta.utils import format_url
from okta.api_client import APIClient


class AuthenticatorClient(APIClient):
    """
    A Client object for the Authenticator resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_authenticators(
            self,
            keep_empty_params=False
    ):
        """
        List Authenticators
        Args:
        Returns:
            list: Collection of Authenticator instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authenticators
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Authenticator)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Authenticator(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_authenticator(
            self, authenticator, query_params={},
            keep_empty_params=False
    ):
        """
        Create Authenticator
        Args:
            {authenticator}
            query_params {dict}: Map of query parameters for request
            [query_params.activate] {str}
        Returns:
            Authenticator
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authenticators
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(authenticator, dict):
            body = authenticator
        else:
            body = authenticator.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Authenticator)

        if error:
            return (None, response, error)

        try:
            result = Authenticator(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_authenticator(
            self, authenticatorId,
            keep_empty_params=False
    ):
        """
        Args:
            authenticator_id {str}
        Returns:
            Authenticator
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authenticators/{authenticatorId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Authenticator)

        if error:
            return (None, response, error)

        try:
            result = Authenticator(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_authenticator(
            self, authenticatorId, authenticator,
            keep_empty_params=False
    ):
        """
        Updates an authenticator
        Args:
            authenticator_id {str}
            {authenticator}
        Returns:
            Authenticator
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authenticators/{authenticatorId}
            """)

        if isinstance(authenticator, dict):
            body = authenticator
        else:
            body = authenticator.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Authenticator)

        if error:
            return (None, response, error)

        try:
            result = Authenticator(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_authenticator(
            self, authenticatorId,
            keep_empty_params=False
    ):
        """
        Args:
            authenticator_id {str}
        Returns:
            Authenticator
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authenticators/{authenticatorId}/lifecycle
                /activate
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Authenticator)

        if error:
            return (None, response, error)

        try:
            result = Authenticator(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def deactivate_authenticator(
            self, authenticatorId,
            keep_empty_params=False
    ):
        """
        Args:
            authenticator_id {str}
        Returns:
            Authenticator
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authenticators/{authenticatorId}/lifecycle
                /deactivate
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Authenticator)

        if error:
            return (None, response, error)

        try:
            result = Authenticator(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
