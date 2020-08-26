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

from okta.models.session\
    import Session
from okta.utils import format_url
from okta.api_client import APIClient


class SessionClient(APIClient):
    """
    A Client object for the Session resource.
    """

    def __init__(self):
        self._base_url = ""

    async def create_session(
            self, create_session_request
    ):
        """
        Creates a new session for a user with a valid session t
        oken. Use this API if, for example, you want to set the
        session cookie yourself instead of allowing Okta to se
        t it, or want to hold the session ID in order to delete
        a session via the API instead of visiting the logout U
        RL.
        Args:
            {create_session_request}
        Returns:
            Session
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/sessions
            """)

        if isinstance(create_session_request, dict):
            body = create_session_request
        else:
            body = create_session_request.as_dict()
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
            .execute(request, Session)

        if error:
            return (None, response, error)

        try:
            result = Session(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def end_session(
            self, sessionId
    ):
        """
        Method for
        /api/v1/sessions/{sessionId}
        Args:
            session_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/sessions/{sessionId}
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

    async def get_session(
            self, sessionId
    ):
        """
        Get details about a session.
        Args:
            session_id {str}
        Returns:
            Session
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/sessions/{sessionId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Session)

        if error:
            return (None, response, error)

        try:
            result = Session(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def refresh_session(
            self, sessionId
    ):
        """
        Method for
        /api/v1/sessions/{sessionId}/lifecycle/refresh
        Args:
            session_id {str}
        Returns:
            Session
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/sessions/{sessionId}/lifecycle/refresh
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Session)

        if error:
            return (None, response, error)

        try:
            result = Session(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
