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
from okta.models.application\
    import Application
from okta.models.provisioning_connection\
    import ProvisioningConnection
from okta.models.csr\
    import Csr
from okta.models.json_web_key\
    import JsonWebKey
from okta.models.client_secret\
    import ClientSecret
from okta.models.application_feature\
    import ApplicationFeature
from okta.models.o_auth_2_scope_consent_grant\
    import OAuth2ScopeConsentGrant
from okta.models.application_group_assignment\
    import ApplicationGroupAssignment
from okta.models.o_auth_2_token\
    import OAuth2Token
from okta.models.app_user\
    import AppUser
from okta.utils import format_url
from okta.api_client import APIClient
from okta.constants import find_app_model


class ApplicationClient(APIClient):
    """
    A Client object for the Application resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_applications(
            self, query_params={},
            keep_empty_params=False
    ):
        """
        Enumerates apps added to your organization with paginat
        ion. A subset of apps can be returned that match a supp
        orted filter expression or query.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
            [query_params.filter] {str}
            [query_params.expand] {str}
            [query_params.includeNonDeleted] {str}
        Returns:
            list: Collection of Application instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Application)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(
                    find_app_model(item["signOnMode"], item["name"])(
                        self.form_response_body(item)
                        )
                    )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_application(
            self, application, query_params={},
            keep_empty_params=False
    ):
        """
        Adds a new application to your Okta organization.
        Args:
            {application}
            query_params {dict}: Map of query parameters for request
            [query_params.activate] {str}
        Returns:
            Application
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(application, dict):
            body = application
        else:
            body = application.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Application)

        if error:
            return (None, response, error)

        try:
            body = response.get_body()
            result = find_app_model(body["signOnMode"], body["name"])(
                self.form_response_body(body)
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Removes an inactive application.
        Args:
            app_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_application(
            self, appId, query_params={},
            keep_empty_params=False
    ):
        """
        Fetches an application from your Okta organization by `
        id`.
        Args:
            app_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            Application
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Application)

        if error:
            return (None, response, error)

        try:
            body = response.get_body()
            result = find_app_model(body["signOnMode"], body["name"])(
                self.form_response_body(body)
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_application(
            self, appId, application,
            keep_empty_params=False
    ):
        """
        Updates an application in your organization.
        Args:
            app_id {str}
            {application}
        Returns:
            Application
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}
            """)

        if isinstance(application, dict):
            body = application
        else:
            body = application.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Application)

        if error:
            return (None, response, error)

        try:
            body = response.get_body()
            result = find_app_model(body["signOnMode"], body["name"])(
                self.form_response_body(body)
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_default_provisioning_connection_for_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Get default Provisioning Connection for application
        Args:
            app_id {str}
        Returns:
            ProvisioningConnection
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/connections/default
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ProvisioningConnection)

        if error:
            return (None, response, error)

        try:
            result = ProvisioningConnection(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def set_default_provisioning_connection_for_application(
            self, appId, provisioning_connection_request, query_params={},
            keep_empty_params=False
    ):
        """
        Set default Provisioning Connection for application
        Args:
            app_id {str}
            {provisioning_connection_request}
            query_params {dict}: Map of query parameters for request
            [query_params.activate] {str}
        Returns:
            ProvisioningConnection
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/connections/default
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(provisioning_connection_request, dict):
            body = provisioning_connection_request
        else:
            body = provisioning_connection_request.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ProvisioningConnection)

        if error:
            return (None, response, error)

        try:
            result = ProvisioningConnection(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_default_provisioning_connection_for_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Activates the default Provisioning Connection for an ap
        plication.
        Args:
            app_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/connections/default/lifecycle
                /activate
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def deactivate_default_provisioning_connection_for_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Deactivates the default Provisioning Connection for an
        application.
        Args:
            app_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/connections/default/lifecycle
                /deactivate
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def list_csrs_for_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Enumerates Certificate Signing Requests for an applicat
        ion
        Args:
            app_id {str}
        Returns:
            list: Collection of Csr instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Csr)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Csr(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def generate_csr_for_application(
            self, appId, csr_metadata,
            keep_empty_params=False
    ):
        """
        Generates a new key pair and returns the Certificate Si
        gning Request for it.
        Args:
            app_id {str}
            {csr_metadata}
        Returns:
            Csr
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs
            """)

        if isinstance(csr_metadata, dict):
            body = csr_metadata
        else:
            body = csr_metadata.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Csr)

        if error:
            return (None, response, error)

        try:
            result = Csr(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def revoke_csr_from_application(
            self, appId, csrId,
            keep_empty_params=False
    ):
        """
        Method for
        /api/v1/apps/{appId}/credentials/csrs/{csrId}
        Args:
            app_id {str}
            csr_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs/{csrId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_csr_for_application(
            self, appId, csrId,
            keep_empty_params=False
    ):
        """
        Method for
        /api/v1/apps/{appId}/credentials/csrs/{csrId}
        Args:
            app_id {str}
            csr_id {str}
        Returns:
            Csr
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs/{csrId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Csr)

        if error:
            return (None, response, error)

        try:
            result = Csr(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_cer_cert(
            self, appId, csrId, string,
            keep_empty_params=False
    ):
        """
        Method for
        /api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle
        /publish
        Args:
            app_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs/{csrId}
                /lifecycle/publish
            """)

        if isinstance(string, dict):
            body = string
        else:
            body = string.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-x509-ca-cert"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_binary_cer_cert(
            self, appId, csrId, string,
            keep_empty_params=False
    ):
        """
        Method for
        /api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle
        /publish
        Args:
            app_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs/{csrId}
                /lifecycle/publish
            """)

        body = HTTPClient.format_binary_data(string)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-x509-ca-cert"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_der_cert(
            self, appId, csrId, string,
            keep_empty_params=False
    ):
        """
        Method for
        /api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle
        /publish
        Args:
            app_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs/{csrId}
                /lifecycle/publish
            """)

        if isinstance(string, dict):
            body = string
        else:
            body = string.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/pkix-cert"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_binary_der_cert(
            self, appId, csrId, string,
            keep_empty_params=False
    ):
        """
        Method for
        /api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle
        /publish
        Args:
            app_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs/{csrId}
                /lifecycle/publish
            """)

        body = HTTPClient.format_binary_data(string)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/pkix-cert"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_binary_pem_cert(
            self, appId, csrId, string,
            keep_empty_params=False
    ):
        """
        Method for
        /api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle
        /publish
        Args:
            app_id {str}
            csr_id {str}
            {string}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/csrs/{csrId}
                /lifecycle/publish
            """)

        body = HTTPClient.format_binary_data(string)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-pem-file"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_application_keys(
            self, appId,
            keep_empty_params=False
    ):
        """
        Enumerates key credentials for an application
        Args:
            app_id {str}
        Returns:
            list: Collection of JsonWebKey instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/keys
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
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

    async def generate_application_key(
            self, appId, query_params={},
            keep_empty_params=False
    ):
        """
        Generates a new X.509 certificate for an application ke
        y credential
        Args:
            app_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.validityYears] {str}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/keys/generate
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_application_key(
            self, appId, keyId,
            keep_empty_params=False
    ):
        """
        Gets a specific application key credential by kid
        Args:
            app_id {str}
            key_id {str}
        Returns:
            JsonWebKey
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/keys/{keyId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def clone_application_key(
            self, appId, keyId, query_params={},
            keep_empty_params=False
    ):
        """
        Clones a X.509 certificate for an application key crede
        ntial from a source application to target application.
        Args:
            app_id {str}
            key_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.targetAid] {str}
        Returns:
            JsonWebKey
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/keys/{keyId}/clone
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, JsonWebKey)

        if error:
            return (None, response, error)

        try:
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_client_secrets_for_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Enumerates the client's collection of secrets
        Args:
            app_id {str}
        Returns:
            list: Collection of ClientSecret instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/secrets
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ClientSecret)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(ClientSecret(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_new_client_secret_for_application(
            self, appId, client_secret_metadata,
            keep_empty_params=False
    ):
        """
        Adds a new secret to the client's collection of secrets
        .
        Args:
            app_id {str}
            {client_secret_metadata}
        Returns:
            ClientSecret
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/secrets
            """)

        if isinstance(client_secret_metadata, dict):
            body = client_secret_metadata
        else:
            body = client_secret_metadata.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ClientSecret)

        if error:
            return (None, response, error)

        try:
            result = ClientSecret(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_client_secret_for_application(
            self, appId, secretId,
            keep_empty_params=False
    ):
        """
        Removes a secret from the client's collection of secret
        s.
        Args:
            app_id {str}
            secret_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/secrets/{secretId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_client_secret_for_application(
            self, appId, secretId,
            keep_empty_params=False
    ):
        """
        Gets a specific client secret by secretId
        Args:
            app_id {str}
            secret_id {str}
        Returns:
            ClientSecret
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/secrets/{secretId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ClientSecret)

        if error:
            return (None, response, error)

        try:
            result = ClientSecret(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_client_secret_for_application(
            self, appId, secretId,
            keep_empty_params=False
    ):
        """
        Activates a specific client secret by secretId
        Args:
            app_id {str}
            secret_id {str}
        Returns:
            ClientSecret
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/secrets/{secretId}
                /lifecycle/activate
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ClientSecret)

        if error:
            return (None, response, error)

        try:
            result = ClientSecret(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def deactivate_client_secret_for_application(
            self, appId, secretId,
            keep_empty_params=False
    ):
        """
        Deactivates a specific client secret by secretId
        Args:
            app_id {str}
            secret_id {str}
        Returns:
            ClientSecret
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/credentials/secrets/{secretId}
                /lifecycle/deactivate
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ClientSecret)

        if error:
            return (None, response, error)

        try:
            result = ClientSecret(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_features_for_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        List Features for application
        Args:
            app_id {str}
        Returns:
            list: Collection of ApplicationFeature instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/features
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ApplicationFeature)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(ApplicationFeature(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_feature_for_application(
            self, appId, name,
            keep_empty_params=False
    ):
        """
        Fetches a Feature object for an application.
        Args:
            app_id {str}
            name {str}
        Returns:
            ApplicationFeature
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/features/{name}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ApplicationFeature)

        if error:
            return (None, response, error)

        try:
            result = ApplicationFeature(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_feature_for_application(
            self, appId, name, capabilities_object,
            keep_empty_params=False
    ):
        """
        Updates a Feature object for an application.
        Args:
            app_id {str}
            name {str}
            {capabilities_object}
        Returns:
            ApplicationFeature
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/features/{name}
            """)

        if isinstance(capabilities_object, dict):
            body = capabilities_object
        else:
            body = capabilities_object.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ApplicationFeature)

        if error:
            return (None, response, error)

        try:
            result = ApplicationFeature(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_scope_consent_grants(
            self, appId, query_params={},
            keep_empty_params=False
    ):
        """
        Lists all scope consent grants for the application
        Args:
            app_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            list: Collection of OAuth2ScopeConsentGrant instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/grants
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
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

    async def grant_consent_to_scope(
            self, appId, o_auth_2_scope_consent_grant,
            keep_empty_params=False
    ):
        """
        Grants consent for the application to request an OAuth
        2.0 Okta scope
        Args:
            app_id {str}
            {o_auth_2_scope_consent_grant}
        Returns:
            OAuth2ScopeConsentGrant
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/grants
            """)

        if isinstance(o_auth_2_scope_consent_grant, dict):
            body = o_auth_2_scope_consent_grant
        else:
            body = o_auth_2_scope_consent_grant.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
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

    async def revoke_scope_consent_grant(
            self, appId, grantId,
            keep_empty_params=False
    ):
        """
        Revokes permission for the application to request the g
        iven scope
        Args:
            app_id {str}
            grant_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/grants/{grantId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_scope_consent_grant(
            self, appId, grantId, query_params={},
            keep_empty_params=False
    ):
        """
        Fetches a single scope consent grant for the applicatio
        n
        Args:
            app_id {str}
            grant_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            OAuth2ScopeConsentGrant
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/grants/{grantId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
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

    async def list_application_group_assignments(
            self, appId, query_params={},
            keep_empty_params=False
    ):
        """
        Enumerates group assignments for an application.
        Args:
            app_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
            [query_params.expand] {str}
        Returns:
            list: Collection of ApplicationGroupAssignment instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/groups
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ApplicationGroupAssignment)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(ApplicationGroupAssignment(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_application_group_assignment(
            self, appId, groupId,
            keep_empty_params=False
    ):
        """
        Removes a group assignment from an application.
        Args:
            app_id {str}
            group_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/groups/{groupId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_application_group_assignment(
            self, appId, groupId, query_params={},
            keep_empty_params=False
    ):
        """
        Fetches an application group assignment
        Args:
            app_id {str}
            group_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            ApplicationGroupAssignment
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/groups/{groupId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ApplicationGroupAssignment)

        if error:
            return (None, response, error)

        try:
            result = ApplicationGroupAssignment(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_application_group_assignment(
            self, appId, groupId, application_group_assignment,
            keep_empty_params=False
    ):
        """
        Assigns a group to an application
        Args:
            app_id {str}
            group_id {str}
            {application_group_assignment}
        Returns:
            ApplicationGroupAssignment
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/groups/{groupId}
            """)

        if isinstance(application_group_assignment, dict):
            body = application_group_assignment
        else:
            body = application_group_assignment.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ApplicationGroupAssignment)

        if error:
            return (None, response, error)

        try:
            result = ApplicationGroupAssignment(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Activates an inactive application.
        Args:
            app_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/lifecycle/activate
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def deactivate_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Deactivates an active application.
        Args:
            app_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/lifecycle/deactivate
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def upload_application_logo(
            self, appId, file,
            keep_empty_params=False
    ):
        """
        Update the logo for an application.
        Args:
            app_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/logo
            """)

        body = {}
        headers = {}
        form = {
            "file": file,
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def update_application_policy(
            self, appId, policyId,
            keep_empty_params=False
    ):
        """
        Assign an application to a specific policy. This unassi
        gns the application from its currently assigned policy.
        Args:
            app_id {str}
            policy_id {str}
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/policies/{policyId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def preview_saml_app_metadata(
            self, appId, query_params={},
            keep_empty_params=False
    ):
        """
        Previews SAML metadata based on a specific key credenti
        al for an application
        Args:
            app_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.kid] {str}
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/sso/saml/metadata
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        headers['Accept'] = "application/xml"
        request, error = await self._request_executor.create_request(
            http_method, api_url, None, headers, None, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def revoke_o_auth_2_tokens_for_application(
            self, appId,
            keep_empty_params=False
    ):
        """
        Revokes all tokens for the specified application
        Args:
            app_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/tokens
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def list_o_auth_2_tokens_for_application(
            self, appId, query_params={},
            keep_empty_params=False
    ):
        """
        Lists all tokens for the application
        Args:
            app_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
        Returns:
            list: Collection of OAuth2Token instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/tokens
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OAuth2Token)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(OAuth2Token(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def revoke_o_auth_2_token_for_application(
            self, appId, tokenId,
            keep_empty_params=False
    ):
        """
        Revokes the specified token for the specified applicati
        on
        Args:
            app_id {str}
            token_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/tokens/{tokenId}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_o_auth_2_token_for_application(
            self, appId, tokenId, query_params={},
            keep_empty_params=False
    ):
        """
        Gets a token for the specified application
        Args:
            app_id {str}
            token_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            OAuth2Token
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/tokens/{tokenId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OAuth2Token)

        if error:
            return (None, response, error)

        try:
            result = OAuth2Token(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_application_users(
            self, appId, query_params={},
            keep_empty_params=False
    ):
        """
        Enumerates all assigned [application users](#applicatio
        n-user-model) for an application.
        Args:
            app_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.q] {str}
            [query_params.query_scope] {str}
            [query_params.after] {str}
            [query_params.limit] {str}
            [query_params.filter] {str}
            [query_params.expand] {str}
        Returns:
            list: Collection of AppUser instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/users
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AppUser)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(AppUser(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def assign_user_to_application(
            self, appId, app_user,
            keep_empty_params=False
    ):
        """
        Assigns an user to an application with [credentials](#a
        pplication-user-credentials-object) and an app-specific
        [profile](#application-user-profile-object). Profile m
        appings defined for the application are first applied b
        efore applying any profile properties specified in the
        request.
        Args:
            app_id {str}
            {app_user}
        Returns:
            AppUser
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/users
            """)

        if isinstance(app_user, dict):
            body = app_user
        else:
            body = app_user.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AppUser)

        if error:
            return (None, response, error)

        try:
            result = AppUser(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_application_user(
            self, appId, userId, query_params={},
            keep_empty_params=False
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
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/users/{userId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_application_user(
            self, appId, userId, query_params={},
            keep_empty_params=False
    ):
        """
        Fetches a specific user assignment for application by `
        id`.
        Args:
            app_id {str}
            user_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            AppUser
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/users/{userId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AppUser)

        if error:
            return (None, response, error)

        try:
            result = AppUser(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_application_user(
            self, appId, userId, app_user,
            keep_empty_params=False
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
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/apps/{appId}/users/{userId}
            """)

        if isinstance(app_user, dict):
            body = app_user
        else:
            body = app_user.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, AppUser)

        if error:
            return (None, response, error)

        try:
            result = AppUser(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
