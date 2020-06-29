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


class UserType:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.created = config["created"]
            self.created_by = config["createdBy"]
            self.default = config["default"]
            self.description = config["description"]
            self.display_name = config["displayName"]
            self.id = config["id"]
            self.last_updated = config["lastUpdated"]
            self.last_updated_by = config["lastUpdatedBy"]
            self.name = config["name"]
        else:
            self.links = None
            self.created = None
            self.created_by = None
            self.default = None
            self.description = None
            self.display_name = None
            self.id = None
            self.last_updated = None
            self.last_updated_by = None
            self.name = None

    # Creates a new User Type. A default User Type is automatically created along with your org, and you may add another 9 User Types for a maximum of 10.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user
            """)

        body = user_type
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
            result = UserType(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Updates an existing User Type
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user/{typeId}
            """)

        body = user_type
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
            result = UserType(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Fetches a User Type by ID. The special identifier &#x60;default&#x60; may be used to fetch the default User Type.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user/{typeId}
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
            result = UserType(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Deletes a User Type permanently. This operation is not permitted for the default type, nor for any User Type that has existing users
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user/{typeId}
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

    # Fetches all User Types in your org
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user
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
            result.append(UserType(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Replace an existing User Type
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/meta/types/user/{typeId}
            """)

        body = user_type
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
            result = UserType(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation
