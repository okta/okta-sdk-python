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

from okta.models.threat_insight_configuration\
    import ThreatInsightConfiguration
from okta.utils import format_url
from okta.api_client import APIClient


class ThreatInsightClient(APIClient):
    """
    A Client object for the ThreatInsight resource.
    """

    def __init__(self):
        self._base_url = ""

    async def get_current_configuration(
            self,
            keep_empty_params=False
    ):
        """
        Gets current ThreatInsight configuration
        Args:
        Returns:
            ThreatInsightConfiguration
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/threats/configuration
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ThreatInsightConfiguration)

        if error:
            return (None, response, error)

        try:
            result = ThreatInsightConfiguration(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_configuration(
            self, threat_insight_configuration,
            keep_empty_params=False
    ):
        """
        Updates ThreatInsight configuration
        Args:
            {threat_insight_configuration}
        Returns:
            ThreatInsightConfiguration
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/threats/configuration
            """)

        if isinstance(threat_insight_configuration, dict):
            body = threat_insight_configuration
        else:
            body = threat_insight_configuration.as_dict()
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
            .execute(request, ThreatInsightConfiguration)

        if error:
            return (None, response, error)

        try:
            result = ThreatInsightConfiguration(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
