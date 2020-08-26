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
from okta.models.csr\
    import Csr
from okta.models.json_web_key\
    import JsonWebKey
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
            self, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, application, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Application)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_app_model(body["signOnMode"], body["name"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_application(
            self, appId
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

    async def get_application(
            self, appId, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Application)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_app_model(body["signOnMode"], body["name"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_application(
            self, appId, application
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Application)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_app_model(body["signOnMode"], body["name"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_csrs_for_application(
            self, appId
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, csr_metadata
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, csrId
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

    async def get_csr_for_application(
            self, appId, csrId
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, csrId, string
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
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_binary_cer_cert(
            self, appId, csrId, string
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
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_der_cert(
            self, appId, csrId, string
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
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_binary_der_cert(
            self, appId, csrId, string
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
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def publish_binary_pem_cert(
            self, appId, csrId, string
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
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_application_keys(
            self, appId
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

    async def generate_application_key(
            self, appId, query_params={}
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
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_application_key(
            self, appId, keyId
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
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def clone_application_key(
            self, appId, keyId, query_params={}
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
            result = JsonWebKey(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_scope_consent_grants(
            self, appId, query_params={}
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

    async def grant_consent_to_scope(
            self, appId, o_auth_2_scope_consent_grant
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

    async def revoke_scope_consent_grant(
            self, appId, grantId
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

    async def get_scope_consent_grant(
            self, appId, grantId, query_params={}
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

    async def list_application_group_assignments(
            self, appId, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, groupId
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

    async def get_application_group_assignment(
            self, appId, groupId, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, groupId, application_group_assignment
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId
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

    async def deactivate_application(
            self, appId
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

    async def revoke_o_auth_2_tokens_for_application(
            self, appId
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

    async def list_o_auth_2_tokens_for_application(
            self, appId, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, tokenId
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

    async def get_o_auth_2_token_for_application(
            self, appId, tokenId, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, app_user
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
            self, appId, userId, query_params={}
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

    async def get_application_user(
            self, appId, userId, query_params={}
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
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
