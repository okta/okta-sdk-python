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


class Session:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.amr = config["amr"]
            self.created_at = config["createdAt"]
            self.expires_at = config["expiresAt"]
            self.id = config["id"]
            self.idp = config["idp"]
            self.last_factor_verification = config["lastFactorVerification"]
            self.last_password_verification = config["lastPasswordVerification"]
            self.login = config["login"]
            self.status = config["status"]
            self.user_id = config["userId"]
        else:
            self.links = None
            self.amr = None
            self.created_at = None
            self.expires_at = None
            self.id = None
            self.idp = None
            self.last_factor_verification = None
            self.last_password_verification = None
            self.login = None
            self.status = None
            self.user_id = None

    # Get details about a session.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/sessions/{sessionId}
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
            result = Session(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # 
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/sessions/{sessionId}
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

    # Creates a new session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID in order to delete a session via the API instead of visiting the logout URL.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/sessions
            """)

        body = create_session_request
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
            result = Session(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # 
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/sessions/{sessionId}/lifecycle/refresh
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
            result = Session(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation
