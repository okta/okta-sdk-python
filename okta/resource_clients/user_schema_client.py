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

from okta.models.user_schema\
    import UserSchema
from okta.utils import format_url
from okta.api_client import APIClient


class UserSchemaClient(APIClient):
    """
    A Client object for the UserSchema resource.
    """

    def __init__(self):
        self._base_url = ""

    async def get_application_user_schema(
            self, appInstanceId,
            keep_empty_params=True
    ):
        """
        Fetches the Schema for an App User
        Args:
            app_instance_id {str}
        Returns:
            UserSchema
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/apps/{appInstanceId}/default
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserSchema)

        if error:
            return (None, response, error)

        try:
            result = UserSchema(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_application_user_profile(
            self, appInstanceId, user_schema,
            keep_empty_params=True
    ):
        """
        Partial updates on the User Profile properties of the A
        pplication User Schema.
        Args:
            app_instance_id {str}
            {user_schema}
        Returns:
            UserSchema
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/apps/{appInstanceId}/default
            """)

        if isinstance(user_schema, dict):
            body = user_schema
        else:
            body = user_schema.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserSchema)

        if error:
            return (None, response, error)

        try:
            result = UserSchema(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_user_schema(
            self, schemaId,
            keep_empty_params=True
    ):
        """
        Fetches the schema for a Schema Id.
        Args:
            schema_id {str}
        Returns:
            UserSchema
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/user/{schemaId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserSchema)

        if error:
            return (None, response, error)

        try:
            result = UserSchema(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_user_profile(
            self, schemaId, user_schema,
            keep_empty_params=True
    ):
        """
        Partial updates on the User Profile properties of the u
        ser schema.
        Args:
            schema_id {str}
            {user_schema}
        Returns:
            UserSchema
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/user/{schemaId}
            """)

        if isinstance(user_schema, dict):
            body = user_schema
        else:
            body = user_schema.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserSchema)

        if error:
            return (None, response, error)

        try:
            result = UserSchema(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
