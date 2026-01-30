# flake8: noqa
# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import pytest

from okta import models
from tests.mocks import MockOktaClient


class TestBrandsResource:
    """
    Integration Tests for the Brand and Themes Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_brands(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        assert len(brands) > 0
        for brand in brands:
            assert isinstance(brand, models.BrandWithEmbedded)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_brand(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        brand, _, err = await client.get_brand(brand_id)
        assert err is None
        assert isinstance(brand, models.BrandWithEmbedded)
        assert brand.id == brand_id

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_brand(self, fs):
        client = MockOktaClient(fs)
        custom_privacy_policy_url = "https://www.someHost.com/privacy-policy"

        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id if brands and hasattr(brands[0], "id") else None
        assert brand_id is not None

        brand, _, err = await client.get_brand(brand_id)
        assert err is None
        assert brand and hasattr(brand, "id")
        assert brand.id == brand_id
        assert (
                getattr(brand, "custom_privacy_policy_url", None)
                != custom_privacy_policy_url
        )

        # Create new brand request data
        new_brand = models.BrandRequest(
            **{
                "name": brand.name if brand.name else "Okta",
                "agreeToCustomPrivacyPolicy": True,
                "customPrivacyPolicyUrl": custom_privacy_policy_url,
                "removePoweredByOkta": getattr(brand, "remove_powered_by_okta", None),
                "locale": getattr(brand, "locale", None),
            }
        )

        try:
            updated_brand, _, err = await client.replace_brand(brand_id, new_brand)
            assert err is None
            assert updated_brand and hasattr(updated_brand, "id")
            assert brand.id == updated_brand.id
            assert (
                    getattr(updated_brand, "custom_privacy_policy_url", None)
                    == custom_privacy_policy_url
            )
        finally:
            # Create restore brand request
            restore_brand = models.BrandRequest(
                **{
                    "name": brand.name if brand.name else "Okta",
                    "agreeToCustomPrivacyPolicy": getattr(
                        brand, "agree_to_custom_privacy_policy", False
                    ),
                    "customPrivacyPolicyUrl": getattr(
                        brand, "custom_privacy_policy_url", None
                    ),
                    "removePoweredByOkta": getattr(
                        brand, "remove_powered_by_okta", None
                    ),
                    "locale": getattr(brand, "locale", None),
                }
            )

            # restore previous brand settings
            _, _, err = await client.replace_brand(brand_id, restore_brand)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_brand_themes(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        assert len(themes) > 0
        for theme in themes:
            assert isinstance(theme, models.ThemeResponse)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_brand_theme(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        theme_id = themes[0].id
        theme, _, err = await client.get_brand_theme(brand_id, theme_id)
        assert err is None
        assert isinstance(theme, models.ThemeResponse)
        assert isinstance(
            theme.email_template_touch_point_variant,
            models.EmailTemplateTouchPointVariant,
        )
        assert isinstance(
            theme.end_user_dashboard_touch_point_variant,
            models.EndUserDashboardTouchPointVariant,
        )
        assert isinstance(
            theme.error_page_touch_point_variant, models.ErrorPageTouchPointVariant
        )
        assert isinstance(
            theme.sign_in_page_touch_point_variant, models.SignInPageTouchPointVariant
        )

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_brand_theme(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        theme_id = themes[0].id
        theme, _, err = await client.get_brand_theme(brand_id, theme_id)
        assert err is None

        update_theme_params = {
            "primaryColorHex": "#ababab",
            "secondaryColorHex": "#ebebeb",
            "emailTemplateTouchPointVariant": models.EmailTemplateTouchPointVariant(
                "OKTA_DEFAULT"
            ),
            "endUserDashboardTouchPointVariant": models.EndUserDashboardTouchPointVariant(
                "OKTA_DEFAULT"
            ),
            "signInPageTouchPointVariant": models.SignInPageTouchPointVariant(
                "OKTA_DEFAULT"
            ),
            "errorPageTouchPointVariant": models.ErrorPageTouchPointVariant(
                "OKTA_DEFAULT"
            ),
        }
        try:
            updated_theme, _, err = await client.replace_brand_theme(
                brand_id, theme_id, update_theme_params
            )
            assert err is None
            assert updated_theme.primary_color_hex == "#ababab"
            assert updated_theme.secondary_color_hex == "#ebebeb"
            assert updated_theme.email_template_touch_point_variant == "OKTA_DEFAULT"
            assert (
                    updated_theme.end_user_dashboard_touch_point_variant == "OKTA_DEFAULT"
            )
        finally:
            # restore previous theme settings
            restore_theme_params = {
                "primaryColorHex": theme.primary_color_hex,
                "secondaryColorHex": theme.secondary_color_hex,
                "emailTemplateTouchPointVariant": theme.email_template_touch_point_variant,
                "endUserDashboardTouchPointVariant": theme.end_user_dashboard_touch_point_variant,
                "signInPageTouchPointVariant": theme.sign_in_page_touch_point_variant,
                "errorPageTouchPointVariant": theme.error_page_touch_point_variant,
            }
            _, _, err = await client.replace_brand_theme(
                brand_id, theme_id, restore_theme_params
            )
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_brand_theme_background_image(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        theme_id = themes[0].id
        _, _, err = await client.delete_brand_theme_background_image(brand_id, theme_id)
        assert err is None

    # skip test until solution with writing cassette is found
    @pytest.mark.skip
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_upload_brand_theme_background_image(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        theme_id = themes[0].id
        try:
            image = open(f"tests/integration/data/brand_theme_background.png", "rb")
            image_upload_resp, _, err = (
                await client.upload_brand_theme_background_image(
                    brand_id, theme_id, image
                )
            )
            assert err is None
            assert isinstance(image_upload_resp, models.ImageUploadResponse)
        finally:
            _, _, err = await client.delete_brand_theme_background_image(
                brand_id, theme_id
            )
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_brand_theme_favicon(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        theme_id = themes[0].id
        _, _, err = await client.delete_brand_theme_favicon(brand_id, theme_id)
        assert err is None

    # skip test until solution with writing cassette is found
    @pytest.mark.skip
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_upload_brand_theme_favicon(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        theme_id = themes[0].id
        try:
            image = open(f"tests/integration/data/brand_theme_favicon.ico", "rb")
            image_upload_resp, _, err = await client.upload_brand_theme_favicon(
                brand_id, theme_id, image
            )
            assert err is None
            assert isinstance(image_upload_resp, models.ImageUploadResponse)
        finally:
            _, _, err = await client.delete_brand_theme_favicon(brand_id, theme_id)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_brand_theme_logo(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        theme_id = themes[0].id
        _, _, err = await client.delete_brand_theme_logo(brand_id, theme_id)
        assert err is None

    # skip test until solution with writing cassette is found
    @pytest.mark.skip
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_upload_brand_theme_logo(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        themes, _, err = await client.list_brand_themes(brand_id)
        assert err is None
        theme_id = themes[0].id
        try:
            image = open(f"tests/integration/data/brand_theme_logo.png", "rb")
            image_upload_resp, _, err = await client.upload_brand_theme_logo(
                brand_id, theme_id, image
            )
            assert err is None
            assert isinstance(image_upload_resp, models.ImageUploadResponse)
        finally:
            _, _, err = await client.delete_brand_theme_logo(brand_id, theme_id)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_email_templates(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        email_templates, _, err = await client.list_email_templates(brand_id)
        assert err is None
        for template in email_templates:
            assert isinstance(template, models.EmailTemplateResponse)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_email_template(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        email_templates, _, err = await client.list_email_templates(brand_id)
        assert err is None
        template = email_templates[0]
        received_template, _, err = await client.get_email_template(
            brand_id, template.name
        )
        assert isinstance(received_template, models.EmailTemplateResponse)
        assert template.name == received_template.name

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_email_template_customizations(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        email_templates, _, err = await client.list_email_templates(brand_id)
        assert err is None
        template = email_templates[0]

        # create email template customization
        email_template_customization_request = models.EmailCustomization(
            **{
                "language": "en",
                "subject": "Welcome to ${org.name}!",
                "body": '<!DOCTYPE html><html><body><p>Hello ${user.profile.firstName}. <a href="${activationLink}">Activate '
                        'account</a></p></body></html>',
                "isDefault": False,
            }
        )
        customization, _, err = await client.create_email_customization(
            brand_id, template.name, email_template_customization_request
        )
        assert err is None
        assert isinstance(customization, models.EmailCustomization)

        customizations, _, err = await client.list_email_customizations(
            brand_id, template.name
        )
        assert err is None
        assert len(customizations) == 1
        for template_customization in customizations:
            assert isinstance(template_customization, models.EmailCustomization)

        # clear all customizations
        _, _, err = await client.delete_email_customization(
            brand_id, template.name, customization.id
        )
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_delete_email_template_customizations(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        email_templates, _, err = await client.list_email_templates(brand_id)
        assert err is None
        template = email_templates[0]

        email_template_customization_request = models.EmailCustomization(
            **{
                "language": "fr",
                "subject": "Bienvenue dans ${org.name}!",
                "body": '<!DOCTYPE html><html><body><p>Bonjour ${user.profile.firstName}. <a href="${activationLink}">Activer '
                        'le compte</a></p></body></html>',
                "isDefault": False,
            }
        )
        customization_1, _, err = await client.create_email_customization(
            brand_id, template.name, email_template_customization_request
        )
        assert err is None
        assert isinstance(customization_1, models.EmailCustomization)
        assert customization_1.language == "fr"

        # create 2nd customization as it is possible to delete only non-default customization
        email_template_customization_request = models.EmailCustomization(
            **{
                "language": "en",
                "subject": "Welcome to ${org.name}!",
                "body": '<!DOCTYPE html><html><body><p>Hello ${user.profile.firstName}. <a href="${activationLink}">Activate '
                        'account</a></p></body></html>',
                "isDefault": False,
            }
        )
        customization_2, _, err = await client.create_email_customization(
            brand_id, template.name, email_template_customization_request
        )
        assert err is None
        assert isinstance(customization_2, models.EmailCustomization)
        assert customization_2.language == "en"

        _, _, err = await client.delete_email_customization(
            brand_id, template.name, customization_1.id
        )
        assert err is None

        # clear all customizations
        _, _, err = await client.delete_email_customization(
            brand_id, template.name, customization_2.id
        )
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_update_email_template_customization(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        email_templates, _, err = await client.list_email_templates(brand_id)
        assert err is None
        template = email_templates[0]

        email_template_customization_request = models.EmailCustomization(
            **{
                "language": "fr",
                "subject": "Bienvenue dans ${org.name}!",
                "body": '<!DOCTYPE html><html><body><p>Bonjour ${user.profile.firstName}. <a href="${activationLink}">Activer '
                        'le compte</a></p></body></html>',
                "isDefault": True,
            }
        )
        customization, _, err = await client.create_email_customization(
            brand_id, template.name, email_template_customization_request
        )
        assert err is None
        assert isinstance(customization, models.EmailCustomization)
        assert customization.language == "fr"

        # update customization
        email_template_customization_request = models.EmailCustomization(
            **{
                "language": "en",
                "subject": "Welcome to ${org.name}!",
                "body": '<!DOCTYPE html><html><body><p>Hello ${user.profile.firstName}. <a href="${activationLink}">Activate '
                        'account</a></p></body></html>',
                "isDefault": True,
            }
        )
        customization, _, err = await client.replace_email_customization(
            brand_id,
            template.name,
            customization.id,
            email_template_customization_request,
        )
        assert err is None
        assert customization.language == "en"

        # get customization
        customization, _, err = await client.get_email_customization(
            brand_id, template.name, customization.id
        )
        assert err is None
        assert customization.language == "en"

        # clear all customizations
        _, _, err = await client.delete_email_customization(
            brand_id, template.name, customization.id
        )
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_email_template_customization_preview(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        email_templates, _, err = await client.list_email_templates(brand_id)
        assert err is None
        template = email_templates[0]

        # Create a customization first
        email_template_customization_request = models.EmailCustomization(
            **{
                "language": "en",
                "subject": "Hello, welcome to ${org.name}!",
                "body": '<!DOCTYPE html><html><body><p>Hello ${user.profile.firstName}. <a href="${activationLink}">Activate '
                        'account</a></p></body></html>',
            }
        )

        customization, _, err = await client.create_email_customization(
            brand_id, template.name, email_template_customization_request
        )
        assert err is None

        # Get the created customization
        retrieved_customization, _, err = await client.get_customization_preview(
            brand_id, template.name, customization.id
        )
        assert err is None
        assert retrieved_customization.subject == "Hello, welcome to test!"

        # Now delete the customization using the correct ID
        _, _, err = await client.delete_email_customization(
            brand_id, template.name, customization.id
        )
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_brand_lifecycle(self, fs):
        """
        Test the complete lifecycle of Brand operations

        This test covers:
        - Creating a new brand
        - Listing brands and verifying the created brand
        - Getting a specific brand
        - Replacing/updating a brand
        - Listing brand domains
        - Deleting the brand

        This comprehensive test increases coverage for:
        - create_brand()
        - list_brands() with pagination
        - get_brand() with expand parameter
        - replace_brand()
        - list_brand_domains()
        - delete_brand()
        """
        client = MockOktaClient(fs)

        brand_id = None

        try:
            # ===== CREATE BRAND =====
            print("\n=== Creating Brand ===")

            create_brand_request = models.CreateBrandRequest(
                name="Python SDK Test Brand"
            )

            created_brand, _, err = await client.create_brand(create_brand_request)

            assert err is None, f"Failed to create brand: {err}"
            assert created_brand is not None
            assert isinstance(created_brand, models.Brand)
            assert created_brand.name == "Python SDK Test Brand"

            brand_id = created_brand.id
            print(f"Created brand: {brand_id}")
            print(f"  Name: {created_brand.name}")

            # ===== LIST BRANDS =====
            print("\n=== Listing Brands ===")

            brands_list, _, err = await client.list_brands()

            assert err is None, f"Failed to list brands: {err}"
            assert brands_list is not None
            assert isinstance(brands_list, list)
            assert len(brands_list) > 0

            # Verify our created brand is in the list
            brand_ids = [brand.id for brand in brands_list]
            assert brand_id in brand_ids, f"Created brand {brand_id} not found in list"

            print(f"Found {len(brands_list)} brand(s)")

            # ===== LIST BRANDS WITH PAGINATION =====
            print("\n=== Testing List with Pagination ===")

            paginated_brands, _, err = await client.list_brands(limit=10)

            assert err is None, f"Failed to list brands with limit: {err}"
            assert paginated_brands is not None
            assert isinstance(paginated_brands, list)
            print(f"Paginated list returned {len(paginated_brands)} brand(s)")

            # ===== GET BRAND =====
            print("\n=== Getting Specific Brand ===")

            retrieved_brand, _, err = await client.get_brand(brand_id)

            assert err is None, f"Failed to get brand: {err}"
            assert retrieved_brand is not None
            assert isinstance(retrieved_brand, models.BrandWithEmbedded)
            assert retrieved_brand.id == brand_id

            print(f"Retrieved brand: {retrieved_brand.id}")

            # ===== GET BRAND WITH EXPAND =====
            print("\n=== Getting Brand with Expand ===")

            expanded_brand, _, err = await client.get_brand(brand_id, expand=["domains"])

            assert err is None, f"Failed to get brand with expand: {err}"
            assert expanded_brand is not None
            print(f"Retrieved brand with expand parameter")

            # ===== REPLACE (UPDATE) BRAND =====
            print("\n=== Replacing Brand ===")

            # Create updated brand request with privacy policy
            updated_brand_request = models.BrandRequest(
                name="Python SDK Test Brand",
                agree_to_custom_privacy_policy=True,
                custom_privacy_policy_url="https://example.com/privacy"
            )

            replaced_brand, _, err = await client.replace_brand(brand_id, updated_brand_request)

            assert err is None, f"Failed to replace brand: {err}"
            assert replaced_brand is not None
            assert replaced_brand.id == brand_id
            assert replaced_brand.custom_privacy_policy_url == "https://example.com/privacy"

            print(f"Replaced brand successfully")
            print(f"  Privacy URL: {replaced_brand.custom_privacy_policy_url}")

            # ===== LIST BRAND DOMAINS =====
            print("\n=== Listing Brand Domains ===")

            brand_domains, _, err = await client.list_brand_domains(brand_id)

            assert err is None, f"Failed to list brand domains: {err}"
            assert brand_domains is not None
            assert isinstance(brand_domains, models.BrandDomains)

            print(f"Successfully retrieved brand domains")

            print("\n=== Test completed successfully ===")

        except Exception as e:
            print(f"\n!!! Test failed with error: {e}")
            raise

        finally:
            # ===== DELETE BRAND =====
            if brand_id:
                print("\n=== Cleanup: Deleting Brand ===")

                try:
                    _, _, err = await client.delete_brand(brand_id)

                    if err:
                        print(f"Warning: Could not delete brand: {err}")
                    else:
                        print(f"Deleted brand successfully")

                        # Verify deletion by trying to get the brand
                        verify_brand, _, verify_err = await client.get_brand(brand_id)

                        if verify_err:
                            print(f"Verified brand is deleted (404 expected): {verify_err}")

                except Exception as e:
                    print(f"Exception deleting brand: {e}")

            print("=== Cleanup completed ===")

