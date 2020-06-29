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


class AppUser:
    def __init__(self):
        pass

    # Updates a user&#x27;s profile for an application
    async def update_application_user(
            self, appId, userId, app_user
    ):
        """
            Updates a user's profile for an application
        Args:
            app_id {str}
            user_id {str}
            {app_user}
        Returns:
            AppUser
        """
        http_method = "post".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/users/{userId}
            """)

        body = app_user
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
            result = AppUser(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Removes an assignment for a user from an application.
    async def delete_application_user(
            self, appId, userId, query_params
    ):
        """
            Removes an assignment for a user from an application.
        Args:
            app_id {str}
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.sendEmail] {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/users/{userId}
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
        return (response, None)


# End of File Generation
