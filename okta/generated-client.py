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

import okta.models as models
from urllib.parse import urlencode


class GeneratedAPIClient():
    """
    Auto-Generated API client; implements the operations as defined in the
    OpenAPI JSON spec
    """
    def __init__(self):
        self._base_url = ""

        async def list_applications(
            query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Application(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_application(
            application, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = application

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Application(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_application(
            appId
        ):
            """
            Removes an inactive application.
            Args:
                app_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_application(
            appId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Application(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_application(
            appId, application
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}
                """)

            body = application

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Application(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_csrs_for_application(
            appId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Csr(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def generate_csr_for_application(
            appId, csr_metadata
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs
                """)

            body = csr_metadata

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Csr(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_csr_from_application(
            appId, csrId
        ):
            """
            Method for
            /api/v1/apps/{appId}/credentials/csrs/{csrId}
            Args:
                app_id {str}
                csr_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs/{csrId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_csr_for_application(
            appId, csrId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs/{csrId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Csr(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_cer_cert(
            appId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_binary_cer_cert(
            appId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_der_cert(
            appId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_binary_der_cert(
            appId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_binary_pem_cert(
            appId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_application_keys(
            appId
        ):
            """
            Enumerates key credentials for an application
            Args:
                app_id {str}
            Returns:
                list: Collection of JsonWebKey instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/keys
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def generate_application_key(
            appId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/keys/generate
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def get_application_key(
            appId, keyId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/keys/{keyId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def clone_application_key(
            appId, keyId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/credentials/keys/{keyId}/clone
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_scope_consent_grants(
            appId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/grants
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2ScopeConsentGrant(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def grant_consent_to_scope(
            appId, o_auth_2_scope_consent_grant
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/grants
                """)

            body = o_auth_2_scope_consent_grant

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2ScopeConsentGrant(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_scope_consent_grant(
            appId, grantId
        ):
            """
            Revokes permission for the application to request the g
            iven scope
            Args:
                app_id {str}
                grant_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/grants/{grantId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_scope_consent_grant(
            appId, grantId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/grants/{grantId}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2ScopeConsentGrant(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_application_group_assignments(
            appId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/groups
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.ApplicationGroupAssignment(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_application_group_assignment(
            appId, groupId
        ):
            """
            Removes a group assignment from an application.
            Args:
                app_id {str}
                group_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/groups/{groupId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_application_group_assignment(
            appId, groupId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/groups/{groupId}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.ApplicationGroupAssignment(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_application_group_assignment(
            appId, groupId, application_group_assignment
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/groups/{groupId}
                """)

            body = application_group_assignment

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.ApplicationGroupAssignment(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_application(
            appId
        ):
            """
            Activates an inactive application.
            Args:
                app_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/lifecycle/activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def deactivate_application(
            appId
        ):
            """
            Deactivates an active application.
            Args:
                app_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/lifecycle/deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def revoke_o_auth_2_tokens_for_application(
            appId
        ):
            """
            Revokes all tokens for the specified application
            Args:
                app_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/tokens
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_o_auth_2_tokens_for_application(
            appId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/tokens
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Token(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_o_auth_2_token_for_application(
            appId, tokenId
        ):
            """
            Revokes the specified token for the specified applicati
            on
            Args:
                app_id {str}
                token_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/tokens/{tokenId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_o_auth_2_token_for_application(
            appId, tokenId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/tokens/{tokenId}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Token(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_application_users(
            appId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/users
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AppUser(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def assign_user_to_application(
            appId, app_user
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/users
                """)

            body = app_user

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AppUser(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_application_user(
            appId, userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_application_user(
            appId, userId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/apps/{appId}/users/{userId}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AppUser(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_application_user(
            appId, userId, app_user
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AppUser(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_authorization_servers(
            query_params
        ):
            """
            Success
            Args:
                query_params {dict}: Map of query parameters for request
                [query_params.q] {str}
                [query_params.limit] {str}
                [query_params.after] {str}
            Returns:
                list: Collection of AuthorizationServer instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AuthorizationServer(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_authorization_server(
            authorization_server
        ):
            """
            Success
            Args:
                {authorization_server}
            Returns:
                AuthorizationServer
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers
                """)

            body = authorization_server

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AuthorizationServer(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_authorization_server(
            authServerId
        ):
            """
            Success
            Args:
                auth_server_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_authorization_server(
            authServerId
        ):
            """
            Success
            Args:
                auth_server_id {str}
            Returns:
                AuthorizationServer
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AuthorizationServer(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_authorization_server(
            authServerId, authorization_server
        ):
            """
            Success
            Args:
                auth_server_id {str}
                {authorization_server}
            Returns:
                AuthorizationServer
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                """)

            body = authorization_server

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AuthorizationServer(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_o_auth_2_claims(
            authServerId
        ):
            """
            Success
            Args:
                auth_server_id {str}
            Returns:
                list: Collection of OAuth2Claim instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/claims
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Claim(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_o_auth_2_claim(
            authServerId, o_auth_2_claim
        ):
            """
            Success
            Args:
                auth_server_id {str}
                {o_auth_2_claim}
            Returns:
                OAuth2Claim
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/claims
                """)

            body = o_auth_2_claim

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Claim(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_o_auth_2_claim(
            authServerId, claimId
        ):
            """
            Success
            Args:
                auth_server_id {str}
                claim_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/claims
                {claimId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_o_auth_2_claim(
            authServerId, claimId
        ):
            """
            Success
            Args:
                auth_server_id {str}
                claim_id {str}
            Returns:
                OAuth2Claim
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/claims
                {claimId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Claim(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_o_auth_2_claim(
            authServerId, claimId, o_auth_2_claim
        ):
            """
            Success
            Args:
                auth_server_id {str}
                claim_id {str}
                {o_auth_2_claim}
            Returns:
                OAuth2Claim
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/claims
                {claimId}
                """)

            body = o_auth_2_claim

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Claim(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_o_auth_2_clients_for_authorization_server(
            authServerId
        ):
            """
            Success
            Args:
                auth_server_id {str}
            Returns:
                list: Collection of OAuth2Client instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/clients
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Client(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_refresh_tokens_for_authorization_server_and_client(
            authServerId, clientId
        ):
            """
            Success
            Args:
                auth_server_id {str}
                client_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/clients
                {clientId}/tokens
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_refresh_tokens_for_authorization_server_and_client(
            authServerId, clientId, query_params
        ):
            """
            Success
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/clients
                {clientId}/tokens
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2RefreshToken(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_refresh_token_for_authorization_server_and_client(
            authServerId, clientId, tokenId
        ):
            """
            Success
            Args:
                auth_server_id {str}
                client_id {str}
                token_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/clients
                {clientId}/tokens/{tokenId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_refresh_token_for_authorization_server_and_client(
            authServerId, clientId, tokenId, query_params
        ):
            """
            Success
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/clients
                {clientId}/tokens/{tokenId}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2RefreshToken(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_authorization_server_keys(
            authServerId
        ):
            """
            Success
            Args:
                auth_server_id {str}
            Returns:
                list: Collection of JsonWebKey instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                credentials/keys
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def rotate_authorization_server_keys(
            authServerId, jwk_use
        ):
            """
            Success
            Args:
                auth_server_id {str}
            Returns:
                list: Collection of JsonWebKey instances.
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                credentials/lifecycle/keyRotate
                """)

            body = jwk_use

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_authorization_server(
            authServerId
        ):
            """
            Success
            Args:
                auth_server_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                lifecycle/activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def deactivate_authorization_server(
            authServerId
        ):
            """
            Success
            Args:
                auth_server_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                lifecycle/deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_authorization_server_policies(
            authServerId
        ):
            """
            Success
            Args:
                auth_server_id {str}
            Returns:
                list: Collection of Policy instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                policies
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Policy(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_authorization_server_policy(
            authServerId, policy
        ):
            """
            Success
            Args:
                auth_server_id {str}
                {policy}
            Returns:
                Policy
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                policies
                """)

            body = policy

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Policy(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_authorization_server_policy(
            authServerId, policyId
        ):
            """
            Success
            Args:
                auth_server_id {str}
                policy_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                policies/{policyId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_authorization_server_policy(
            authServerId, policyId
        ):
            """
            Success
            Args:
                auth_server_id {str}
                policy_id {str}
            Returns:
                Policy
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                policies/{policyId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Policy(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_authorization_server_policy(
            authServerId, policyId, policy
        ):
            """
            Success
            Args:
                auth_server_id {str}
                policy_id {str}
                {policy}
            Returns:
                Policy
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}
                policies/{policyId}
                """)

            body = policy

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Policy(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_o_auth_2_scopes(
            authServerId, query_params
        ):
            """
            Success
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/scopes
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Scope(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_o_auth_2_scope(
            authServerId, o_auth_2_scope
        ):
            """
            Success
            Args:
                auth_server_id {str}
                {o_auth_2_scope}
            Returns:
                OAuth2Scope
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/scopes
                """)

            body = o_auth_2_scope

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Scope(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_o_auth_2_scope(
            authServerId, scopeId
        ):
            """
            Success
            Args:
                auth_server_id {str}
                scope_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/scopes
                {scopeId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_o_auth_2_scope(
            authServerId, scopeId
        ):
            """
            Success
            Args:
                auth_server_id {str}
                scope_id {str}
            Returns:
                OAuth2Scope
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/scopes
                {scopeId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Scope(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_o_auth_2_scope(
            authServerId, scopeId, o_auth_2_scope
        ):
            """
            Success
            Args:
                auth_server_id {str}
                scope_id {str}
                {o_auth_2_scope}
            Returns:
                OAuth2Scope
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/authorizationServers/{authServerId}/scopes
                {scopeId}
                """)

            body = o_auth_2_scope

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Scope(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_event_hooks(

        ):
            """
            Success
            Args:
            Returns:
                list: Collection of EventHook instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/eventHooks
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.EventHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_event_hook(
            event_hook
        ):
            """
            Success
            Args:
                {event_hook}
            Returns:
                EventHook
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/eventHooks
                """)

            body = event_hook

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.EventHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_event_hook(
            eventHookId
        ):
            """
            Success
            Args:
                event_hook_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/eventHooks/{eventHookId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_event_hook(
            eventHookId
        ):
            """
            Success
            Args:
                event_hook_id {str}
            Returns:
                EventHook
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/eventHooks/{eventHookId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.EventHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_event_hook(
            eventHookId, event_hook
        ):
            """
            Success
            Args:
                event_hook_id {str}
                {event_hook}
            Returns:
                EventHook
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/eventHooks/{eventHookId}
                """)

            body = event_hook

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.EventHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_event_hook(
            eventHookId
        ):
            """
            Success
            Args:
                event_hook_id {str}
            Returns:
                EventHook
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/eventHooks/{eventHookId}/lifecycle/activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.EventHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def deactivate_event_hook(
            eventHookId
        ):
            """
            Success
            Args:
                event_hook_id {str}
            Returns:
                EventHook
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/eventHooks/{eventHookId}/lifecycle
                deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.EventHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def verify_event_hook(
            eventHookId
        ):
            """
            Success
            Args:
                event_hook_id {str}
            Returns:
                EventHook
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/eventHooks/{eventHookId}/lifecycle/verify
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.EventHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_features(

        ):
            """
            Success
            Args:
            Returns:
                list: Collection of Feature instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/features
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Feature(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def get_feature(
            featureId
        ):
            """
            Success
            Args:
                feature_id {str}
            Returns:
                Feature
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/features/{featureId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Feature(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_feature_dependencies(
            featureId
        ):
            """
            Success
            Args:
                feature_id {str}
            Returns:
                list: Collection of Feature instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/features/{featureId}/dependencies
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Feature(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_feature_dependents(
            featureId
        ):
            """
            Success
            Args:
                feature_id {str}
            Returns:
                list: Collection of Feature instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/features/{featureId}/dependents
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Feature(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_feature_lifecycle(
            featureId, lifecycle, query_params
        ):
            """
            Success
            Args:
                feature_id {str}
                lifecycle {str}
                query_params {dict}: Map of query parameters for request
                [query_params.mode] {str}
            Returns:
                Feature
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/features/{featureId}/{lifecycle}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Feature(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_groups(
            query_params
        ):
            """
            Enumerates groups in your organization with pagination.
            A subset of groups can be returned that match a suppor
            ted filter expression or query.
            Args:
                query_params {dict}: Map of query parameters for request
                [query_params.q] {str}
                [query_params.filter] {str}
                [query_params.after] {str}
                [query_params.limit] {str}
            Returns:
                list: Collection of Group instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Group(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_group(
            group
        ):
            """
            Adds a new group with `OKTA_GROUP` type to your organiz
            ation.
            Args:
                {group}
            Returns:
                Group
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups
                """)

            body = group

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Group(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_group_rules(
            query_params
        ):
            """
            Lists all group rules for your organization.
            Args:
                query_params {dict}: Map of query parameters for request
                [query_params.limit] {str}
                [query_params.after] {str}
                [query_params.search] {str}
                [query_params.expand] {str}
            Returns:
                list: Collection of GroupRule instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/rules
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.GroupRule(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_group_rule(
            group_rule
        ):
            """
            Creates a group rule to dynamically add users to the sp
            ecified group if they match the condition
            Args:
                {group_rule}
            Returns:
                GroupRule
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/rules
                """)

            body = group_rule

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.GroupRule(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_group_rule(
            ruleId
        ):
            """
            Removes a specific group rule by id from your organizat
            ion
            Args:
                rule_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/rules/{ruleId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_group_rule(
            ruleId, query_params
        ):
            """
            Fetches a specific group rule by id from your organizat
            ion
            Args:
                rule_id {str}
                query_params {dict}: Map of query parameters for request
                [query_params.expand] {str}
            Returns:
                GroupRule
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/rules/{ruleId}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.GroupRule(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_group_rule(
            ruleId, group_rule
        ):
            """
            Updates a group rule. Only `INACTIVE` rules can be upda
            ted.
            Args:
                rule_id {str}
                {group_rule}
            Returns:
                GroupRule
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/rules/{ruleId}
                """)

            body = group_rule

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.GroupRule(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_group_rule(
            ruleId
        ):
            """
            Activates a specific group rule by id from your organiz
            ation
            Args:
                rule_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/rules/{ruleId}/lifecycle/activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def deactivate_group_rule(
            ruleId
        ):
            """
            Deactivates a specific group rule by id from your organ
            ization
            Args:
                rule_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/rules/{ruleId}/lifecycle/deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def delete_group(
            groupId
        ):
            """
            Removes a group with `OKTA_GROUP` type from your organi
            zation.
            Args:
                group_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_group(
            groupId
        ):
            """
            Lists all group rules for your organization.
            Args:
                group_id {str}
            Returns:
                Group
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Group(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_group(
            groupId, group
        ):
            """
            Updates the profile for a group with `OKTA_GROUP` type
            from your organization.
            Args:
                group_id {str}
                {group}
            Returns:
                Group
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}
                """)

            body = group

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Group(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_assigned_applications_for_group(
            groupId, query_params
        ):
            """
            Enumerates all applications that are assigned to a grou
            p.
            Args:
                group_id {str}
                query_params {dict}: Map of query parameters for request
                [query_params.after] {str}
                [query_params.limit] {str}
            Returns:
                list: Collection of Application instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/apps
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Application(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_group_assigned_roles(
            groupId, query_params
        ):
            """
            Success
            Args:
                group_id {str}
                query_params {dict}: Map of query parameters for request
                [query_params.expand] {str}
            Returns:
                list: Collection of Role instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Role(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def assign_role_to_group(
            groupId, assign_role_request, query_params
        ):
            """
            Assigns a Role to a Group
            Args:
                group_id {str}
                {assign_role_request}
                query_params {dict}: Map of query parameters for request
                [query_params.disableNotifications] {str}
            Returns:
                Role
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = assign_role_request

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Role(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def remove_role_from_group(
            groupId, roleId
        ):
            """
            Unassigns a Role from a Group
            Args:
                group_id {str}
                role_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles/{roleId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_role(
            groupId, roleId
        ):
            """
            Success
            Args:
                group_id {str}
                role_id {str}
            Returns:
                Role
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles/{roleId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Role(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_app_targets_for_application_admin_role_for_group(
            groupId, roleId, query_params
        ):
            """
            Lists all App targets for an `APP_ADMIN` Role assigned
            to a Group. This methods return list may include full A
            pplications or Instances. The response for an instance
            will have an `ID` value, while Application will not hav
            e an ID.
            Args:
                group_id {str}
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
                /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.CatalogApplication(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def remove_app_target_from_application_admin_role_given_to_group(
            groupId, roleId, appName
        ):
            """
            Success
            Args:
                group_id {str}
                role_id {str}
                app_name {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps/{appName}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def add_application_target_to_admin_role_given_to_group(
            groupId, roleId, appName
        ):
            """
            Success
            Args:
                group_id {str}
                role_id {str}
                app_name {str}
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps/{appName}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def remove_app_target_from_admin_role_given_to_group(
            groupId, roleId, appName, applicationId
        ):
            """
            Remove App Instance Target to App Administrator Role gi
            ven to a Group
            Args:
                group_id {str}
                role_id {str}
                app_name {str}
                application_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps/{appName}/{applicationId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def add_app_instance_target_to_app_admin_role_given_to_group(
            groupId, roleId, appName, applicationId
        ):
            """
            Add App Instance Target to App Administrator Role given
            to a Group
            Args:
                group_id {str}
                role_id {str}
                app_name {str}
                application_id {str}
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles/{roleId}/targets
                catalog/apps/{appName}/{applicationId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_group_targets_for_group_role(
            groupId, roleId, query_params
        ):
            """
            Success
            Args:
                group_id {str}
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
                /api/v1/groups/{groupId}/roles/{roleId}/targets
                groups
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Group(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def remove_group_target_from_group_admin_role_given_to_group(
            groupId, roleId, targetGroupId
        ):
            """
            Method for
            /api/v1/groups/{groupId}/roles/{roleId}/targets/groups/
            {targetGroupId}
            Args:
                group_id {str}
                role_id {str}
                target_group_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles/{roleId}/targets
                groups/{targetGroupId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def add_group_target_to_group_administrator_role_for_group(
            groupId, roleId, targetGroupId
        ):
            """
            Method for
            /api/v1/groups/{groupId}/roles/{roleId}/targets/groups/
            {targetGroupId}
            Args:
                group_id {str}
                role_id {str}
                target_group_id {str}
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/roles/{roleId}/targets
                groups/{targetGroupId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_group_users(
            groupId, query_params
        ):
            """
            Enumerates all users that are a member of a group.
            Args:
                group_id {str}
                query_params {dict}: Map of query parameters for request
                [query_params.after] {str}
                [query_params.limit] {str}
            Returns:
                list: Collection of User instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/users
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.User(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def remove_user_from_group(
            groupId, userId
        ):
            """
            Removes a user from a group with 'OKTA_GROUP' type.
            Args:
                group_id {str}
                user_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/users/{userId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def add_user_to_group(
            groupId, userId
        ):
            """
            Adds a user to a group with 'OKTA_GROUP' type.
            Args:
                group_id {str}
                user_id {str}
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/groups/{groupId}/users/{userId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_identity_providers(
            query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProvider(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_identity_provider(
            identity_provider
        ):
            """
            Adds a new IdP to your organization.
            Args:
                {identity_provider}
            Returns:
                IdentityProvider
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps
                """)

            body = identity_provider

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProvider(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_identity_provider_keys(
            query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/credentials/keys
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_identity_provider_key(
            json_web_key
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/credentials/keys
                """)

            body = json_web_key

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_identity_provider_key(
            keyId
        ):
            """
            Deletes a specific IdP Key Credential by `kid` if it is
            not currently being used by an Active or Inactive IdP.
            Args:
                key_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/credentials/keys/{keyId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_identity_provider_key(
            keyId
        ):
            """
            Gets a specific IdP Key Credential by `kid`
            Args:
                key_id {str}
            Returns:
                JsonWebKey
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/credentials/keys/{keyId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_identity_provider(
            idpId
        ):
            """
            Removes an IdP from your organization.
            Args:
                idp_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_identity_provider(
            idpId
        ):
            """
            Fetches an IdP by `id`.
            Args:
                idp_id {str}
            Returns:
                IdentityProvider
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProvider(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_identity_provider(
            idpId, identity_provider
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}
                """)

            body = identity_provider

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProvider(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_csrs_for_identity_provider(
            idpId
        ):
            """
            Enumerates Certificate Signing Requests for an IdP
            Args:
                idp_id {str}
            Returns:
                list: Collection of Csr instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Csr(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def generate_csr_for_identity_provider(
            idpId, csr_metadata
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs
                """)

            body = csr_metadata

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Csr(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_csr_for_identity_provider(
            idpId, csrId
        ):
            """
            Revoke a Certificate Signing Request and delete the key
            pair from the IdP
            Args:
                idp_id {str}
                csr_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_csr_for_identity_provider(
            idpId, csrId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Csr(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_cer_cert_for_identity_provider(
            idpId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_binary_cer_cert_for_identity_provider(
            idpId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_der_cert_for_identity_provider(
            idpId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_binary_der_cert_for_identity_provider(
            idpId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def publish_binary_pem_cert_for_identity_provider(
            idpId, csrId, string
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/csrs/{csrId}
                lifecycle/publish
                """)

            body = string

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_identity_provider_signing_keys(
            idpId
        ):
            """
            Enumerates signing key credentials for an IdP
            Args:
                idp_id {str}
            Returns:
                list: Collection of JsonWebKey instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/keys
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def generate_identity_provider_signing_key(
            idpId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/keys/generate
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def get_identity_provider_signing_key(
            idpId, keyId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/keys/{keyId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def clone_identity_provider_key(
            idpId, keyId, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/credentials/keys/{keyId}/clone
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.JsonWebKey(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_identity_provider(
            idpId
        ):
            """
            Activates an inactive IdP.
            Args:
                idp_id {str}
            Returns:
                IdentityProvider
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/lifecycle/activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProvider(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def deactivate_identity_provider(
            idpId
        ):
            """
            Deactivates an active IdP.
            Args:
                idp_id {str}
            Returns:
                IdentityProvider
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/lifecycle/deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProvider(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_identity_provider_application_users(
            idpId
        ):
            """
            Find all the users linked to an identity provider
            Args:
                idp_id {str}
            Returns:
                list: Collection of IdentityProviderApplicationUser instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/users
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProviderApplicationUser(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def unlink_user_from_identity_provider(
            idpId, userId
        ):
            """
            Removes the link between the Okta user and the IdP user
            .
            Args:
                idp_id {str}
                user_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/users/{userId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_identity_provider_application_user(
            idpId, userId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/users/{userId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProviderApplicationUser(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def link_user_to_identity_provider(
            idpId, userId, user_identity_provider_link_request
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/users/{userId}
                """)

            body = user_identity_provider_link_request

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProviderApplicationUser(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_social_auth_tokens(
            idpId, userId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/idps/{idpId}/users/{userId}/credentials
                tokens
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.SocialAuthToken(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_inline_hooks(
            query_params
        ):
            """
            Success
            Args:
                query_params {dict}: Map of query parameters for request
                [query_params.type] {str}
            Returns:
                list: Collection of InlineHook instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/inlineHooks
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.InlineHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_inline_hook(
            inline_hook
        ):
            """
            Success
            Args:
                {inline_hook}
            Returns:
                InlineHook
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/inlineHooks
                """)

            body = inline_hook

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.InlineHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_inline_hook(
            inlineHookId
        ):
            """
            Deletes the Inline Hook matching the provided id. Once
            deleted, the Inline Hook is unrecoverable. As a safety
            precaution, only Inline Hooks with a status of INACTIVE
            are eligible for deletion.
            Args:
                inline_hook_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/inlineHooks/{inlineHookId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_inline_hook(
            inlineHookId
        ):
            """
            Gets an inline hook by ID
            Args:
                inline_hook_id {str}
            Returns:
                InlineHook
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/inlineHooks/{inlineHookId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.InlineHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_inline_hook(
            inlineHookId, inline_hook
        ):
            """
            Updates an inline hook by ID
            Args:
                inline_hook_id {str}
                {inline_hook}
            Returns:
                InlineHook
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/inlineHooks/{inlineHookId}
                """)

            body = inline_hook

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.InlineHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def execute_inline_hook(
            inlineHookId, inline_hook_payload
        ):
            """
            Executes the Inline Hook matching the provided inlineHo
            okId using the request body as the input. This will sen
            d the provided data through the Channel and return a re
            sponse if it matches the correct data contract. This ex
            ecution endpoint should only be used for testing purpos
            es.
            Args:
                inline_hook_id {str}
                {inline_hook_payload}
            Returns:
                InlineHookResponse
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/inlineHooks/{inlineHookId}/execute
                """)

            body = inline_hook_payload

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.InlineHookResponse(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_inline_hook(
            inlineHookId
        ):
            """
            Activates the Inline Hook matching the provided id
            Args:
                inline_hook_id {str}
            Returns:
                InlineHook
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/inlineHooks/{inlineHookId}/lifecycle
                activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.InlineHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def deactivate_inline_hook(
            inlineHookId
        ):
            """
            Deactivates the Inline Hook matching the provided id
            Args:
                inline_hook_id {str}
            Returns:
                InlineHook
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/inlineHooks/{inlineHookId}/lifecycle
                deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.InlineHook(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def get_logs(
            query_params
        ):
            """
            The Okta System Log API provides read access to your or
            ganization’s system log. This API provides more functio
            nality than the Events API
            Args:
                query_params {dict}: Map of query parameters for request
                [query_params.until] {str}
                [query_params.since] {str}
                [query_params.filter] {str}
                [query_params.q] {str}
                [query_params.limit] {str}
                [query_params.sortOrder] {str}
                [query_params.after] {str}
            Returns:
                list: Collection of LogEvent instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/logs
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.LogEvent(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_linked_object_definitions(

        ):
            """
            Success
            Args:
            Returns:
                list: Collection of LinkedObject instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/schemas/user/linkedObjects
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.LinkedObject(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def add_linked_object_definition(
            linked_object
        ):
            """
            Success
            Args:
                {linked_object}
            Returns:
                LinkedObject
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/schemas/user/linkedObjects
                """)

            body = linked_object

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.LinkedObject(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_linked_object_definition(
            linkedObjectName
        ):
            """
            Success
            Args:
                linked_object_name {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/schemas/user/linkedObjects
                {linkedObjectName}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_linked_object_definition(
            linkedObjectName
        ):
            """
            Success
            Args:
                linked_object_name {str}
            Returns:
                LinkedObject
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/schemas/user/linkedObjects
                {linkedObjectName}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.LinkedObject(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_user_types(

        ):
            """
            Fetches all User Types in your org
            Args:
            Returns:
                list: Collection of UserType instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/types/user
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserType(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_user_type(
            user_type
        ):
            """
            Creates a new User Type. A default User Type is automat
            ically created along with your org, and you may add ano
            ther 9 User Types for a maximum of 10.
            Args:
                {user_type}
            Returns:
                UserType
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/types/user
                """)

            body = user_type

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserType(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_user_type(
            typeId
        ):
            """
            Deletes a User Type permanently. This operation is not
            permitted for the default type, nor for any User Type t
            hat has existing users
            Args:
                type_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/types/user/{typeId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_user_type(
            typeId
        ):
            """
            Fetches a User Type by ID. The special identifier `defa
            ult` may be used to fetch the default User Type.
            Args:
                type_id {str}
            Returns:
                UserType
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/types/user/{typeId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserType(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_user_type(
            typeId, user_type
        ):
            """
            Updates an existing User Type
            Args:
                type_id {str}
                {user_type}
            Returns:
                UserType
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/types/user/{typeId}
                """)

            body = user_type

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserType(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def replace_user_type(
            typeId, user_type
        ):
            """
            Replace an existing User Type
            Args:
                type_id {str}
                {user_type}
            Returns:
                UserType
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/meta/types/user/{typeId}
                """)

            body = user_type

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserType(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_policies(
            query_params
        ):
            """
            Gets all policies with the specified type.
            Args:
                query_params {dict}: Map of query parameters for request
                [query_params.type] {str}
                [query_params.status] {str}
                [query_params.expand] {str}
            Returns:
                list: Collection of Policy instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Policy(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_policy(
            policy, query_params
        ):
            """
            Creates a policy.
            Args:
                {policy}
                query_params {dict}: Map of query parameters for request
                [query_params.activate] {str}
            Returns:
                Policy
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = policy

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Policy(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_policy(
            policyId
        ):
            """
            Removes a policy.
            Args:
                policy_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_policy(
            policyId, query_params
        ):
            """
            Gets a policy.
            Args:
                policy_id {str}
                query_params {dict}: Map of query parameters for request
                [query_params.expand] {str}
            Returns:
                Policy
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Policy(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_policy(
            policyId, policy
        ):
            """
            Updates a policy.
            Args:
                policy_id {str}
                {policy}
            Returns:
                Policy
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}
                """)

            body = policy

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Policy(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_policy(
            policyId
        ):
            """
            Activates a policy.
            Args:
                policy_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/lifecycle/activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def deactivate_policy(
            policyId
        ):
            """
            Deactivates a policy.
            Args:
                policy_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/lifecycle/deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_policy_rules(
            policyId
        ):
            """
            Enumerates all policy rules.
            Args:
                policy_id {str}
            Returns:
                list: Collection of PolicyRule instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/rules
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.PolicyRule(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_policy_rule(
            policyId, policy_rule
        ):
            """
            Creates a policy rule.
            Args:
                policy_id {str}
                {policy_rule}
            Returns:
                PolicyRule
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/rules
                """)

            body = policy_rule

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.PolicyRule(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_policy_rule(
            policyId, ruleId
        ):
            """
            Removes a policy rule.
            Args:
                policy_id {str}
                rule_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/rules/{ruleId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_policy_rule(
            policyId, ruleId
        ):
            """
            Gets a policy rule.
            Args:
                policy_id {str}
                rule_id {str}
            Returns:
                PolicyRule
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/rules/{ruleId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.PolicyRule(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_policy_rule(
            policyId, ruleId, policy_rule
        ):
            """
            Updates a policy rule.
            Args:
                policy_id {str}
                rule_id {str}
                {policy_rule}
            Returns:
                PolicyRule
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/rules/{ruleId}
                """)

            body = policy_rule

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.PolicyRule(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_policy_rule(
            policyId, ruleId
        ):
            """
            Activates a policy rule.
            Args:
                policy_id {str}
                rule_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/rules/{ruleId}
                lifecycle/activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def deactivate_policy_rule(
            policyId, ruleId
        ):
            """
            Deactivates a policy rule.
            Args:
                policy_id {str}
                rule_id {str}
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/policies/{policyId}/rules/{ruleId}
                lifecycle/deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def create_session(
            create_session_request
        ):
            """
            Creates a new session for a user with a valid session t
            oken. Use this API if, for example, you want to set the
            session cookie yourself instead of allowing Okta to se
            t it, or want to hold the session ID in order to delete
            a session via the API instead of visiting the logout U
            RL.
            Args:
                {create_session_request}
            Returns:
                Session
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/sessions
                """)

            body = create_session_request

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Session(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def end_session(
            sessionId
        ):
            """
            Method for
            /api/v1/sessions/{sessionId}
            Args:
                session_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/sessions/{sessionId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_session(
            sessionId
        ):
            """
            Get details about a session.
            Args:
                session_id {str}
            Returns:
                Session
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/sessions/{sessionId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Session(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def refresh_session(
            sessionId
        ):
            """
            Method for
            /api/v1/sessions/{sessionId}/lifecycle/refresh
            Args:
                session_id {str}
            Returns:
                Session
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/sessions/{sessionId}/lifecycle/refresh
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Session(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_sms_templates(
            query_params
        ):
            """
            Enumerates custom SMS templates in your organization. A
            subset of templates can be returned that match a templ
            ate type.
            Args:
                query_params {dict}: Map of query parameters for request
                [query_params.templateType] {str}
            Returns:
                list: Collection of SmsTemplate instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/templates/sms
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.SmsTemplate(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_sms_template(
            sms_template
        ):
            """
            Adds a new custom SMS template to your organization.
            Args:
                {sms_template}
            Returns:
                SmsTemplate
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/templates/sms
                """)

            body = sms_template

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.SmsTemplate(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_sms_template(
            templateId
        ):
            """
            Removes an SMS template.
            Args:
                template_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/templates/sms/{templateId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_sms_template(
            templateId
        ):
            """
            Fetches a specific template by `id`
            Args:
                template_id {str}
            Returns:
                SmsTemplate
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/templates/sms/{templateId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.SmsTemplate(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def partial_update_sms_template(
            templateId, sms_template
        ):
            """
            Updates only some of the SMS template properties:
            Args:
                template_id {str}
                {sms_template}
            Returns:
                SmsTemplate
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/templates/sms/{templateId}
                """)

            body = sms_template

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.SmsTemplate(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_sms_template(
            templateId, sms_template
        ):
            """
            Updates the SMS template.
            Args:
                template_id {str}
                {sms_template}
            Returns:
                SmsTemplate
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/templates/sms/{templateId}
                """)

            body = sms_template

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.SmsTemplate(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_origins(
            query_params
        ):
            """
            Success
            Args:
                query_params {dict}: Map of query parameters for request
                [query_params.q] {str}
                [query_params.filter] {str}
                [query_params.after] {str}
                [query_params.limit] {str}
            Returns:
                list: Collection of TrustedOrigin instances.
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/trustedOrigins
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.TrustedOrigin(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_origin(
            trusted_origin
        ):
            """
            Success
            Args:
                {trusted_origin}
            Returns:
                TrustedOrigin
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/trustedOrigins
                """)

            body = trusted_origin

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.TrustedOrigin(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_origin(
            trustedOriginId
        ):
            """
            Success
            Args:
                trusted_origin_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/trustedOrigins/{trustedOriginId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_origin(
            trustedOriginId
        ):
            """
            Success
            Args:
                trusted_origin_id {str}
            Returns:
                TrustedOrigin
            """
            http_method = "get".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/trustedOrigins/{trustedOriginId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.TrustedOrigin(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_origin(
            trustedOriginId, trusted_origin
        ):
            """
            Success
            Args:
                trusted_origin_id {str}
                {trusted_origin}
            Returns:
                TrustedOrigin
            """
            http_method = "put".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/trustedOrigins/{trustedOriginId}
                """)

            body = trusted_origin

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.TrustedOrigin(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_origin(
            trustedOriginId
        ):
            """
            Success
            Args:
                trusted_origin_id {str}
            Returns:
                TrustedOrigin
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/trustedOrigins/{trustedOriginId}/lifecycle
                activate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.TrustedOrigin(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def deactivate_origin(
            trustedOriginId
        ):
            """
            Success
            Args:
                trusted_origin_id {str}
            Returns:
                TrustedOrigin
            """
            http_method = "post".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/trustedOrigins/{trustedOriginId}/lifecycle
                deactivate
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.TrustedOrigin(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_users(
            query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.User(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def create_user(
            create_user_request, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.User(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def set_linked_object_for_user(
            associatedUserId, primaryRelationshipName, primaryUserId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def deactivate_or_delete_user(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_user(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.User(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def partial_update_user(
            userId, user, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.User(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def update_user(
            userId, user, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.User(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_app_links(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.AppLink(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_user_clients(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2Client(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_grants_for_user_and_client(
            userId, clientId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_grants_for_user_and_client(
            userId, clientId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2ScopeConsentGrant(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_tokens_for_user_and_client(
            userId, clientId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_refresh_tokens_for_user_and_client(
            userId, clientId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2RefreshToken(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_token_for_user_and_client(
            userId, clientId, tokenId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_refresh_token_for_user_and_client(
            userId, clientId, tokenId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2RefreshToken(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def change_password(
            userId, change_password_request, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserCredentials(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def change_recovery_question(
            userId, user_credentials
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserCredentials(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def forgot_password_generate_one_time_token(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.ForgotPasswordResponse(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def forgot_password_set_new_password(
            userId, user_credentials, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.ForgotPasswordResponse(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_factors(
            userId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserFactor(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def enroll_factor(
            userId, user_factor, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = user_factor

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserFactor(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_supported_factors(
            userId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors/catalog
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserFactor(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_supported_security_questions(
            userId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors/questions
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.SecurityQuestion(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def delete_factor(
            userId, factorId
        ):
            """
            Unenrolls an existing factor for the specified user, al
            lowing the user to enroll a new factor.
            Args:
                user_id {str}
                factor_id {str}
            """
            http_method = "delete".upper()
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors/{factorId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_factor(
            userId, factorId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors/{factorId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserFactor(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_factor(
            userId, factorId, activate_factor_request
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors/{factorId}/lifecycle
                activate
                """)

            body = activate_factor_request

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserFactor(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def get_factor_transaction_status(
            userId, factorId, transactionId
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors/{factorId}
                transactions/{transactionId}
                """)

            body = None

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.VerifyUserFactorResponse(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def verify_factor(
            userId, factorId, verify_factor_request, query_params
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
            api_url = self.format_url(f"""
                {self._base_url}
                /api/v1/users/{userId}/factors/{factorId}/verify
                """)
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

            body = verify_factor_request

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.VerifyUserFactorResponse(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_user_grants(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_user_grants(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2ScopeConsentGrant(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def revoke_user_grant(
            userId, grantId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_user_grant(
            userId, grantId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.OAuth2ScopeConsentGrant(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_user_groups(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Group(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_user_identity_providers(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.IdentityProvider(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def activate_user(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserActivationToken(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def deactivate_user(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def expire_password(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.User(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def expire_password_and_get_temporary_password(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.TempPassword(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def reactivate_user(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.UserActivationToken(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def reset_factors(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def reset_password(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.ResetPasswordToken(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def suspend_user(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def unlock_user(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def unsuspend_user(
            userId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def remove_linked_object_for_user(
            userId, relationshipName
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def get_linked_objects_for_user(
            userId, relationshipName, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.ResponseLinks(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def list_assigned_roles_for_user(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Role(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def assign_role_to_user(
            userId, assign_role_request, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Role(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def remove_role_from_user(
            userId, roleId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_app_targets_for_application_admin_role_for_user(
            userId, roleId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.CatalogApplication(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def add_all_apps_as_target_to_role(
            userId, roleId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def remove_app_target_from_application_admin_role_for_user(
            userId, roleId, appName
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def add_application_target_to_admin_role_for_user(
            userId, roleId, appName
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def remove_application_target_from_administrator_role_for_user(
            userId, roleId, appName, applicationId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def add_application_target_to_app_admin_role_for_user(
            userId, roleId, appName, applicationId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def list_group_targets_for_role(
            userId, roleId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            try:
                result = models.Group(
                    response.get_body()
                )
            except Exception as error:
                return None, error

            return (result, None)

        async def remove_group_target_from_role(
            userId, roleId, groupId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def add_group_target_to_role(
            userId, roleId, groupId
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

        async def clear_user_sessions(
            userId, query_params
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

            request, error = self._request_executor.create_request(
                http_method, api_url, body
            )

            if error:
                return None, error

            response, error = await self._request_executor\
                .execute(request)

            if error:
                return None, error
            return response, None

    def format_url(base_string):
        return ''.join(
            [line.strip() for line in base_string.splitlines()]
        )

"""
End of File Generation
"""
