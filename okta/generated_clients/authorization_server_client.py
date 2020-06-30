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
from okta.models.authorization_server\
    import AuthorizationServer
from okta.models.o_auth_2_claim\
    import OAuth2Claim
from okta.models.o_auth_2_client\
    import OAuth2Client
from okta.models.o_auth_2_refresh_token\
    import OAuth2RefreshToken
from okta.models.json_web_key\
    import JsonWebKey
from okta.models.policy\
    import Policy
from okta.models.o_auth_2_scope\
    import OAuth2Scope


class AuthorizationServerClient():
    """
    A Client object for the AuthorizationServer resource.
    """
    def __init__(self):
        self._base_url = ""

    async def list_authorization_servers(
            self, query_params
    ):
        """
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.limit] {str}
            [query_params.after] {str}
        Returns:
            list: Collection of AuthorizationServer instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers
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
                result.append(AuthorizationServer(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def create_authorization_server(
            self, authorization_server
    ):
        """
        Args:
            {authorization_server}
        Returns:
            AuthorizationServer
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers
            """)

        body = authorization_server.as_dict()
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
            result = AuthorizationServer(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def delete_authorization_server(
            self, authServerId
    ):
        """
        Args:
            auth_server_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
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

    async def get_authorization_server(
            self, authServerId
    ):
        """
        Args:
            auth_server_id {str}
        Returns:
            AuthorizationServer
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
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
            result = AuthorizationServer(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def update_authorization_server(
            self, authServerId, authorization_server
    ):
        """
        Args:
            auth_server_id {str}
            {authorization_server}
        Returns:
            AuthorizationServer
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
            """)

        body = authorization_server.as_dict()
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
            result = AuthorizationServer(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_o_auth_2_claims(
            self, authServerId
    ):
        """
        Args:
            auth_server_id {str}
        Returns:
            list: Collection of OAuth2Claim instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/claims
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
                result.append(OAuth2Claim(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def create_o_auth_2_claim(
            self, authServerId, o_auth_2_claim
    ):
        """
        Args:
            auth_server_id {str}
            {o_auth_2_claim}
        Returns:
            OAuth2Claim
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/claims
            """)

        body = o_auth_2_claim.as_dict()
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
            result = OAuth2Claim(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def delete_o_auth_2_claim(
            self, authServerId, claimId
    ):
        """
        Args:
            auth_server_id {str}
            claim_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/claims
                {claimId}
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

    async def get_o_auth_2_claim(
            self, authServerId, claimId
    ):
        """
        Args:
            auth_server_id {str}
            claim_id {str}
        Returns:
            OAuth2Claim
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/claims
                {claimId}
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
            result = OAuth2Claim(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def update_o_auth_2_claim(
            self, authServerId, claimId, o_auth_2_claim
    ):
        """
        Args:
            auth_server_id {str}
            claim_id {str}
            {o_auth_2_claim}
        Returns:
            OAuth2Claim
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/claims
                {claimId}
            """)

        body = o_auth_2_claim.as_dict()
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
            result = OAuth2Claim(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_o_auth_2_clients_for_authorization_server(
            self, authServerId
    ):
        """
        Args:
            auth_server_id {str}
        Returns:
            list: Collection of OAuth2Client instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/clients
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

    async def revoke_refresh_tokens_for_authorization_server_and_client(
            self, authServerId, clientId
    ):
        """
        Args:
            auth_server_id {str}
            client_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/clients
                {clientId}/tokens
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

    async def list_refresh_tokens_for_authorization_server_and_client(
            self, authServerId, clientId, query_params
    ):
        """
        Args:
            auth_server_id {str}
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
            /api/v1/authorizationServers/{authServerId}/clients
                {clientId}/tokens
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

    async def revoke_refresh_token_for_authorization_server_and_client(
            self, authServerId, clientId, tokenId
    ):
        """
        Args:
            auth_server_id {str}
            client_id {str}
            token_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/clients
                {clientId}/tokens/{tokenId}
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

    async def get_refresh_token_for_authorization_server_and_client(
            self, authServerId, clientId, tokenId, query_params
    ):
        """
        Args:
            auth_server_id {str}
            client_id {str}
            token_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            OAuth2RefreshToken
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/clients
                {clientId}/tokens/{tokenId}
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

    async def list_authorization_server_keys(
            self, authServerId
    ):
        """
        Args:
            auth_server_id {str}
        Returns:
            list: Collection of JsonWebKey instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                credentials/keys
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
                result.append(JsonWebKey(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def rotate_authorization_server_keys(
            self, authServerId, jwk_use
    ):
        """
        Args:
            auth_server_id {str}
        Returns:
            list: Collection of JsonWebKey instances.
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                credentials/lifecycle/keyRotate
            """)

        body = jwk_use.as_dict()
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
            result = []
            for item in response.get_body():
                result.append(JsonWebKey(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def activate_authorization_server(
            self, authServerId
    ):
        """
        Args:
            auth_server_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                lifecycle/activate
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

    async def deactivate_authorization_server(
            self, authServerId
    ):
        """
        Args:
            auth_server_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                lifecycle/deactivate
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

    async def list_authorization_server_policies(
            self, authServerId
    ):
        """
        Args:
            auth_server_id {str}
        Returns:
            list: Collection of Policy instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                policies
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
                result.append(Policy(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def create_authorization_server_policy(
            self, authServerId, policy
    ):
        """
        Args:
            auth_server_id {str}
            {policy}
        Returns:
            Policy
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                policies
            """)

        body = policy.as_dict()
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
            result = Policy(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def delete_authorization_server_policy(
            self, authServerId, policyId
    ):
        """
        Args:
            auth_server_id {str}
            policy_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                policies/{policyId}
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

    async def get_authorization_server_policy(
            self, authServerId, policyId
    ):
        """
        Args:
            auth_server_id {str}
            policy_id {str}
        Returns:
            Policy
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                policies/{policyId}
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
            result = Policy(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def update_authorization_server_policy(
            self, authServerId, policyId, policy
    ):
        """
        Args:
            auth_server_id {str}
            policy_id {str}
            {policy}
        Returns:
            Policy
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                policies/{policyId}
            """)

        body = policy.as_dict()
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
            result = Policy(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_o_auth_2_scopes(
            self, authServerId, query_params
    ):
        """
        Args:
            auth_server_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.filter] {str}
            [query_params.cursor] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of OAuth2Scope instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/scopes
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
                result.append(OAuth2Scope(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def create_o_auth_2_scope(
            self, authServerId, o_auth_2_scope
    ):
        """
        Args:
            auth_server_id {str}
            {o_auth_2_scope}
        Returns:
            OAuth2Scope
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/scopes
            """)

        body = o_auth_2_scope.as_dict()
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
            result = OAuth2Scope(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def delete_o_auth_2_scope(
            self, authServerId, scopeId
    ):
        """
        Args:
            auth_server_id {str}
            scope_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/scopes
                {scopeId}
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

    async def get_o_auth_2_scope(
            self, authServerId, scopeId
    ):
        """
        Args:
            auth_server_id {str}
            scope_id {str}
        Returns:
            OAuth2Scope
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/scopes
                {scopeId}
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
            result = OAuth2Scope(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def update_o_auth_2_scope(
            self, authServerId, scopeId, o_auth_2_scope
    ):
        """
        Args:
            auth_server_id {str}
            scope_id {str}
            {o_auth_2_scope}
        Returns:
            OAuth2Scope
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}/scopes
                {scopeId}
            """)

        body = o_auth_2_scope.as_dict()
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
            result = OAuth2Scope(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation
