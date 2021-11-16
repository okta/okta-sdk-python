import copy
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
            assert isinstance(brand, models.Brand)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_brand(self, fs):
        client = MockOktaClient(fs)
        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        brand, _, err = await client.get_brand(brand_id)
        assert err is None
        assert isinstance(brand, models.Brand)
        assert brand.id == brand_id

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_brand(self, fs):
        client = MockOktaClient(fs)
        custom_privacy_policy_url = 'https://www.someHost.com/privacy-policy'

        brands, _, err = await client.list_brands()
        assert err is None
        brand_id = brands[0].id
        brand, _, err = await client.get_brand(brand_id)
        assert err is None
        assert brand.id == brand_id
        assert brand.custom_privacy_policy_url != custom_privacy_policy_url

        new_brand = copy.deepcopy(brand)
        new_brand.agree_to_custom_privacy_policy = True
        new_brand.custom_privacy_policy_url = 'https://www.someHost.com/privacy-policy'

        try:
            updated_brand, _, err = await client.update_brand(brand_id, new_brand)
            assert err is None
            assert isinstance(updated_brand, models.Brand)
            assert brand.id == updated_brand.id
            assert updated_brand.custom_privacy_policy_url == custom_privacy_policy_url
        finally:
            # restore previous brand settings
            _, _, err = await client.update_brand(brand_id, brand)
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
        assert isinstance(theme.email_template_touch_point_variant,
                          models.EmailTemplateTouchPointVariant)
        assert isinstance(theme.end_user_dashboard_touch_point_variant,
                          models.EndUserDashboardTouchPointVariant)
        assert isinstance(theme.error_page_touch_point_variant,
                          models.ErrorPageTouchPointVariant)
        assert isinstance(theme.sign_in_page_touch_point_variant,
                          models.SignInPageTouchPointVariant)

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

        update_theme_params = {'primaryColorHex': '#ababab',
                               'secondaryColorHex': '#ebebeb',
                               'emailTemplateTouchPointVariant': models.EmailTemplateTouchPointVariant('OKTA_DEFAULT'),
                               'endUserDashboardTouchPointVariant': models.EndUserDashboardTouchPointVariant('OKTA_DEFAULT'),
                               'signInPageTouchPointVariant': models.SignInPageTouchPointVariant('OKTA_DEFAULT'),
                               'errorPageTouchPointVariant': models.ErrorPageTouchPointVariant('OKTA_DEFAULT')}
        try:
            updated_theme, _, err = await client.update_brand_theme(brand_id, theme_id, update_theme_params)
            assert err is None
            assert updated_theme.primary_color_hex == '#ababab'
            assert updated_theme.secondary_color_hex == '#ebebeb'
            assert updated_theme.email_template_touch_point_variant == 'OKTA_DEFAULT'
            assert updated_theme.end_user_dashboard_touch_point_variant == 'OKTA_DEFAULT'
        finally:
            # restore previous theme settings
            restore_theme_params = {'primaryColorHex': theme.primary_color_hex,
                                    'secondaryColorHex': theme.secondary_color_hex,
                                    'emailTemplateTouchPointVariant': theme.email_template_touch_point_variant,
                                    'endUserDashboardTouchPointVariant': theme.end_user_dashboard_touch_point_variant,
                                    'signInPageTouchPointVariant': theme.sign_in_page_touch_point_variant,
                                    'errorPageTouchPointVariant': theme.error_page_touch_point_variant}
            _, _, err = await client.update_brand_theme(brand_id, theme_id, restore_theme_params)
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
        _, err = await client.delete_brand_theme_background_image(brand_id, theme_id)
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
            image = open(f'tests/integration/data/brand_theme_background.png', 'rb')
            image_upload_resp, _, err = await client.upload_brand_theme_background_image(brand_id, theme_id, image)
            assert err is None
            assert isinstance(image_upload_resp, models.ImageUploadResponse)
        finally:
            _, err = await client.delete_brand_theme_background_image(brand_id, theme_id)
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
        _, err = await client.delete_brand_theme_favicon(brand_id, theme_id)
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
            image = open(f'tests/integration/data/brand_theme_favicon.ico', 'rb')
            image_upload_resp, _, err = await client.upload_brand_theme_favicon(brand_id, theme_id, image)
            assert err is None
            assert isinstance(image_upload_resp, models.ImageUploadResponse)
        finally:
            _, err = await client.delete_brand_theme_favicon(brand_id, theme_id)
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
        _, err = await client.delete_brand_theme_logo(brand_id, theme_id)
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
            image = open(f'tests/integration/data/brand_theme_logo.png', 'rb')
            image_upload_resp, _, err = await client.upload_brand_theme_logo(brand_id, theme_id, image)
            assert err is None
            assert isinstance(image_upload_resp, models.ImageUploadResponse)
        finally:
            _, err = await client.delete_brand_theme_logo(brand_id, theme_id)
            assert err is None
