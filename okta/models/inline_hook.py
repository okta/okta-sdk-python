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


class InlineHook:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.channel = config["channel"]
            self.created = config["created"]
            self.id = config["id"]
            self.last_updated = config["lastUpdated"]
            self.name = config["name"]
            self.status = config["status"]
            self.type = config["type"]
            self.version = config["version"]
        else:
            self.links = None
            self.channel = None
            self.created = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.status = None
            self.type = None
            self.version = None

    
    async def create_inline_hook(
            self, inline_hook
    ):
        """
            Success
        Args:
            {inline_hook}
        Returns:
            InlineHook
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks
            """)

        body = inline_hook
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = InlineHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Gets an inline hook by ID
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = InlineHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Updates an inline hook by ID
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}
            """)

        body = inline_hook
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = InlineHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Deletes the Inline Hook matching the provided id. Once deleted, the Inline Hook is unrecoverable. As a safety precaution, only Inline Hooks with a status of INACTIVE are eligible for deletion.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)

    
    async def list_inline_hooks(
            self, query_params
    ):
        """
            Success
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.type] {str}
        Returns:
            list: Collection of InlineHook instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
        result = []
        for item in response.get_body():
            result.append(InlineHook(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Executes the Inline Hook matching the provided inlineHookId using the request body as the input. This will send the provided data through the Channel and return a response if it matches the correct data contract. This execution endpoint should only be used for testing purposes.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}/execute
            """)

        body = inline_hook_payload
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = InlineHookResponse(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Activates the Inline Hook matching the provided id
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}/lifecycle
                activate
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = InlineHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Deactivates the Inline Hook matching the provided id
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/inlineHooks/{inlineHookId}/lifecycle
                deactivate
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = InlineHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation
