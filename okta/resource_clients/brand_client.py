"""
Copyright 2021 - Present Okta, Inc.

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

from okta.models.brand\
    import Brand
from okta.models.theme_response\
    import ThemeResponse
from okta.models.image_upload_response\
    import ImageUploadResponse
from okta.utils import format_url
from okta.api_client import APIClient


class BrandClient(APIClient):
    """
    A Client object for the Brand resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_brands(
            self,
            keep_empty_params=False
    ):
        """
        List all the brands in your org.
        Args:
        Returns:
            list: Collection of Brand instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands
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
            .execute(request, Brand)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Brand(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_brand(
            self, brandId,
            keep_empty_params=False
    ):
        """
        Fetches a brand by `brandId`
        Args:
            brand_id {str}
        Returns:
            Brand
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}
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
            .execute(request, Brand)

        if error:
            return (None, response, error)

        try:
            result = Brand(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_brand(
            self, brandId, brand,
            keep_empty_params=False
    ):
        """
        Updates a brand by `brandId`
        Args:
            brand_id {str}
            {brand}
        Returns:
            Brand
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}
            """)

        if isinstance(brand, dict):
            body = brand
        else:
            body = brand.as_dict()
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
            .execute(request, Brand)

        if error:
            return (None, response, error)

        try:
            result = Brand(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def list_brand_themes(
            self, brandId,
            keep_empty_params=False
    ):
        """
        List all the themes in your brand
        Args:
            brand_id {str}
        Returns:
            list: Collection of ThemeResponse instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes
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
            .execute(request, ThemeResponse)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(ThemeResponse(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_brand_theme(
            self, brandId, themeId,
            keep_empty_params=False
    ):
        """
        Fetches a theme for a brand
        Args:
            brand_id {str}
            theme_id {str}
        Returns:
            ThemeResponse
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes/{themeId}
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
            .execute(request, ThemeResponse)

        if error:
            return (None, response, error)

        try:
            result = ThemeResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_brand_theme(
            self, brandId, themeId, theme,
            keep_empty_params=False
    ):
        """
        Updates a theme for a brand
        Args:
            brand_id {str}
            theme_id {str}
            {theme}
        Returns:
            ThemeResponse
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes/{themeId}
            """)

        if isinstance(theme, dict):
            body = theme
        else:
            body = theme.as_dict()
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
            .execute(request, ThemeResponse)

        if error:
            return (None, response, error)

        try:
            result = ThemeResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_brand_theme_background_image(
            self, brandId, themeId,
            keep_empty_params=False
    ):
        """
        Deletes a Theme background image
        Args:
            brand_id {str}
            theme_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes/{themeId}
                /background-image
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

    async def upload_brand_theme_background_image(
            self, brandId, themeId, file,
            keep_empty_params=False
    ):
        """
        Updates the background image for your Theme
        Args:
            brand_id {str}
            theme_id {str}
        Returns:
            ImageUploadResponse
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes/{themeId}
                /background-image
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
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ImageUploadResponse)

        if error:
            return (None, response, error)

        try:
            result = ImageUploadResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_brand_theme_favicon(
            self, brandId, themeId,
            keep_empty_params=False
    ):
        """
        Deletes a Theme favicon. The org then uses the Okta def
        ault favicon.
        Args:
            brand_id {str}
            theme_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes/{themeId}/favicon
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

    async def upload_brand_theme_favicon(
            self, brandId, themeId, file,
            keep_empty_params=False
    ):
        """
        Updates the favicon for your theme
        Args:
            brand_id {str}
            theme_id {str}
        Returns:
            ImageUploadResponse
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes/{themeId}/favicon
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
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ImageUploadResponse)

        if error:
            return (None, response, error)

        try:
            result = ImageUploadResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_brand_theme_logo(
            self, brandId, themeId,
            keep_empty_params=False
    ):
        """
        Deletes a Theme logo. The org then uses the Okta defaul
        t logo.
        Args:
            brand_id {str}
            theme_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes/{themeId}/logo
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

    async def upload_brand_theme_logo(
            self, brandId, themeId, file,
            keep_empty_params=False
    ):
        """
        Updates the logo for your Theme
        Args:
            brand_id {str}
            theme_id {str}
        Returns:
            ImageUploadResponse
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/brands/{brandId}/themes/{themeId}/logo
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
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, ImageUploadResponse)

        if error:
            return (None, response, error)

        try:
            result = ImageUploadResponse(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
