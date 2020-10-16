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
from okta.models.inline_hook\
    import InlineHook
from okta.models.inline_hook_response\
    import InlineHookResponse
from okta.utils import format_url
from okta.api_client import APIClient


class InlineHookClient(APIClient):
    """
    A Client object for the InlineHook resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_inline_hooks(
            self, query_params={}
    ):
        """
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.type] {str}
        Returns:
            list: Collection of InlineHook instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks
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
            .execute(request, InlineHook)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(InlineHook(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_inline_hook(
            self, inline_hook
    ):
        """
        Args:
            {inline_hook}
        Returns:
            InlineHook
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks
            """)

        if isinstance(inline_hook, dict):
            body = inline_hook
        else:
            body = inline_hook.as_dict()
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
            .execute(request, InlineHook)

        if error:
            return (None, response, error)

        try:
            result = InlineHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_inline_hook(
            self, inlineHookId
    ):
        """
        Deletes the Inline Hook matching the provided id. Once
        deleted, the Inline Hook is unrecoverable. As a safety
        precaution, only Inline Hooks with a status of INACTIVE
        are eligible for deletion.
        Args:
            inline_hook_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}
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

    async def get_inline_hook(
            self, inlineHookId
    ):
        """
        Gets an inline hook by ID
        Args:
            inline_hook_id {str}
        Returns:
            InlineHook
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, InlineHook)

        if error:
            return (None, response, error)

        try:
            result = InlineHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_inline_hook(
            self, inlineHookId, inline_hook
    ):
        """
        Updates an inline hook by ID
        Args:
            inline_hook_id {str}
            {inline_hook}
        Returns:
            InlineHook
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}
            """)

        if isinstance(inline_hook, dict):
            body = inline_hook
        else:
            body = inline_hook.as_dict()
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
            .execute(request, InlineHook)

        if error:
            return (None, response, error)

        try:
            result = InlineHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def execute_inline_hook(
            self, inlineHookId, inline_hook_payload
    ):
        """
        Executes the Inline Hook matching the provided inlineHo
        okId using the request body as the input. This will sen
        d the provided data through the Channel and return a re
        sponse if it matches the correct data contract. This ex
        ecution endpoint should only be used for testing purpos
        es.
        Args:
            inline_hook_id {str}
            {inline_hook_payload}
        Returns:
            InlineHookResponse
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}/execute
            """)

        if isinstance(inline_hook_payload, dict):
            body = inline_hook_payload
        else:
            body = inline_hook_payload.as_dict()
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
            .execute(request, InlineHookResponse)

        if error:
            return (None, response, error)

        try:
            result = InlineHookResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_inline_hook(
            self, inlineHookId
    ):
        """
        Activates the Inline Hook matching the provided id
        Args:
            inline_hook_id {str}
        Returns:
            InlineHook
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}/lifecycle
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
            .execute(request, InlineHook)

        if error:
            return (None, response, error)

        try:
            result = InlineHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def deactivate_inline_hook(
            self, inlineHookId
    ):
        """
        Deactivates the Inline Hook matching the provided id
        Args:
            inline_hook_id {str}
        Returns:
            InlineHook
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}/lifecycle
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
            .execute(request, InlineHook)

        if error:
            return (None, response, error)

        try:
            result = InlineHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
