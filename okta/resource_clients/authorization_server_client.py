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
from okta.models.authorization_server_policy\
    import AuthorizationServerPolicy
from okta.models.authorization_server_policy_rule\
    import AuthorizationServerPolicyRule
from okta.models.o_auth_2_scope\
    import OAuth2Scope
from okta.utils import format_url
from okta.api_client import APIClient


class AuthorizationServerClient(APIClient):
    """
    A Client object for the AuthorizationServer resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_authorization_servers(
            self, query_params={},
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authorization_server,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_authorization_server(
            self, authServerId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, authorization_server,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, o_auth_2_claim,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, claimId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_o_auth_2_claim(
            self, authServerId, claimId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, claimId, o_auth_2_claim,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, clientId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def list_refresh_tokens_for_authorization_server_and_client(
            self, authServerId, clientId, query_params={},
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, clientId, tokenId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_refresh_token_for_authorization_server_and_client(
            self, authServerId, clientId, tokenId, query_params={},
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, jwk_use,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def deactivate_authorization_server(
            self, authServerId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def list_authorization_server_policies(
            self, authServerId,
            keep_empty_params=False
    ):
        """
        Args:
            auth_server_id {str}
        Returns:
            list: Collection of AuthorizationServerPolicy instances.
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AuthorizationServerPolicy)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(AuthorizationServerPolicy(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_authorization_server_policy(
            self, authServerId, authorization_server_policy,
            keep_empty_params=False
    ):
        """
        Args:
            auth_server_id {str}
            {authorization_server_policy}
        Returns:
            AuthorizationServerPolicy
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies
            """)

        if isinstance(authorization_server_policy, dict):
            body = authorization_server_policy
        else:
            body = authorization_server_policy.as_dict()
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
            .execute(request, AuthorizationServerPolicy)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServerPolicy(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_authorization_server_policy(
            self, authServerId, policyId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_authorization_server_policy(
            self, authServerId, policyId,
            keep_empty_params=False
    ):
        """
        Args:
            auth_server_id {str}
            policy_id {str}
        Returns:
            AuthorizationServerPolicy
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AuthorizationServerPolicy)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServerPolicy(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_authorization_server_policy(
            self, authServerId, policyId, authorization_server_policy,
            keep_empty_params=False
    ):
        """
        Args:
            auth_server_id {str}
            policy_id {str}
            {authorization_server_policy}
        Returns:
            AuthorizationServerPolicy
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}
            """)

        if isinstance(authorization_server_policy, dict):
            body = authorization_server_policy
        else:
            body = authorization_server_policy.as_dict()
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
            .execute(request, AuthorizationServerPolicy)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServerPolicy(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_authorization_server_policy(
            self, authServerId, policyId,
            keep_empty_params=False
    ):
        """
        Activate Authorization Server Policy
        Args:
            auth_server_id {str}
            policy_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/lifecycle/activate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def deactivate_authorization_server_policy(
            self, authServerId, policyId,
            keep_empty_params=False
    ):
        """
        Deactivate Authorization Server Policy
        Args:
            auth_server_id {str}
            policy_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/lifecycle/deactivate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def list_authorization_server_policy_rules(
            self, policyId, authServerId,
            keep_empty_params=False
    ):
        """
        Enumerates all policy rules for the specified Custom Au
        thorization Server and Policy.
        Args:
            policy_id {str}
            auth_server_id {str}
        Returns:
            list: Collection of AuthorizationServerPolicyRule instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/rules
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AuthorizationServerPolicyRule)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(AuthorizationServerPolicyRule(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_authorization_server_policy_rule(
            self, policyId, authServerId, authorization_server_policy_rule,
            keep_empty_params=False
    ):
        """
        Creates a policy rule for the specified Custom Authoriz
        ation Server and Policy.
        Args:
            policy_id {str}
            auth_server_id {str}
            {authorization_server_policy_rule}
        Returns:
            AuthorizationServerPolicyRule
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/rules
            """)

        if isinstance(authorization_server_policy_rule, dict):
            body = authorization_server_policy_rule
        else:
            body = authorization_server_policy_rule.as_dict()
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
            .execute(request, AuthorizationServerPolicyRule)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServerPolicyRule(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_authorization_server_policy_rule(
            self, policyId, authServerId, ruleId,
            keep_empty_params=False
    ):
        """
        Deletes a Policy Rule defined in the specified Custom A
        uthorization Server and Policy.
        Args:
            policy_id {str}
            auth_server_id {str}
            rule_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/rules/{ruleId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_authorization_server_policy_rule(
            self, policyId, authServerId, ruleId,
            keep_empty_params=False
    ):
        """
        Returns a Policy Rule by ID that is defined in the spec
        ified Custom Authorization Server and Policy.
        Args:
            policy_id {str}
            auth_server_id {str}
            rule_id {str}
        Returns:
            AuthorizationServerPolicyRule
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/rules/{ruleId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AuthorizationServerPolicyRule)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServerPolicyRule(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_authorization_server_policy_rule(
            self, policyId, authServerId, ruleId, authorization_server_policy_rule,
            keep_empty_params=False
    ):
        """
        Updates the configuration of the Policy Rule defined in
        the specified Custom Authorization Server and Policy.
        Args:
            policy_id {str}
            auth_server_id {str}
            rule_id {str}
            {authorization_server_policy_rule}
        Returns:
            AuthorizationServerPolicyRule
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/rules/{ruleId}
            """)

        if isinstance(authorization_server_policy_rule, dict):
            body = authorization_server_policy_rule
        else:
            body = authorization_server_policy_rule.as_dict()
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
            .execute(request, AuthorizationServerPolicyRule)

        if error:
            return (None, response, error)

        try:
            result = AuthorizationServerPolicyRule(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_authorization_server_policy_rule(
            self, authServerId, policyId, ruleId,
            keep_empty_params=False
    ):
        """
        Activate Authorization Server Policy Rule
        Args:
            auth_server_id {str}
            policy_id {str}
            rule_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/rules/{ruleId}/lifecycle
                /activate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def deactivate_authorization_server_policy_rule(
            self, authServerId, policyId, ruleId,
            keep_empty_params=False
    ):
        """
        Deactivate Authorization Server Policy Rule
        Args:
            auth_server_id {str}
            policy_id {str}
            rule_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/authorizationServers/{authServerId}
                /policies/{policyId}/rules/{ruleId}/lifecycle
                /deactivate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def list_o_auth_2_scopes(
            self, authServerId, query_params={},
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, o_auth_2_scope,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, scopeId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_o_auth_2_scope(
            self, authServerId, scopeId,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
            self, authServerId, scopeId, o_auth_2_scope,
            keep_empty_params=False
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
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
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
