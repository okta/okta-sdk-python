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
from okta.utils import format_url


class FeatureClient():
    """
    A Client object for the Feature resource.
    """
    def __init__(self):
        self._base_url = ""

    async def list_features(
            self
    ):
        """
            Success
        Args:
        Returns:
            list: Collection of Feature instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/features
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
                result.append(Feature(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def get_feature(
            self, featureId
    ):
        """
            Success
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
            result = Feature(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_feature_dependencies(
            self, featureId
    ):
        """
            Success
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
                result.append(Feature(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_feature_dependents(
            self, featureId
    ):
        """
            Success
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
                result.append(Feature(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def update_feature_lifecycle(
            self, featureId, lifecycle, query_params
    ):
        """
            Success
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
            result = Feature(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation
