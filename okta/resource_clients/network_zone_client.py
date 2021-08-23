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
from okta.models.network_zone\
    import NetworkZone
from okta.utils import format_url
from okta.api_client import APIClient


class NetworkZoneClient(APIClient):
    """
    A Client object for the NetworkZone resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_network_zones(
            self, query_params={},
            keep_empty_params=False
    ):
        """
        Enumerates network zones added to your organization wit
        h pagination. A subset of zones can be returned that ma
        tch a supported filter expression or query.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
            [query_params.filter] {str}
        Returns:
            list: Collection of NetworkZone instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/zones
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
            .execute(request, NetworkZone)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(NetworkZone(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_network_zone(
            self, network_zone,
            keep_empty_params=False
    ):
        """
        Adds a new network zone to your Okta organization.
        Args:
            {network_zone}
        Returns:
            NetworkZone
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/zones
            """)

        if isinstance(network_zone, dict):
            body = network_zone
        else:
            body = network_zone.as_dict()
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
            .execute(request, NetworkZone)

        if error:
            return (None, response, error)

        try:
            result = NetworkZone(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_network_zone(
            self, zoneId,
            keep_empty_params=False
    ):
        """
        Removes network zone.
        Args:
            zone_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/zones/{zoneId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_network_zone(
            self, zoneId,
            keep_empty_params=False
    ):
        """
        Fetches a network zone from your Okta organization by `
        id`.
        Args:
            zone_id {str}
        Returns:
            NetworkZone
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/zones/{zoneId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, NetworkZone)

        if error:
            return (None, response, error)

        try:
            result = NetworkZone(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_network_zone(
            self, zoneId, network_zone,
            keep_empty_params=False
    ):
        """
        Updates a network zone in your organization.
        Args:
            zone_id {str}
            {network_zone}
        Returns:
            NetworkZone
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/zones/{zoneId}
            """)

        if isinstance(network_zone, dict):
            body = network_zone
        else:
            body = network_zone.as_dict()
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
            .execute(request, NetworkZone)

        if error:
            return (None, response, error)

        try:
            result = NetworkZone(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_network_zone(
            self, zoneId,
            keep_empty_params=False
    ):
        """
        Activate Network Zone
        Args:
            zone_id {str}
        Returns:
            NetworkZone
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/zones/{zoneId}/lifecycle/activate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, NetworkZone)

        if error:
            return (None, response, error)

        try:
            result = NetworkZone(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def deactivate_network_zone(
            self, zoneId,
            keep_empty_params=False
    ):
        """
        Deactivates a network zone.
        Args:
            zone_id {str}
        Returns:
            NetworkZone
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/zones/{zoneId}/lifecycle/deactivate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, NetworkZone)

        if error:
            return (None, response, error)

        try:
            result = NetworkZone(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
