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
from okta.http_client import HTTPClient
from okta.utils import format_url
from okta.models.identity_provider\
    import IdentityProvider
from okta.models.json_web_key\
    import JsonWebKey
from okta.models.csr\
    import Csr
from okta.models.identity_provider_application_user\
    import IdentityProviderApplicationUser
from okta.models.social_auth_token\
    import SocialAuthToken


class IdentityProviderClient():
    """
    A Client object for the IdentityProvider resource.
    """
    def __init__(self):
        self._base_url = ""

    async def list_identity_providers(
            self, query_params
    ):
        """
        Enumerates IdPs in your organization with pagination. A
        subset of IdPs can be returned that match a supported
        filter expression or query.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
            [query_params.type] {str}
        Returns:
            list: Collection of IdentityProvider instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps
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
                result.append(IdentityProvider(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def create_identity_provider(
            self, identity_provider
    ):
        """
        Adds a new IdP to your organization.
        Args:
            {identity_provider}
        Returns:
            IdentityProvider
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps
            """)

        body = identity_provider.as_dict()
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
            result = IdentityProvider(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_identity_provider_keys(
            self, query_params
    ):
        """
        Enumerates IdP key credentials.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of JsonWebKey instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/credentials/keys
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
                result.append(JsonWebKey(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def create_identity_provider_key(
            self, json_web_key
    ):
        """
        Adds a new X.509 certificate credential to the IdP key
        store.
        Args:
            {json_web_key}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/credentials/keys
            """)

        body = json_web_key.as_dict()
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def delete_identity_provider_key(
            self, keyId
    ):
        """
        Deletes a specific IdP Key Credential by `kid` if it is
        not currently being used by an Active or Inactive IdP.
        Args:
            key_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/credentials/keys/{keyId}
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

    async def get_identity_provider_key(
            self, keyId
    ):
        """
        Gets a specific IdP Key Credential by `kid`
        Args:
            key_id {str}
        Returns:
            JsonWebKey
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/credentials/keys/{keyId}
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def delete_identity_provider(
            self, idpId
    ):
        """
        Removes an IdP from your organization.
        Args:
            idp_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}
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

    async def get_identity_provider(
            self, idpId
    ):
        """
        Fetches an IdP by `id`.
        Args:
            idp_id {str}
        Returns:
            IdentityProvider
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}
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
            result = IdentityProvider(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def update_identity_provider(
            self, idpId, identity_provider
    ):
        """
        Updates the configuration for an IdP.
        Args:
            idp_id {str}
            {identity_provider}
        Returns:
            IdentityProvider
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}
            """)

        body = identity_provider.as_dict()
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
            result = IdentityProvider(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_csrs_for_identity_provider(
            self, idpId
    ):
        """
        Enumerates Certificate Signing Requests for an IdP
        Args:
            idp_id {str}
        Returns:
            list: Collection of Csr instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs
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
                result.append(Csr(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def generate_csr_for_identity_provider(
            self, idpId, csr_metadata
    ):
        """
        Generates a new key pair and returns a Certificate Sign
        ing Request for it.
        Args:
            idp_id {str}
            {csr_metadata}
        Returns:
            Csr
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs
            """)

        body = csr_metadata.as_dict()
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
            result = Csr(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def revoke_csr_for_identity_provider(
            self, idpId, csrId
    ):
        """
        Revoke a Certificate Signing Request and delete the key
        pair from the IdP
        Args:
            idp_id {str}
            csr_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs/{csrId}
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

    async def get_csr_for_identity_provider(
            self, idpId, csrId
    ):
        """
        Gets a specific Certificate Signing Request model by id
        Args:
            idp_id {str}
            csr_id {str}
        Returns:
            Csr
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs/{csrId}
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
            result = Csr(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def publish_cer_cert_for_identity_provider(
            self, idpId, csrId, string
    ):
        """
        Update the Certificate Signing Request with a signed X.
        509 certificate and add it into the signing key credent
        ials for the IdP.
        Args:
            idp_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
            """)

        body = string.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-x509-ca-cert"
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def publish_binary_cer_cert_for_identity_provider(
            self, idpId, csrId, string
    ):
        """
        Update the Certificate Signing Request with a signed X.
        509 certificate and add it into the signing key credent
        ials for the IdP.
        Args:
            idp_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
            """)

        body = HTTPClient.format_binary_data(string)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-x509-ca-cert"
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def publish_der_cert_for_identity_provider(
            self, idpId, csrId, string
    ):
        """
        Update the Certificate Signing Request with a signed X.
        509 certificate and add it into the signing key credent
        ials for the IdP.
        Args:
            idp_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
            """)

        body = string.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/pkix-cert"
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def publish_binary_der_cert_for_identity_provider(
            self, idpId, csrId, string
    ):
        """
        Update the Certificate Signing Request with a signed X.
        509 certificate and add it into the signing key credent
        ials for the IdP.
        Args:
            idp_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
            """)

        body = HTTPClient.format_binary_data(string)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/pkix-cert"
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def publish_binary_pem_cert_for_identity_provider(
            self, idpId, csrId, string
    ):
        """
        Update the Certificate Signing Request with a signed X.
        509 certificate and add it into the signing key credent
        ials for the IdP.
        Args:
            idp_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
            """)

        body = HTTPClient.format_binary_data(string)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-pem-file"
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_identity_provider_signing_keys(
            self, idpId
    ):
        """
        Enumerates signing key credentials for an IdP
        Args:
            idp_id {str}
        Returns:
            list: Collection of JsonWebKey instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/keys
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

    async def generate_identity_provider_signing_key(
            self, idpId, query_params
    ):
        """
        Generates a new X.509 certificate for an IdP signing ke
        y credential to be used for signing assertions sent to
        the IdP
        Args:
            idp_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.validityYears] {str}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/keys/generate
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def get_identity_provider_signing_key(
            self, idpId, keyId
    ):
        """
        Gets a specific IdP Key Credential by `kid`
        Args:
            idp_id {str}
            key_id {str}
        Returns:
            JsonWebKey
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/keys/{keyId}
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def clone_identity_provider_key(
            self, idpId, keyId, query_params
    ):
        """
        Clones a X.509 certificate for an IdP signing key crede
        ntial from a source IdP to target IdP
        Args:
            idp_id {str}
            key_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.targetIdpId] {str}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/credentials/keys/{keyId}/clone
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
            result = JsonWebKey(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def activate_identity_provider(
            self, idpId
    ):
        """
        Activates an inactive IdP.
        Args:
            idp_id {str}
        Returns:
            IdentityProvider
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/lifecycle/activate
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
            result = IdentityProvider(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def deactivate_identity_provider(
            self, idpId
    ):
        """
        Deactivates an active IdP.
        Args:
            idp_id {str}
        Returns:
            IdentityProvider
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/lifecycle/deactivate
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
            result = IdentityProvider(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_identity_provider_application_users(
            self, idpId
    ):
        """
        Find all the users linked to an identity provider
        Args:
            idp_id {str}
        Returns:
            list: Collection of IdentityProviderApplicationUser instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/users
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
                result.append(IdentityProviderApplicationUser(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def unlink_user_from_identity_provider(
            self, idpId, userId
    ):
        """
        Removes the link between the Okta user and the IdP user
        .
        Args:
            idp_id {str}
            user_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/users/{userId}
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

    async def get_identity_provider_application_user(
            self, idpId, userId
    ):
        """
        Fetches a linked IdP user by ID
        Args:
            idp_id {str}
            user_id {str}
        Returns:
            IdentityProviderApplicationUser
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/users/{userId}
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
            result = IdentityProviderApplicationUser(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def link_user_to_identity_provider(
            self, idpId, userId, user_identity_provider_link_request
    ):
        """
        Links an Okta user to an existing Social Identity Provi
        der. This does not support the SAML2 Identity Provider
        Type
        Args:
            idp_id {str}
            user_id {str}
            {user_identity_provider_link_request}
        Returns:
            IdentityProviderApplicationUser
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/users/{userId}
            """)

        body = user_identity_provider_link_request.as_dict()
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
            result = IdentityProviderApplicationUser(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def list_social_auth_tokens(
            self, idpId, userId
    ):
        """
        Fetches the tokens minted by the Social Authentication
        Provider when the user authenticates with Okta via Soci
        al Auth.
        Args:
            idp_id {str}
            user_id {str}
        Returns:
            list: Collection of SocialAuthToken instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/idps/{idpId}/users/{userId}/credentials
                tokens
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
                result.append(SocialAuthToken(item))
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation