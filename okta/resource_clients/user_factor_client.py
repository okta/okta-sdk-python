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
from okta.models.user_factor\
    import UserFactor
from okta.models.security_question\
    import SecurityQuestion
from okta.models.verify_user_factor_response\
    import VerifyUserFactorResponse
from okta.utils import format_url
from okta.api_client import APIClient
from okta.constants import find_factor_model


class UserFactorClient(APIClient):
    """
    A Client object for the UserFactor resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_factors(
            self, userId
    ):
        """
        Enumerates all the enrolled factors for the specified u
        ser
        Args:
            user_id {str}
        Returns:
            list: Collection of UserFactor instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserFactor)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(
                    find_factor_model(item["factorType"])(
                        self.form_response_body(item)
                        )
                    )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def enroll_factor(
            self, userId, user_factor, query_params={}
    ):
        """
        Enrolls a user with a supported factor.
        Args:
            user_id {str}
            {user_factor}
            query_params {dict}: Map of query parameters for request
            [query_params.updatePhone] {str}
            [query_params.templateId] {str}
            [query_params.tokenLifetimeSeconds] {str}
            [query_params.activate] {str}
        Returns:
            UserFactor
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(user_factor, dict):
            body = user_factor
        else:
            body = user_factor.as_dict()
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
            .execute(request, UserFactor)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_factor_model(body["factorType"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_supported_factors(
            self, userId
    ):
        """
        Enumerates all the supported factors that can be enroll
        ed for the specified user
        Args:
            user_id {str}
        Returns:
            list: Collection of UserFactor instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors/catalog
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserFactor)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(
                    find_factor_model(item["factorType"])(
                        self.form_response_body(item)
                        )
                    )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_supported_security_questions(
            self, userId
    ):
        """
        Enumerates all available security questions for a user'
        s `question` factor
        Args:
            user_id {str}
        Returns:
            list: Collection of SecurityQuestion instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors/questions
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, SecurityQuestion)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(SecurityQuestion(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_factor(
            self, userId, factorId
    ):
        """
        Unenrolls an existing factor for the specified user, al
        lowing the user to enroll a new factor.
        Args:
            user_id {str}
            factor_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors/{factorId}
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

    async def get_factor(
            self, userId, factorId
    ):
        """
        Fetches a factor for the specified user
        Args:
            user_id {str}
            factor_id {str}
        Returns:
            UserFactor
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors/{factorId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, UserFactor)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_factor_model(body["factorType"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_factor(
            self, userId, factorId, activate_factor_request
    ):
        """
        The `sms` and `token:software:totp` factor types requir
        e activation to complete the enrollment process.
        Args:
            user_id {str}
            factor_id {str}
            {activate_factor_request}
        Returns:
            UserFactor
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors/{factorId}/lifecycle
                /activate
            """)

        if isinstance(activate_factor_request, dict):
            body = activate_factor_request
        else:
            body = activate_factor_request.as_dict()
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
            .execute(request, UserFactor)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_factor_model(body["factorType"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_factor_transaction_status(
            self, userId, factorId, transactionId
    ):
        """
        Polls factors verification transaction for status.
        Args:
            user_id {str}
            factor_id {str}
            transaction_id {str}
        Returns:
            VerifyUserFactorResponse
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors/{factorId}
                /transactions/{transactionId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, VerifyUserFactorResponse)

        if error:
            return (None, response, error)

        try:
            result = VerifyUserFactorResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def verify_factor(
            self, userId, factorId, verify_factor_request, query_params={}
    ):
        """
        Verifies an OTP for a `token` or `token:hardware` facto
        r
        Args:
            user_id {str}
            factor_id {str}
            {verify_factor_request}
            query_params {dict}: Map of query parameters for request
            [query_params.templateId] {str}
            [query_params.tokenLifetimeSeconds] {str}
        Returns:
            VerifyUserFactorResponse
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/factors/{factorId}/verify
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(verify_factor_request, dict):
            body = verify_factor_request
        else:
            body = verify_factor_request.as_dict()
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
            .execute(request, VerifyUserFactorResponse)

        if error:
            return (None, response, error)

        try:
            result = VerifyUserFactorResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
