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

from okta.models.linked_object\
    import LinkedObject
from okta.utils import format_url
from okta.api_client import APIClient


class LinkedObjectClient(APIClient):
    """
    A Client object for the LinkedObject resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_linked_object_definitions(
            self
    ):
        """
        Args:
        Returns:
            list: Collection of LinkedObject instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/user/linkedObjects
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, LinkedObject)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(LinkedObject(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def add_linked_object_definition(
            self, linked_object
    ):
        """
        Args:
            {linked_object}
        Returns:
            LinkedObject
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/user/linkedObjects
            """)

        if isinstance(linked_object, dict):
            body = linked_object
        else:
            body = linked_object.as_dict()
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
            .execute(request, LinkedObject)

        if error:
            return (None, response, error)

        try:
            result = LinkedObject(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_linked_object_definition(
            self, linkedObjectName
    ):
        """
        Args:
            linked_object_name {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/user/linkedObjects
                /{linkedObjectName}
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

    async def get_linked_object_definition(
            self, linkedObjectName
    ):
        """
        Args:
            linked_object_name {str}
        Returns:
            LinkedObject
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/user/linkedObjects
                /{linkedObjectName}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, LinkedObject)

        if error:
            return (None, response, error)

        try:
            result = LinkedObject(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
