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


class EventHook:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.channel = config["channel"]
            self.created = config["created"]
            self.created_by = config["createdBy"]
            self.events = config["events"]
            self.id = config["id"]
            self.last_updated = config["lastUpdated"]
            self.name = config["name"]
            self.status = config["status"]
            self.verification_status = config["verificationStatus"]
        else:
            self.links = None
            self.channel = None
            self.created = None
            self.created_by = None
            self.events = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.status = None
            self.verification_status = None

    
    async def create_event_hook(
            self, event_hook
    ):
        """
            Success
        Args:
            {event_hook}
        Returns:
            EventHook
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/eventHooks
            """)

        body = event_hook
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
            result = EventHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def get_event_hook(
            self, eventHookId
    ):
        """
            Success
        Args:
            event_hook_id {str}
        Returns:
            EventHook
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}
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
            result = EventHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def update_event_hook(
            self, eventHookId, event_hook
    ):
        """
            Success
        Args:
            event_hook_id {str}
            {event_hook}
        Returns:
            EventHook
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}
            """)

        body = event_hook
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
            result = EventHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def delete_event_hook(
            self, eventHookId
    ):
        """
            Success
        Args:
            event_hook_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}
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

    
    async def list_event_hooks(
            self
    ):
        """
            Success
        Args:
        Returns:
            list: Collection of EventHook instances.
        """
        http_method = "get".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/eventHooks
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
        result = []
        for item in response.get_body():
            result.append(EventHook(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def activate_event_hook(
            self, eventHookId
    ):
        """
            Success
        Args:
            event_hook_id {str}
        Returns:
            EventHook
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}/lifecycle/activate
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
            result = EventHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def deactivate_event_hook(
            self, eventHookId
    ):
        """
            Success
        Args:
            event_hook_id {str}
        Returns:
            EventHook
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}/lifecycle
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
            result = EventHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def verify_event_hook(
            self, eventHookId
    ):
        """
            Success
        Args:
            event_hook_id {str}
        Returns:
            EventHook
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/eventHooks/{eventHookId}/lifecycle/verify
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
            result = EventHook(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation
