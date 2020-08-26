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

from okta.models.event_hook\
    import EventHook
from okta.utils import format_url
from okta.api_client import APIClient


class EventHookClient(APIClient):
    """
    A Client object for the EventHook resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_event_hooks(
            self
    ):
        """
        Args:
        Returns:
            list: Collection of EventHook instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/eventHooks
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, EventHook)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(EventHook(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_event_hook(
            self, event_hook
    ):
        """
        Args:
            {event_hook}
        Returns:
            EventHook
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/eventHooks
            """)

        if isinstance(event_hook, dict):
            body = event_hook
        else:
            body = event_hook.as_dict()
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
            .execute(request, EventHook)

        if error:
            return (None, response, error)

        try:
            result = EventHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_event_hook(
            self, eventHookId
    ):
        """
        Args:
            event_hook_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}
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

    async def get_event_hook(
            self, eventHookId
    ):
        """
        Args:
            event_hook_id {str}
        Returns:
            EventHook
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, EventHook)

        if error:
            return (None, response, error)

        try:
            result = EventHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_event_hook(
            self, eventHookId, event_hook
    ):
        """
        Args:
            event_hook_id {str}
            {event_hook}
        Returns:
            EventHook
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}
            """)

        if isinstance(event_hook, dict):
            body = event_hook
        else:
            body = event_hook.as_dict()
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
            .execute(request, EventHook)

        if error:
            return (None, response, error)

        try:
            result = EventHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_event_hook(
            self, eventHookId
    ):
        """
        Args:
            event_hook_id {str}
        Returns:
            EventHook
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}/lifecycle/activate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, EventHook)

        if error:
            return (None, response, error)

        try:
            result = EventHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def deactivate_event_hook(
            self, eventHookId
    ):
        """
        Args:
            event_hook_id {str}
        Returns:
            EventHook
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}/lifecycle
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
            .execute(request, EventHook)

        if error:
            return (None, response, error)

        try:
            result = EventHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def verify_event_hook(
            self, eventHookId
    ):
        """
        Args:
            event_hook_id {str}
        Returns:
            EventHook
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}/lifecycle/verify
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, EventHook)

        if error:
            return (None, response, error)

        try:
            result = EventHook(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
