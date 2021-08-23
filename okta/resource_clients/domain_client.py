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

from okta.models.domain_list_response\
    import DomainListResponse
from okta.models.domain\
    import Domain
from okta.utils import format_url
from okta.api_client import APIClient


class DomainClient(APIClient):
    """
    A Client object for the Domain resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_domains(
            self,
            keep_empty_params=False
    ):
        """
        List all verified custom Domains for the org.
        Args:
        Returns:
            DomainListResponse
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/domains
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, DomainListResponse)

        if error:
            return (None, response, error)

        try:
            result = DomainListResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_domain(
            self, domain,
            keep_empty_params=False
    ):
        """
        Creates your domain.
        Args:
            {domain}
        Returns:
            Domain
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/domains
            """)

        if isinstance(domain, dict):
            body = domain
        else:
            body = domain.as_dict()
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
            .execute(request, Domain)

        if error:
            return (None, response, error)

        try:
            result = Domain(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_domain(
            self, domainId,
            keep_empty_params=False
    ):
        """
        Deletes a Domain by `id`.
        Args:
            domain_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/domains/{domainId}
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

    async def get_domain(
            self, domainId,
            keep_empty_params=False
    ):
        """
        Fetches a Domain by `id`.
        Args:
            domain_id {str}
        Returns:
            Domain
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/domains/{domainId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Domain)

        if error:
            return (None, response, error)

        try:
            result = Domain(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_certificate(
            self, domainId, domain_certificate,
            keep_empty_params=False
    ):
        """
        Creates the Certificate for the Domain.
        Args:
            domain_id {str}
            {domain_certificate}
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/domains/{domainId}/certificate
            """)

        if isinstance(domain_certificate, dict):
            body = domain_certificate
        else:
            body = domain_certificate.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

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

    async def verify_domain(
            self, domainId,
            keep_empty_params=False
    ):
        """
        Verifies the Domain by `id`.
        Args:
            domain_id {str}
        Returns:
            Domain
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/domains/{domainId}/verify
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Domain)

        if error:
            return (None, response, error)

        try:
            result = Domain(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
