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

from okta.models.user_type\
    import UserType
from okta.utils import format_url
from okta.api_client import APIClient


class UserTypeClient(APIClient):
    """
    A Client object for the UserType resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_user_types(
            self
    ):
        """
        Fetches all User Types in your org
        Args:
        Returns:
            list: Collection of UserType instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserType)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(UserType(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_user_type(
            self, user_type
    ):
        """
        Creates a new User Type. A default User Type is automat
        ically created along with your org, and you may add ano
        ther 9 User Types for a maximum of 10.
        Args:
            {user_type}
        Returns:
            UserType
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user
            """)

        if isinstance(user_type, dict):
            body = user_type
        else:
            body = user_type.as_dict()
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
            .execute(request, UserType)

        if error:
            return (None, response, error)

        try:
            result = UserType(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_user_type(
            self, typeId
    ):
        """
        Deletes a User Type permanently. This operation is not
        permitted for the default type, nor for any User Type t
        hat has existing users
        Args:
            type_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user/{typeId}
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

    async def get_user_type(
            self, typeId
    ):
        """
        Fetches a User Type by ID. The special identifier `defa
        ult` may be used to fetch the default User Type.
        Args:
            type_id {str}
        Returns:
            UserType
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user/{typeId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserType)

        if error:
            return (None, response, error)

        try:
            result = UserType(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_user_type(
            self, typeId, user_type
    ):
        """
        Updates an existing User Type
        Args:
            type_id {str}
            {user_type}
        Returns:
            UserType
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user/{typeId}
            """)

        if isinstance(user_type, dict):
            body = user_type
        else:
            body = user_type.as_dict()
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
            .execute(request, UserType)

        if error:
            return (None, response, error)

        try:
            result = UserType(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def replace_user_type(
            self, typeId, user_type
    ):
        """
        Replace an existing User Type
        Args:
            type_id {str}
            {user_type}
        Returns:
            UserType
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user/{typeId}
            """)

        if isinstance(user_type, dict):
            body = user_type
        else:
            body = user_type.as_dict()
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
            .execute(request, UserType)

        if error:
            return (None, response, error)

        try:
            result = UserType(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
