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
from okta.models.profile_mapping\
    import ProfileMapping
from okta.utils import format_url
from okta.api_client import APIClient


class ProfileMappingClient(APIClient):
    """
    A Client object for the ProfileMapping resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_profile_mappings(
            self, query_params={},
            keep_empty_params=False
    ):
        """
        Enumerates Profile Mappings in your organization with p
        agination.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
            [query_params.sourceId] {str}
            [query_params.targetId] {str}
        Returns:
            list: Collection of ProfileMapping instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/mappings
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ProfileMapping)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(ProfileMapping(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_profile_mapping(
            self, mappingId,
            keep_empty_params=False
    ):
        """
        Fetches a single Profile Mapping referenced by its ID.
        Args:
            mapping_id {str}
        Returns:
            ProfileMapping
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/mappings/{mappingId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ProfileMapping)

        if error:
            return (None, response, error)

        try:
            result = ProfileMapping(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_profile_mapping(
            self, mappingId, profile_mapping,
            keep_empty_params=False
    ):
        """
        Updates an existing Profile Mapping by adding, updating
        , or removing one or many Property Mappings.
        Args:
            mapping_id {str}
            {profile_mapping}
        Returns:
            ProfileMapping
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/mappings/{mappingId}
            """)

        if isinstance(profile_mapping, dict):
            body = profile_mapping
        else:
            body = profile_mapping.as_dict()
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
            .execute(request, ProfileMapping)

        if error:
            return (None, response, error)

        try:
            result = ProfileMapping(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
