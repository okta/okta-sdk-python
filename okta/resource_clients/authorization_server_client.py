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
from okta.utils import format_url
from okta.api_client import APIClient
from okta.constants import find_policy_model


class AuthorizationServerClient(APIClient):
    """
    A Client object for the AuthorizationServer resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_authorization_servers(
            self, query_params={}
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
            .execute(request, AuthorizationServer)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(AuthorizationServer(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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

        if isinstance(authorization_server, dict):
            body = authorization_server
        else:
            body = authorization_server.as_dict()
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
            .execute(request, AuthorizationServer)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServer(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AuthorizationServer)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServer(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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

        if isinstance(authorization_server, dict):
            body = authorization_server
        else:
            body = authorization_server.as_dict()
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
            .execute(request, AuthorizationServer)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServer(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OAuth2Claim)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(OAuth2Claim(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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

        if isinstance(o_auth_2_claim, dict):
            body = o_auth_2_claim
        else:
            body = o_auth_2_claim.as_dict()
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
            .execute(request, OAuth2Claim)

        if error:
            return (None, response, error)

        try:
            result = OAuth2Claim(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /{claimId}
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
                /{claimId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OAuth2Claim)

        if error:
            return (None, response, error)

        try:
            result = OAuth2Claim(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /{claimId}
            """)

        if isinstance(o_auth_2_claim, dict):
            body = o_auth_2_claim
        else:
            body = o_auth_2_claim.as_dict()
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
            .execute(request, OAuth2Claim)

        if error:
            return (None, response, error)

        try:
            result = OAuth2Claim(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /{clientId}/tokens
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

    async def list_refresh_tokens_for_authorization_server_and_client(
            self, authServerId, clientId, query_params={}
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
                /{clientId}/tokens
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
                /{clientId}/tokens/{tokenId}
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

    async def get_refresh_token_for_authorization_server_and_client(
            self, authServerId, clientId, tokenId, query_params={}
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
                /{clientId}/tokens/{tokenId}
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
                /credentials/keys
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(JsonWebKey(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /credentials/lifecycle/keyRotate
            """)

        if isinstance(jwk_use, dict):
            body = jwk_use
        else:
            body = jwk_use.as_dict()
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
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(JsonWebKey(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /lifecycle/activate
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
                /lifecycle/deactivate
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
                /policies
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Policy)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(
                    find_policy_model(item["type"])(
                        self.form_response_body(item)
                        )
                    )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /policies
            """)

        if isinstance(policy, dict):
            body = policy
        else:
            body = policy.as_dict()
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
            .execute(request, Policy)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /policies/{policyId}
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
                /policies/{policyId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Policy)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /policies/{policyId}
            """)

        if isinstance(policy, dict):
            body = policy
        else:
            body = policy.as_dict()
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
            .execute(request, Policy)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_o_auth_2_scopes(
            self, authServerId, query_params={}
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
            .execute(request, OAuth2Scope)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(OAuth2Scope(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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

        if isinstance(o_auth_2_scope, dict):
            body = o_auth_2_scope
        else:
            body = o_auth_2_scope.as_dict()
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
            .execute(request, OAuth2Scope)

        if error:
            return (None, response, error)

        try:
            result = OAuth2Scope(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /{scopeId}
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
                /{scopeId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OAuth2Scope)

        if error:
            return (None, response, error)

        try:
            result = OAuth2Scope(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

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
                /{scopeId}
            """)

        if isinstance(o_auth_2_scope, dict):
            body = o_auth_2_scope
        else:
            body = o_auth_2_scope.as_dict()
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
            .execute(request, OAuth2Scope)

        if error:
            return (None, response, error)

        try:
            result = OAuth2Scope(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
