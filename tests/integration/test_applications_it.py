import pytest
from tests.mocks import MockOktaClient
# from http import HTTPStatus
import okta.models as models
from okta.client import Client
# import time
# import sys
# import getopt


class TestApplicationsResource:
    """
    Integration Tests for the Applications Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_bookmark_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Bookmark Application Object
        APP_URL = "https://example.com/bookmark.htm"
        APP_LABEL = "AddBookmarkApp"
        app_settings_app = models.BookmarkApplicationSettingsApplication({
            "requestIntegration": False,
            "url": APP_URL
        })
        app_settings = models.BookmarkApplicationSettings({
            "app": app_settings_app
        })
        bookmark_app_obj = models.BookmarkApplication({
            "label": APP_LABEL,
            "settings": app_settings
        })

        # Create App in org
        app, _, err = await client.create_application(bookmark_app_obj)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.BookmarkApplication)

        # Get app and verify details
        found_app, _, err = await client.get_application(app.id)
        assert err is None
        assert found_app.label == APP_LABEL
        assert found_app.sign_on_mode == models.ApplicationSignOnMode.BOOKMARK
        assert found_app.settings.app.request_integration is False
        assert found_app.settings.app.url == APP_URL

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    # @pytest.mark.vcr()
    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_create_basic_auth_app(self):
        # Instantiate Mock Client
        client = MockOktaClient()
        client = Client()

        # Create BasicAuth Application Object
        APP_AUTH_URL = "https://example.com/auth.html"
        APP_URL = "https://example.com/auth.html"
        APP_LABEL = "AddBasicAuthApp"
        app_settings_app = models.BasicApplicationSettingsApplication({
            "authUrl": APP_AUTH_URL,
            "url": APP_URL
        })
        app_settings = models.BasicApplicationSettings({
            "app": app_settings_app
        })
        basic_auth_app_obj = models.BasicAuthApplication({
            "label": APP_LABEL,
            "settings": app_settings
        })

        # Create App in org
        app, _, err = await client.create_application(basic_auth_app_obj)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.BasicAuthApplication)

        # Get app and verify details
        found_app, _, err = await client.get_application(app.id)
        assert err is None
        assert found_app.label == APP_LABEL
        assert found_app.sign_on_mode == \
            models.ApplicationSignOnMode.BASIC_AUTH
        assert found_app.settings.app.url == APP_URL
        assert found_app.settings.app.authUrl == APP_AUTH_URL

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    # @pytest.mark.vcr()
    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_create_SWA_app(self):
        # Instantiate Mock Client
        client = MockOktaClient()
        client = Client()

        # Create Application object and Application in Org
        APP_LABEL = "Test App"
        BUTTON_FIELD = "btn-login"
        PASSWORD_FIELD = "txt-box-password"
        USERNAME_FIELD = "txt-box-username"
        URL = "https://example.com/login.html"
        LOGIN_URL_REGEX = f"^{URL}$"

        swa_app_settings_app = models.SwaApplicationSettingsApplication({
            "buttonField": BUTTON_FIELD,
            "passwordField": PASSWORD_FIELD,
            "usernameField": USERNAME_FIELD,
            "url": URL,
            "loginUrlRegex": LOGIN_URL_REGEX
        })

        swa_app_settings = models.SwaApplicationSettings({
            "app": swa_app_settings_app
        })

        swa_app_obj = models.SwaApplication({
            "label": APP_LABEL,
            "settings": swa_app_settings,
            "signOnMode": models.ApplicationSignOnMode.BROWSER_PLUGIN
        })

        app, _, err = await client.create_application(swa_app_obj)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.SwaApplication)

        # Get app and verify details
        found_app, _, err = await client.get_application(app.id)
        assert err is None
        assert found_app.label == APP_LABEL
        assert found_app.sign_on_mode == \
            models.ApplicationSignOnMode.BROWSER_PLUGIN
        assert found_app.settings.app.button_field == BUTTON_FIELD
        assert found_app.settings.app.password_field == PASSWORD_FIELD
        assert found_app.settings.app.username_field == USERNAME_FIELD
        assert found_app.settings.app.url == URL
        assert found_app.settings.app.login_url_regex == LOGIN_URL_REGEX

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    # @pytest.mark.vcr()
    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_create_SWA_three_app(self):
        # Instantiate Mock Client
        client = MockOktaClient()
        client = Client()

        # Create Application object and Application in Org
        APP_LABEL = "Test App"
        BUTTON_SELECTOR = "#btn-login"
        PASSWORD_SELECTOR = "#txt-box-password"
        USERNAME_SELECTOR = "#txt-box-username"
        TARGET_URL = "https://example.com/login.html"
        LOGIN_URL_REGEX = f"^{TARGET_URL}$"
        EXTRA_FIELD_SELECTOR = ".login"
        EXTRA_FIELD_VALUE = "SOMEVALUE"

        swa_app_settings_app =\
            models.SwaThreeFieldApplicationSettingsApplication({
                "buttonSelector": BUTTON_SELECTOR,
                "passwordSelector": PASSWORD_SELECTOR,
                "userNameSelector": USERNAME_SELECTOR,
                "targetUrl": TARGET_URL,
                "loginUrlRegex": LOGIN_URL_REGEX,
                "extraFieldSelector": EXTRA_FIELD_SELECTOR,
                "extraFieldValue": EXTRA_FIELD_VALUE
            })

        swa_app_settings = models.SwaThreeFieldApplicationSettings({
            "app": swa_app_settings_app
        })

        swa_app_obj = models.SwaThreeFieldApplication({
            "label": APP_LABEL,
            "settings": swa_app_settings,
        })

        app, _, err = await client.create_application(swa_app_obj)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.SwaThreeFieldApplication)

        # Get app and verify details
        found_app, _, err = await client.get_application(app.id)
        assert err is None
        assert found_app.label == APP_LABEL
        assert found_app.sign_on_mode == \
            models.ApplicationSignOnMode.BROWSER_PLUGIN
        assert found_app.settings.app.button_selector == BUTTON_SELECTOR
        assert found_app.settings.app.password_selector == PASSWORD_SELECTOR
        assert found_app.settings.app.username_selector == USERNAME_SELECTOR
        assert found_app.settings.app.target_url == TARGET_URL
        assert found_app.settings.app.login_url_regex == LOGIN_URL_REGEX
        assert found_app.settings.app.extra_field_selector ==\
            EXTRA_FIELD_SELECTOR
        assert found_app.settings.app.extra_field_value == EXTRA_FIELD_VALUE

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    # @pytest.mark.vcr()
    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_create_secure_password_store_app(self):
        # Instantiate Mock Client
        client = MockOktaClient()
        client = Client()

        # Create Application object and Application in Org
        APP_LABEL = "Test App"
        PASSWORD_FIELD = "txt-box-password"
        USERNAME_FIELD = "txt-box-username"
        URL = "https://example.com/login.html"
        OPT_FIELD_1 = "param1"
        OPT_FIELD_1_VALUE = "value1"
        OPT_FIELD_2 = "param2"
        OPT_FIELD_2_VALUE = "value2"
        OPT_FIELD_3 = "param3"
        OPT_FIELD_3_VALUE = "value3"

        sps_app_settings_app =\
            models.SecurePasswordStoreApplicationSettingsApplication({
                "passwordField": PASSWORD_FIELD,
                "usernameField": USERNAME_FIELD,
                "url": URL,
                "optionalField1": OPT_FIELD_1,
                "optionalField1Value": OPT_FIELD_1_VALUE,
                "optionalField2": OPT_FIELD_2,
                "optionalField2Value": OPT_FIELD_2_VALUE,
                "optionalField3": OPT_FIELD_3,
                "optionalField3Value": OPT_FIELD_3_VALUE,
            })

        sps_app_settings = models.SecurePasswordStoreApplicationSettings({
            "app": sps_app_settings_app
        })

        sps_app_obj = models.SecurePasswordStoreApplication({
            "label": APP_LABEL,
            "settings": sps_app_settings,
            # "signOnMode": "SECURE_PASSWORD_STORE"
        })

        print(type(sps_app_obj.sign_on_mode))

        app, _, err = await client.create_application(sps_app_obj)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.SecurePasswordStoreApplication)

        # Get app and verify details
        found_app, _, err = await client.get_application(app.id)
        assert err is None
        assert found_app.label == APP_LABEL
        assert found_app.sign_on_mode == \
            models.ApplicationSignOnMode.SECURE_PASSWORD_STORE
        assert found_app.settings.app.username_field == USERNAME_FIELD
        assert found_app.settings.app.password_field == PASSWORD_FIELD
        assert found_app.settings.app.url == URL
        assert found_app.settings.app.optional_field_1 == OPT_FIELD_1
        assert found_app.settings.app.optional_field_1_value == \
            OPT_FIELD_1_VALUE
        assert found_app.settings.app.optional_field_2 == OPT_FIELD_2
        assert found_app.settings.app.optional_field_2_value == \
            OPT_FIELD_2_VALUE
        assert found_app.settings.app.optional_field_3 == OPT_FIELD_3
        assert found_app.settings.app.optional_field_3_value == \
            OPT_FIELD_3_VALUE

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    # @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_open_id_connect_app(self):
        # Instantiate Mock Client
        client = MockOktaClient()
        client = Client()

        # Create Bookmark Application Object
        APP_LABEL = "AddOpenIdConnectApp"
        CLIENT_URI = "https://example.com/client"
        LOGO_URI = "https://example.com/assets/images/logo-new.png"
        POLICY_URI = "https://example.com/client/policy"
        GRANT_TYPES = [models.OAuthGrantType.AUTHORIZATION_CODE,
                       models.OAuthGrantType.IMPLICIT]
        APP_TYPE = models.OpenIdConnectApplicationType.NATIVE
        POST_LOGOUT_REDIRECT_URIS = ["https://example.com/postlogout",
                                     "myapp://postlogoutcallback"]
        REDIRECT_URIS = ["https://example.com/oauth2/callback",
                         "myapp://callback"]
        RESPONSE_TYPES = [models.OAuthResponseType.TOKEN,
                          models.OAuthResponseType.ID_TOKEN,
                          models.OAuthResponseType.CODE]
        TOS_URL = "https://example.com/client/tos"
        AUTO_KEY_ROTATION = True
        CLIENT_ID = "testclientid12345"
        TOKEN_ENDPOINT_AUTH_METHOD =\
            models.OAuthEndpointAuthenticationMethod.CLIENT_SECRET_POST

        app_settings_client = models.OpenIdConnectApplicationSettingsClient({
            "applicationType": APP_TYPE,
            "clientUri": CLIENT_URI,
            "grantTypes": GRANT_TYPES,
            "logoUri": LOGO_URI,
            "policyUri": POLICY_URI,
            "postLogoutRedirectUris": POST_LOGOUT_REDIRECT_URIS,
            "redirectUris": REDIRECT_URIS,
            "responseTypes": RESPONSE_TYPES,
            "tosUri": TOS_URL
        })
        app_settings = models.OpenIdConnectApplicationSettings({
            "oauthClient": app_settings_client
        })
        app_credentials = models.OAuthApplicationCredentials({
            "oauthClient": models.ApplicationCredentialsOAuthClient({
                "autoKeyRotation": AUTO_KEY_ROTATION,
                "clientId": CLIENT_ID,
                "tokenEndpointAuthMethod": TOKEN_ENDPOINT_AUTH_METHOD
            })
        })
        oidc_app_obj = models.OpenIdConnectApplication({
            "label": APP_LABEL,
            "settings": app_settings,
            "credentials": app_credentials
        })

        # Create App in org
        app, _, err = await client.create_application(oidc_app_obj)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.OpenIdConnectApplication)

        # Get app and verify details
        found_app, _, err = await client.get_application(app.id)
        assert err is None
        assert found_app.label == APP_LABEL
        assert found_app.sign_on_mode ==\
            models.ApplicationSignOnMode.OPENID_CONNECT
        assert found_app.settings.oauth_client.application_type == APP_TYPE
        assert found_app.settings.oauth_client.client_uri == CLIENT_URI
        assert found_app.settings.oauth_client.grant_types == GRANT_TYPES
        assert found_app.settings.oauth_client.logo_uri == LOGO_URI
        assert found_app.settings.oauth_client.policy_uri == POLICY_URI
        assert found_app.settings.oauth_client.post_logout_redirect_uris ==\
            POST_LOGOUT_REDIRECT_URIS
        assert found_app.settings.oauth_client.redirect_uris == REDIRECT_URIS
        assert found_app.settings.oauth_client.response_types == RESPONSE_TYPES
        assert found_app.settings.oauth_client.tos_uri == TOS_URL

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None
