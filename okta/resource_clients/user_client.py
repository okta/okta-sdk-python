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
from okta.models.user\
    import User
from okta.models.app_link\
    import AppLink
from okta.models.o_auth_2_client\
    import OAuth2Client
from okta.models.o_auth_2_scope_consent_grant\
    import OAuth2ScopeConsentGrant
from okta.models.o_auth_2_refresh_token\
    import OAuth2RefreshToken
from okta.models.user_credentials\
    import UserCredentials
from okta.models.forgot_password_response\
    import ForgotPasswordResponse
from okta.models.group\
    import Group
from okta.models.identity_provider\
    import IdentityProvider
from okta.models.user_activation_token\
    import UserActivationToken
from okta.models.temp_password\
    import TempPassword
from okta.models.reset_password_token\
    import ResetPasswordToken
from okta.models.response_links\
    import ResponseLinks
from okta.models.role\
    import Role
from okta.models.catalog_application\
    import CatalogApplication
from okta.utils import format_url
from okta.api_client import APIClient


class UserClient(APIClient):
    """
    A Client object for the User resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_users(
            self, query_params={}
    ):
        """
        Lists users in your organization with pagination in mos
        t cases.  A subset of users can be returned that match
        a supported filter expression or search criteria.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
            [query_params.filter] {str}
            [query_params.search] {str}
            [query_params.sortBy] {str}
            [query_params.sortOrder] {str}
        Returns:
            list: Collection of User instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users
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
            .execute(request, User)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(User(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_user(
            self, create_user_request, query_params={}
    ):
        """
        Creates a new user in your Okta organization with or wi
        thout credentials.
        Args:
            {create_user_request}
            query_params {dict}: Map of query parameters for request
            [query_params.activate] {str}
            [query_params.provider] {str}
            [query_params.nextLogin] {str}
        Returns:
            User
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(create_user_request, dict):
            body = create_user_request
        else:
            body = create_user_request.as_dict()
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
            .execute(request, User)

        if error:
            return (None, response, error)

        try:
            result = User(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def set_linked_object_for_user(
            self, associatedUserId, primaryRelationshipName, primaryUserId
    ):
        """
        Method for
        /api/v1/users/{associatedUserId}/linkedObjects/{primary
        RelationshipName}/{primaryUserId}
        Args:
            associated_user_id {str}
            primary_relationship_name {str}
            primary_user_id {str}
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{associatedUserId}/linkedObjects
                /{primaryRelationshipName}/{primaryUserId}
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

    async def deactivate_or_delete_user(
            self, userId, query_params={}
    ):
        """
        Deletes a user permanently.  This operation can only be
        performed on users that have a `DEPROVISIONED` status.
        **This action cannot be recovered!**
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.sendEmail] {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}
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
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_user(
            self, userId
    ):
        """
        Fetches a user from your Okta organization.
        Args:
            user_id {str}
        Returns:
            User
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, User)

        if error:
            return (None, response, error)

        try:
            result = User(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def partial_update_user(
            self, userId, user, query_params={}
    ):
        """
        Fetch a user by `id`, `login`, or `login shortname` if
        the short name is unambiguous.
        Args:
            user_id {str}
            {user}
            query_params {dict}: Map of query parameters for request
            [query_params.strict] {str}
        Returns:
            User
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(user, dict):
            body = user
        else:
            body = user.as_dict()
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
            .execute(request, User)

        if error:
            return (None, response, error)

        try:
            result = User(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_user(
            self, userId, user, query_params={}
    ):
        """
        Update a user's profile and/or credentials using strict
        -update semantics.
        Args:
            user_id {str}
            {user}
            query_params {dict}: Map of query parameters for request
            [query_params.strict] {str}
        Returns:
            User
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(user, dict):
            body = user
        else:
            body = user.as_dict()
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
            .execute(request, User)

        if error:
            return (None, response, error)

        try:
            result = User(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_app_links(
            self, userId
    ):
        """
        Fetches appLinks for all direct or indirect (via group
        membership) assigned applications.
        Args:
            user_id {str}
        Returns:
            list: Collection of AppLink instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/appLinks
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AppLink)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(AppLink(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_user_clients(
            self, userId
    ):
        """
        Lists all client resources for which the specified user
        has grants or tokens.
        Args:
            user_id {str}
        Returns:
            list: Collection of OAuth2Client instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OAuth2Client)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(OAuth2Client(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def revoke_grants_for_user_and_client(
            self, userId, clientId
    ):
        """
        Revokes all grants for the specified user and client
        Args:
            user_id {str}
            client_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/grants
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

    async def list_grants_for_user_and_client(
            self, userId, clientId, query_params={}
    ):
        """
        Lists all grants for a specified user and client
        Args:
            user_id {str}
            client_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of OAuth2ScopeConsentGrant instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/grants
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
            .execute(request, OAuth2ScopeConsentGrant)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(OAuth2ScopeConsentGrant(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def revoke_tokens_for_user_and_client(
            self, userId, clientId
    ):
        """
        Revokes all refresh tokens issued for the specified Use
        r and Client.
        Args:
            user_id {str}
            client_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/tokens
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

    async def list_refresh_tokens_for_user_and_client(
            self, userId, clientId, query_params={}
    ):
        """
        Lists all refresh tokens issued for the specified User
        and Client.
        Args:
            user_id {str}
            client_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of OAuth2RefreshToken instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/tokens
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
            .execute(request, OAuth2RefreshToken)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(OAuth2RefreshToken(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def revoke_token_for_user_and_client(
            self, userId, clientId, tokenId
    ):
        """
        Revokes the specified refresh token.
        Args:
            user_id {str}
            client_id {str}
            token_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/tokens
                /{tokenId}
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

    async def get_refresh_token_for_user_and_client(
            self, userId, clientId, tokenId, query_params={}
    ):
        """
        Gets a refresh token issued for the specified User and
        Client.
        Args:
            user_id {str}
            client_id {str}
            token_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
            [query_params.limit] {str}
            [query_params.after] {str}
        Returns:
            OAuth2RefreshToken
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/tokens
                /{tokenId}
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
            .execute(request, OAuth2RefreshToken)

        if error:
            return (None, response, error)

        try:
            result = OAuth2RefreshToken(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def change_password(
            self, userId, change_password_request, query_params={}
    ):
        """
        Changes a user's password by validating the user's curr
        ent password. This operation can only be performed on u
        sers in `STAGED`, `ACTIVE`, `PASSWORD_EXPIRED`, or `REC
        OVERY` status that have a valid password credential
        Args:
            user_id {str}
            {change_password_request}
            query_params {dict}: Map of query parameters for request
            [query_params.strict] {str}
        Returns:
            UserCredentials
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/credentials/change_password
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(change_password_request, dict):
            body = change_password_request
        else:
            body = change_password_request.as_dict()
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
            .execute(request, UserCredentials)

        if error:
            return (None, response, error)

        try:
            result = UserCredentials(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def change_recovery_question(
            self, userId, user_credentials
    ):
        """
        Changes a user's recovery question & answer credential
        by validating the user's current password.  This operat
        ion can only be performed on users in **STAGED**, **ACT
        IVE** or **RECOVERY** `status` that have a valid passwo
        rd credential
        Args:
            user_id {str}
            {user_credentials}
        Returns:
            UserCredentials
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/credentials
                /change_recovery_question
            """)

        if isinstance(user_credentials, dict):
            body = user_credentials
        else:
            body = user_credentials.as_dict()
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
            .execute(request, UserCredentials)

        if error:
            return (None, response, error)

        try:
            result = UserCredentials(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def forgot_password_generate_one_time_token(
            self, userId, query_params={}
    ):
        """
        Generates a one-time token (OTT) that can be used to re
        set a user's password
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.sendEmail] {str}
        Returns:
            ForgotPasswordResponse
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/credentials/forgot_password
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
            .execute(request, ForgotPasswordResponse)

        if error:
            return (None, response, error)

        try:
            result = ForgotPasswordResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def forgot_password_set_new_password(
            self, userId, user_credentials, query_params={}
    ):
        """
        Sets a new password for a user by validating the user's
        answer to their current recovery question
        Args:
            user_id {str}
            {user_credentials}
            query_params {dict}: Map of query parameters for request
            [query_params.sendEmail] {str}
        Returns:
            ForgotPasswordResponse
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/credentials/forgot_password
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(user_credentials, dict):
            body = user_credentials
        else:
            body = user_credentials.as_dict()
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
            .execute(request, ForgotPasswordResponse)

        if error:
            return (None, response, error)

        try:
            result = ForgotPasswordResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def revoke_user_grants(
            self, userId
    ):
        """
        Revokes all grants for a specified user
        Args:
            user_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/grants
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

    async def list_user_grants(
            self, userId, query_params={}
    ):
        """
        Lists all grants for the specified user
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.scopeId] {str}
            [query_params.expand] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of OAuth2ScopeConsentGrant instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/grants
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
            .execute(request, OAuth2ScopeConsentGrant)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(OAuth2ScopeConsentGrant(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def revoke_user_grant(
            self, userId, grantId
    ):
        """
        Revokes one grant for a specified user
        Args:
            user_id {str}
            grant_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/grants/{grantId}
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

    async def get_user_grant(
            self, userId, grantId, query_params={}
    ):
        """
        Gets a grant for the specified user
        Args:
            user_id {str}
            grant_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            OAuth2ScopeConsentGrant
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/grants/{grantId}
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
            .execute(request, OAuth2ScopeConsentGrant)

        if error:
            return (None, response, error)

        try:
            result = OAuth2ScopeConsentGrant(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_user_groups(
            self, userId
    ):
        """
        Fetches the groups of which the user is a member.
        Args:
            user_id {str}
        Returns:
            list: Collection of Group instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/groups
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Group)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Group(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_user_identity_providers(
            self, userId
    ):
        """
        Lists the IdPs associated with the user.
        Args:
            user_id {str}
        Returns:
            list: Collection of IdentityProvider instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/idps
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, IdentityProvider)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(IdentityProvider(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_user(
            self, userId, query_params={}
    ):
        """
        Activates a user.  This operation can only be performed
        on users with a `STAGED` status.  Activation of a user
        is an asynchronous operation. The user will have the `
        transitioningToStatus` property with a value of `ACTIVE
        ` during activation to indicate that the user hasn't co
        mpleted the asynchronous operation.  The user will have
        a status of `ACTIVE` when the activation process is co
        mplete.
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.sendEmail] {str}
        Returns:
            UserActivationToken
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/activate
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
            .execute(request, UserActivationToken)

        if error:
            return (None, response, error)

        try:
            result = UserActivationToken(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def deactivate_user(
            self, userId, query_params={}
    ):
        """
        Deactivates a user.  This operation can only be perform
        ed on users that do not have a `DEPROVISIONED` status.
        Deactivation of a user is an asynchronous operation.
        The user will have the `transitioningToStatus` property
        with a value of `DEPROVISIONED` during deactivation to
        indicate that the user hasn't completed the asynchrono
        us operation.  The user will have a status of `DEPROVIS
        IONED` when the deactivation process is complete.
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.sendEmail] {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/deactivate
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
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def expire_password(
            self, userId
    ):
        """
        This operation transitions the user to the status of `P
        ASSWORD_EXPIRED` so that the user is required to change
        their password at their next login.
        Args:
            user_id {str}
        Returns:
            User
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle
                /expire_password?tempPassword=false
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, User)

        if error:
            return (None, response, error)

        try:
            result = User(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def expire_password_and_get_temporary_password(
            self, userId
    ):
        """
        This operation transitions the user to the status of `P
        ASSWORD_EXPIRED` and the user's password is reset to a
        temporary password that is returned.
        Args:
            user_id {str}
        Returns:
            TempPassword
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle
                /expire_password?tempPassword=true
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, TempPassword)

        if error:
            return (None, response, error)

        try:
            result = TempPassword(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def reactivate_user(
            self, userId, query_params={}
    ):
        """
        Reactivates a user.  This operation can only be perform
        ed on users with a `PROVISIONED` status.  This operatio
        n restarts the activation workflow if for some reason t
        he user activation was not completed when using the act
        ivationToken from [Activate User](#activate-user).
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.sendEmail] {str}
        Returns:
            UserActivationToken
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/reactivate
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
            .execute(request, UserActivationToken)

        if error:
            return (None, response, error)

        try:
            result = UserActivationToken(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def reset_factors(
            self, userId
    ):
        """
        This operation resets all factors for the specified use
        r. All MFA factor enrollments returned to the unenrolle
        d state. The user's status remains ACTIVE. This link is
        present only if the user is currently enrolled in one
        or more MFA factors.
        Args:
            user_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/reset_factors
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

    async def reset_password(
            self, userId, query_params={}
    ):
        """
        Generates a one-time token (OTT) that can be used to re
        set a user's password.  The OTT link can be automatical
        ly emailed to the user or returned to the API caller an
        d distributed using a custom flow.
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.sendEmail] {str}
        Returns:
            ResetPasswordToken
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/reset_password
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
            .execute(request, ResetPasswordToken)

        if error:
            return (None, response, error)

        try:
            result = ResetPasswordToken(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def suspend_user(
            self, userId
    ):
        """
        Suspends a user.  This operation can only be performed
        on users with an `ACTIVE` status.  The user will have a
        status of `SUSPENDED` when the process is complete.
        Args:
            user_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/suspend
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

    async def unlock_user(
            self, userId
    ):
        """
        Unlocks a user with a `LOCKED_OUT` status and returns t
        hem to `ACTIVE` status.  Users will be able to login wi
        th their current password.
        Args:
            user_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/unlock
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

    async def unsuspend_user(
            self, userId
    ):
        """
        Unsuspends a user and returns them to the `ACTIVE` stat
        e.  This operation can only be performed on users that
        have a `SUSPENDED` status.
        Args:
            user_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/unsuspend
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

    async def remove_linked_object_for_user(
            self, userId, relationshipName
    ):
        """
        Delete linked objects for a user, relationshipName can
        be ONLY a primary relationship name
        Args:
            user_id {str}
            relationship_name {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/linkedObjects
                /{relationshipName}
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

    async def get_linked_objects_for_user(
            self, userId, relationshipName, query_params={}
    ):
        """
        Get linked objects for a user, relationshipName can be
        a primary or associated relationship name
        Args:
            user_id {str}
            relationship_name {str}
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of ResponseLinks instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/linkedObjects
                /{relationshipName}
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
            .execute(request, ResponseLinks)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(ResponseLinks(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_assigned_roles_for_user(
            self, userId, query_params={}
    ):
        """
        Lists all roles assigned to a user.
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            list: Collection of Role instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles
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
            .execute(request, Role)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Role(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def assign_role_to_user(
            self, userId, assign_role_request, query_params={}
    ):
        """
        Assigns a role to a user.
        Args:
            user_id {str}
            {assign_role_request}
            query_params {dict}: Map of query parameters for request
            [query_params.disableNotifications] {str}
        Returns:
            Role
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(assign_role_request, dict):
            body = assign_role_request
        else:
            body = assign_role_request.as_dict()
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
            .execute(request, Role)

        if error:
            return (None, response, error)

        try:
            result = Role(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def remove_role_from_user(
            self, userId, roleId
    ):
        """
        Unassigns a role from a user.
        Args:
            user_id {str}
            role_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}
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

    async def list_app_targets_for_application_admin_role_for_user(
            self, userId, roleId, query_params={}
    ):
        """
        Lists all App targets for an `APP_ADMIN` Role assigned
        to a User. This methods return list may include full Ap
        plications or Instances. The response for an instance w
        ill have an `ID` value, while Application will not have
        an ID.
        Args:
            user_id {str}
            role_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of CatalogApplication instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /catalog/apps
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
            .execute(request, CatalogApplication)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(CatalogApplication(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def add_all_apps_as_target_to_role(
            self, userId, roleId
    ):
        """
        Args:
            user_id {str}
            role_id {str}
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /catalog/apps
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

    async def remove_app_target_from_application_admin_role_for_user(
            self, userId, roleId, appName
    ):
        """
        Args:
            user_id {str}
            role_id {str}
            app_name {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /catalog/apps/{appName}
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

    async def add_application_target_to_admin_role_for_user(
            self, userId, roleId, appName
    ):
        """
        Args:
            user_id {str}
            role_id {str}
            app_name {str}
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /catalog/apps/{appName}
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

    async def remove_application_target_from_administrator_role_for_user(
            self, userId, roleId, appName, applicationId
    ):
        """
        Remove App Instance Target to App Administrator Role gi
        ven to a User
        Args:
            user_id {str}
            role_id {str}
            app_name {str}
            application_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /catalog/apps/{appName}/{applicationId}
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

    async def add_application_target_to_app_admin_role_for_user(
            self, userId, roleId, appName, applicationId
    ):
        """
        Add App Instance Target to App Administrator Role given
        to a User
        Args:
            user_id {str}
            role_id {str}
            app_name {str}
            application_id {str}
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /catalog/apps/{appName}/{applicationId}
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

    async def list_group_targets_for_role(
            self, userId, roleId, query_params={}
    ):
        """
        Args:
            user_id {str}
            role_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of Group instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /groups
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
            .execute(request, Group)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Group(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def remove_group_target_from_role(
            self, userId, roleId, groupId
    ):
        """
        Args:
            user_id {str}
            role_id {str}
            group_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /groups/{groupId}
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

    async def add_group_target_to_role(
            self, userId, roleId, groupId
    ):
        """
        Args:
            user_id {str}
            role_id {str}
            group_id {str}
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                /groups/{groupId}
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

    async def clear_user_sessions(
            self, userId, query_params={}
    ):
        """
        Removes all active identity provider sessions. This for
        ces the user to authenticate on the next operation. Opt
        ionally revokes OpenID Connect and OAuth refresh and ac
        cess tokens issued to the user.
        Args:
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.oauthTokens] {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/sessions
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
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)
