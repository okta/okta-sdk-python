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

from okta.models.group_schema\
    import GroupSchema
from okta.utils import format_url
from okta.api_client import APIClient


class GroupSchemaClient(APIClient):
    """
    A Client object for the GroupSchema resource.
    """

    def __init__(self):
        self._base_url = ""

    async def get_group_schema(
            self,
            keep_empty_params=False
    ):
        """
        Fetches the group schema
        Args:
        Returns:
            GroupSchema
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/group/default
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
            .execute(request, GroupSchema)

        if error:
            return (None, response, error)

        try:
            result = GroupSchema(
                response.get_body()
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_group_schema(
            self, group_schema,
            keep_empty_params=False
    ):
        """
        Updates, adds ore removes one or more custom Group Prof
        ile properties in the schema
        Args:
            {group_schema}
        Returns:
            GroupSchema
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/meta/schemas/group/default
            """)

        if isinstance(group_schema, dict):
            body = group_schema
        else:
            body = group_schema.as_dict()
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
            .execute(request, GroupSchema)

        if error:
            return (None, response, error)

        try:
            result = GroupSchema(
                response.get_body()
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
