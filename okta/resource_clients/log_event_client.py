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
from okta.models.log_event\
    import LogEvent
from okta.utils import format_url
from okta.api_client import APIClient


class LogEventClient(APIClient):
    """
    A Client object for the LogEvent resource.
    """

    def __init__(self):
        self._base_url = ""

    async def get_logs(
            self, query_params={}
    ):
        """
        The Okta System Log API provides read access to your or
        ganization’s system log. This API provides more functio
        nality than the Events API
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.since] {str}
            [query_params.until] {str}
            [query_params.filter] {str}
            [query_params.q] {str}
            [query_params.limit] {str}
            [query_params.sortOrder] {str}
            [query_params.after] {str}
        Returns:
            list: Collection of LogEvent instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/logs
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
            .execute(request, LogEvent)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(LogEvent(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
