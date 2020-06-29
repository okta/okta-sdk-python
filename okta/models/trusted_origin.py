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


class TrustedOrigin:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.created = config["created"]
            self.created_by = config["createdBy"]
            self.id = config["id"]
            self.last_updated = config["lastUpdated"]
            self.last_updated_by = config["lastUpdatedBy"]
            self.name = config["name"]
            self.origin = config["origin"]
            self.scopes = config["scopes"]
            self.status = config["status"]
        else:
            self.links = None
            self.created = None
            self.created_by = None
            self.id = None
            self.last_updated = None
            self.last_updated_by = None
            self.name = None
            self.origin = None
            self.scopes = None
            self.status = None

    
    async def create_origin(
            self, trusted_origin
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
            result = TrustedOrigin(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def get_origin(
            self, trustedOriginId
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
            result = TrustedOrigin(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def update_origin(
            self, trustedOriginId, trusted_origin
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
            result = TrustedOrigin(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def delete_origin(
            self, trustedOriginId
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

    
    async def list_origins(
            self, query_params
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
            result.append(TrustedOrigin(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def activate_origin(
            self, trustedOriginId
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
            result = TrustedOrigin(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    
    async def deactivate_origin(
            self, trustedOriginId
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
            result = TrustedOrigin(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation
