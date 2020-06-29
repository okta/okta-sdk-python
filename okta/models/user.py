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


class User:
    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]
            self.links = config["_links"]
            self.activated = config["activated"]
            self.created = config["created"]
            self.credentials = config["credentials"]
            self.id = config["id"]
            self.last_login = config["lastLogin"]
            self.last_updated = config["lastUpdated"]
            self.password_changed = config["passwordChanged"]
            self.profile = config["profile"]
            self.status = config["status"]
            self.status_changed = config["statusChanged"]
            self.transitioning_to_status = config["transitioningToStatus"]
            self.type = config["type"]
        else:
            self.embedded = None
            self.links = None
            self.activated = None
            self.created = None
            self.credentials = None
            self.id = None
            self.last_login = None
            self.last_updated = None
            self.password_changed = None
            self.profile = None
            self.status = None
            self.status_changed = None
            self.transitioning_to_status = None
            self.type = None

    # Creates a new user in your Okta organization with or without credentials.
    async def create_user(
            self, create_user_request, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = create_user_request
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
            result = User(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Fetches a user from your Okta organization.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}
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
            result = User(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Update a user&#x27;s profile and/or credentials using strict-update semantics.
    async def update_user(
            self, userId, user, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = user
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
            result = User(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Deletes a user permanently.  This operation can only be performed on users that have a &#x60;DEPROVISIONED&#x60; status.  **This action cannot be recovered!**
    async def deactivate_or_delete_user(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}
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

    # Lists users in your organization with pagination in most cases.  A subset of users can be returned that match a supported filter expression or search criteria.
    async def list_users(
            self, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users
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
        result = []
        for item in response.get_body():
            result.append(User(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{associatedUserId}/linkedObjects
                {primaryRelationshipName}/{primaryUserId}
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

    # Fetch a user by &#x60;id&#x60;, &#x60;login&#x60;, or &#x60;login shortname&#x60; if the short name is unambiguous.
    async def partial_update_user(
            self, userId, user, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = user
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
            result = User(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Fetches appLinks for all direct or indirect (via group membership) assigned applications.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/appLinks
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
            result.append(AppLink(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Lists all client resources for which the specified user has grants or tokens.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients
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
            result.append(OAuth2Client(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Revokes all grants for the specified user and client
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/grants
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

    # Lists all grants for a specified user and client
    async def list_grants_for_user_and_client(
            self, userId, clientId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/grants
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
        result = []
        for item in response.get_body():
            result.append(OAuth2ScopeConsentGrant(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Revokes all refresh tokens issued for the specified User and Client.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/tokens
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

    # Lists all refresh tokens issued for the specified User and Client.
    async def list_refresh_tokens_for_user_and_client(
            self, userId, clientId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/tokens
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
        result = []
        for item in response.get_body():
            result.append(OAuth2RefreshToken(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Revokes the specified refresh token.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/tokens
                {tokenId}
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

    # Gets a refresh token issued for the specified User and Client.
    async def get_refresh_token_for_user_and_client(
            self, userId, clientId, tokenId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/clients/{clientId}/tokens
                {tokenId}
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
            result = OAuth2RefreshToken(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Changes a user&#x27;s password by validating the user&#x27;s current password. This operation can only be performed on users in &#x60;STAGED&#x60;, &#x60;ACTIVE&#x60;, &#x60;PASSWORD_EXPIRED&#x60;, or &#x60;RECOVERY&#x60; status that have a valid password credential
    async def change_password(
            self, userId, change_password_request, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/credentials/change_password
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = change_password_request
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
            result = UserCredentials(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Changes a user&#x27;s recovery question &amp; answer credential by validating the user&#x27;s current password.  This operation can only be performed on users in **STAGED**, **ACTIVE** or **RECOVERY** &#x60;status&#x60; that have a valid password credential
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/credentials
                change_recovery_question
            """)

        body = user_credentials
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
            result = UserCredentials(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Generates a one-time token (OTT) that can be used to reset a user&#x27;s password
    async def forgot_password_generate_one_time_token(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/credentials/forgot_password
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
            result = ForgotPasswordResponse(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Sets a new password for a user by validating the user&#x27;s answer to their current recovery question
    async def forgot_password_set_new_password(
            self, userId, user_credentials, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/credentials/forgot_password
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = user_credentials
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
            result = ForgotPasswordResponse(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Revokes all grants for a specified user
    async def revoke_user_grants(
            self, userId
    ):
        """
            Revokes all grants for a specified user
        Args:
            user_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/grants
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

    # Lists all grants for the specified user
    async def list_user_grants(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/grants
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
        result = []
        for item in response.get_body():
            result.append(OAuth2ScopeConsentGrant(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Revokes one grant for a specified user
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/grants/{grantId}
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

    # Gets a grant for the specified user
    async def get_user_grant(
            self, userId, grantId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/grants/{grantId}
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
            result = OAuth2ScopeConsentGrant(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Fetches the groups of which the user is a member.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/groups
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
            result.append(Group(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Lists the IdPs associated with the user.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/idps
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
            result.append(IdentityProvider(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Activates a user.  This operation can only be performed on users with a &#x60;STAGED&#x60; status.  Activation of a user is an asynchronous operation. The user will have the &#x60;transitioningToStatus&#x60; property with a value of &#x60;ACTIVE&#x60; during activation to indicate that the user hasn&#x27;t completed the asynchronous operation.  The user will have a status of &#x60;ACTIVE&#x60; when the activation process is complete.
    async def activate_user(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/activate
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
            result = UserActivationToken(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Deactivates a user.  This operation can only be performed on users that do not have a &#x60;DEPROVISIONED&#x60; status.  Deactivation of a user is an asynchronous operation.  The user will have the &#x60;transitioningToStatus&#x60; property with a value of &#x60;DEPROVISIONED&#x60; during deactivation to indicate that the user hasn&#x27;t completed the asynchronous operation.  The user will have a status of &#x60;DEPROVISIONED&#x60; when the deactivation process is complete.
    async def deactivate_user(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/deactivate
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

    # This operation transitions the user to the status of &#x60;PASSWORD_EXPIRED&#x60; so that the user is required to change their password at their next login.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle
                expire_password?tempPassword=false
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
            result = User(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # This operation transitions the user to the status of &#x60;PASSWORD_EXPIRED&#x60; and the user&#x27;s password is reset to a temporary password that is returned.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle
                expire_password?tempPassword=true
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
            result = TempPassword(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Reactivates a user.  This operation can only be performed on users with a &#x60;PROVISIONED&#x60; status.  This operation restarts the activation workflow if for some reason the user activation was not completed when using the activationToken from [Activate User](#activate-user).
    async def reactivate_user(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/reactivate
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
            result = UserActivationToken(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # This operation resets all factors for the specified user. All MFA factor enrollments returned to the unenrolled state. The user&#x27;s status remains ACTIVE. This link is present only if the user is currently enrolled in one or more MFA factors.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/reset_factors
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

    # Generates a one-time token (OTT) that can be used to reset a user&#x27;s password.  The OTT link can be automatically emailed to the user or returned to the API caller and distributed using a custom flow.
    async def reset_password(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/reset_password
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
            result = ResetPasswordToken(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Suspends a user.  This operation can only be performed on users with an &#x60;ACTIVE&#x60; status.  The user will have a status of &#x60;SUSPENDED&#x60; when the process is complete.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/suspend
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

    # Unlocks a user with a &#x60;LOCKED_OUT&#x60; status and returns them to &#x60;ACTIVE&#x60; status.  Users will be able to login with their current password.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/unlock
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

    # Unsuspends a user and returns them to the &#x60;ACTIVE&#x60; state.  This operation can only be performed on users that have a &#x60;SUSPENDED&#x60; status.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/lifecycle/unsuspend
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

    # Delete linked objects for a user, relationshipName can be ONLY a primary relationship name
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/linkedObjects
                {relationshipName}
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

    # Get linked objects for a user, relationshipName can be a primary or associated relationship name
    async def get_linked_objects_for_user(
            self, userId, relationshipName, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/linkedObjects
                {relationshipName}
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
        result = []
        for item in response.get_body():
            result.append(ResponseLinks(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Lists all roles assigned to a user.
    async def list_assigned_roles_for_user(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles
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
        result = []
        for item in response.get_body():
            result.append(Role(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    # Assigns a role to a user.
    async def assign_role_to_user(
            self, userId, assign_role_request, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

        body = assign_role_request
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
            result = Role(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Unassigns a role from a user.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}
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

    # Lists all App targets for an &#x60;APP_ADMIN&#x60; Role assigned to a User. This methods return list may include full Applications or Instances. The response for an instance will have an &#x60;ID&#x60; value, while Application will not have an ID.
    async def list_app_targets_for_application_admin_role_for_user(
            self, userId, roleId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                catalog/apps
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
        result = []
        for item in response.get_body():
            result.append(CatalogApplication(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def add_all_apps_as_target_to_role(
            self, userId, roleId
    ):
        """
            Success
        Args:
            user_id {str}
            role_id {str}
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                catalog/apps
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

    
    async def remove_app_target_from_application_admin_role_for_user(
            self, userId, roleId, appName
    ):
        """
            Success
        Args:
            user_id {str}
            role_id {str}
            app_name {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                catalog/apps/{appName}
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

    
    async def add_application_target_to_admin_role_for_user(
            self, userId, roleId, appName
    ):
        """
            Success
        Args:
            user_id {str}
            role_id {str}
            app_name {str}
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                catalog/apps/{appName}
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

    # Remove App Instance Target to App Administrator Role given to a User
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                catalog/apps/{appName}/{applicationId}
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

    # Add App Instance Target to App Administrator Role given to a User
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                catalog/apps/{appName}/{applicationId}
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

    
    async def list_group_targets_for_role(
            self, userId, roleId, query_params
    ):
        """
            Success
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                groups
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
        result = []
        for item in response.get_body():
            result.append(Group(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def remove_group_target_from_role(
            self, userId, roleId, groupId
    ):
        """
            Success
        Args:
            user_id {str}
            role_id {str}
            group_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                groups/{groupId}
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

    
    async def add_group_target_to_role(
            self, userId, roleId, groupId
    ):
        """
            Success
        Args:
            user_id {str}
            role_id {str}
            group_id {str}
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/roles/{roleId}/targets
                groups/{groupId}
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

    # Removes all active identity provider sessions. This forces the user to authenticate on the next operation. Optionally revokes OpenID Connect and OAuth refresh and access tokens issued to the user.
    async def clear_user_sessions(
            self, userId, query_params
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/sessions
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
