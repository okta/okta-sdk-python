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
from okta.models.feature\
    import Feature
from okta.utils import format_url
from okta.api_client import APIClient


class FeatureClient(APIClient):
    """
    A Client object for the Feature resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_features(
            self
    ):
        """
        Args:
        Returns:
            list: Collection of Feature instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/features
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Feature)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Feature(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_feature(
            self, featureId
    ):
        """
        Args:
            feature_id {str}
        Returns:
            Feature
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/features/{featureId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Feature)

        if error:
            return (None, response, error)

        try:
            result = Feature(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_feature_dependencies(
            self, featureId
    ):
        """
        Args:
            feature_id {str}
        Returns:
            list: Collection of Feature instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/features/{featureId}/dependencies
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Feature)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Feature(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_feature_dependents(
            self, featureId
    ):
        """
        Args:
            feature_id {str}
        Returns:
            list: Collection of Feature instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/features/{featureId}/dependents
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Feature)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Feature(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_feature_lifecycle(
            self, featureId, lifecycle, query_params={}
    ):
        """
        Args:
            feature_id {str}
            lifecycle {str}
            query_params {dict}: Map of query parameters for request
            [query_params.mode] {str}
        Returns:
            Feature
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/features/{featureId}/{lifecycle}
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
            .execute(request, Feature)

        if error:
            return (None, response, error)

        try:
            result = Feature(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
