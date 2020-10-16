import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from okta.errors.okta_api_error import OktaAPIError


class TestApplicationsResource:
    """
    Integration Tests for the Applications Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_bookmark_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_basic_auth_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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
        assert found_app.settings.app.auth_url == APP_AUTH_URL

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_SWA_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_SWA_three_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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
        assert found_app.settings.app.user_name_selector == USERNAME_SELECTOR
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

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_secure_password_store_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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
        })

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

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_open_id_connect_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create OIDC Application Object
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
        assert found_app.settings.oauth_client.post_logout_redirect_uris ==\
            POST_LOGOUT_REDIRECT_URIS
        assert found_app.settings.oauth_client.redirect_uris == REDIRECT_URIS
        assert found_app.settings.oauth_client.response_types == RESPONSE_TYPES

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_apps(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create OIDC Application Object
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

        # Deactivate App
        _, err = await client.deactivate_application(app.id)
        assert err is None

        # List inactive apps
        query_params_list = {"filter": "status eq \"INACTIVE\""}
        apps_list, _, err = await client.list_applications(query_params_list)
        assert err is None
        assert len(apps_list) == 1
        assert apps_list[0].id == app.id

        # Delete created app
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_deactivate_delete_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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
        query_params_create = {"activate": False}
        app, _, err = await client.create_application(bookmark_app_obj,
                                                      query_params_create)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.BookmarkApplication)
        assert app.status == "INACTIVE"

        # Activate App
        _, err = await client.activate_application(app.id)
        assert err is None

        # 2 second sleep for backend to update

        # Get app and verify details
        found_app, _, err = await client.get_application(app.id)
        assert err is None
        assert found_app.label == APP_LABEL
        assert found_app.status == "ACTIVE"

        # Try to delete active app - returns exception
        _, err = await client.delete_application(app.id)
        assert isinstance(err, OktaAPIError)

        # De-activate app
        _, err = await client.deactivate_application(app.id)
        assert err is None

        # Delete app
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_assign_user_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # Create Password
        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        # Create User Credentials
        user_creds = models.UserCredentials({
            "password": password
        })

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Get"
        user_profile.email = "John.Doe-Get@example.com"
        user_profile.login = "John.Doe-Get@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": True}

        # Create User
        user, resp, err = await client.create_user(
            create_user_req, query_params_create)
        assert err is None

        # Create app user
        app_user_credentials_password = models.AppUserPasswordCredential({
            "value": "Password150kta"
        })
        app_user_credentials = models.AppUserCredentials({
            "password": app_user_credentials_password,
            "userName": user.profile.email
        })
        app_user = models.AppUser({
            "credentials": app_user_credentials,
            "id": user.id
        })

        # Assign
        created_app_user, _, err = await\
            client.assign_user_to_application(app.id, app_user)
        assert err is None
        assert isinstance(created_app_user, models.AppUser)
        assert created_app_user.scope == "USER"
        assert created_app_user.status == "ACTIVE"
        assert created_app_user.sync_state == "DISABLED"

        # Deactivate and Delete User
        _, err = await client.deactivate_user(user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_list_assign_users_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # Create Password
        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        # Create User Credentials
        user_creds = models.UserCredentials({
            "password": password
        })

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Get"
        user_profile.email = "John.Doe-Get@example.com"
        user_profile.login = "John.Doe-Get@example.com"

        user_profile_2 = models.UserProfile()
        user_profile_2.first_name = "John"
        user_profile_2.last_name = "Doe-List"
        user_profile_2.email = "John.Doe-List@example.com"
        user_profile_2.login = "John.Doe-List@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })
        create_user_req_2 = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile_2
        })

        query_params_create = {"activate": True}

        # Create Users
        user, resp, err = await client.create_user(
            create_user_req, query_params_create)
        assert err is None

        user_2, resp, err = await client.create_user(
            create_user_req_2, query_params_create)
        assert err is None

        # Create app users
        app_user_credentials_password = models.AppUserPasswordCredential({
            "value": "Password150kta"
        })
        app_user_credentials = models.AppUserCredentials({
            "password": app_user_credentials_password,
            "userName": user.profile.email
        })
        app_user = models.AppUser({
            "credentials": app_user_credentials,
            "id": user.id
        })

        app_user_credentials_password = models.AppUserPasswordCredential({
            "value": "Password150kta"
        })
        app_user_credentials_2 = models.AppUserCredentials({
            "password": app_user_credentials_password,
            "userName": user_2.profile.email
        })
        app_user_2 = models.AppUser({
            "credentials": app_user_credentials_2,
            "id": user_2.id
        })

        # Assign
        created_app_user, _, err = await\
            client.assign_user_to_application(app.id, app_user)
        assert err is None
        assert isinstance(created_app_user, models.AppUser)

        created_app_user_2, _, err = await\
            client.assign_user_to_application(app.id, app_user_2)
        assert err is None
        assert isinstance(created_app_user_2, models.AppUser)

        # Get one user and verify details
        found_app_user, _, err = await\
            client.get_application_user(app.id, user.id)
        assert err is None
        assert found_app_user.id == user.id
        assert found_app_user.scope == "USER"

        # List users in app and verify details
        app_user_list, _, err = await client.list_application_users(app.id)
        assert err is None
        assert len(app_user_list) == 2
        assert next((app_usr for app_usr in app_user_list
                     if app_usr.credentials.user_name == user.profile.email))
        assert next((app_usr for app_usr in app_user_list
                     if app_usr.credentials.user_name == user_2.profile.email))

        # Deactivate and Delete Users
        _, err = await client.deactivate_user(user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await client.deactivate_user(user_2.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(user_2.id)
        assert err is None

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_app_update_assigned_user(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # Create Password
        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        # Create User Credentials
        user_creds = models.UserCredentials({
            "password": password
        })

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Get"
        user_profile.email = "John.Doe-Get@example.com"
        user_profile.login = "John.Doe-Get@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": True}

        # Create User
        user, resp, err = await client.create_user(
            create_user_req, query_params_create)
        assert err is None

        # Create app user
        app_user_credentials_password = models.AppUserPasswordCredential({
            "value": "Password150kta"
        })
        app_user_credentials = models.AppUserCredentials({
            "password": app_user_credentials_password,
            "userName": user.profile.email
        })
        app_user = models.AppUser({
            "credentials": app_user_credentials,
            "id": user.id
        })

        # Assign
        created_app_user, _, err = await\
            client.assign_user_to_application(app.id, app_user)
        assert err is None
        assert isinstance(created_app_user, models.AppUser)
        assert created_app_user.scope == "USER"
        assert created_app_user.status == "ACTIVE"
        assert created_app_user.sync_state == "DISABLED"

        # Retrieve
        found_app_user, _, err = await\
            client.get_application_user(app.id, user.id)
        assert err is None
        assert found_app_user.id == user.id

        # Update
        UPDATED_USER_NAME = "JohnJohnJohn"
        UPDATED_PASSWORD = "Password12345!"
        found_app_user.credentials.user_name = UPDATED_USER_NAME
        found_app_user.credentials.password = models.AppUserPasswordCredential(
            {"value": UPDATED_PASSWORD})
        updated_app_user, _, err = await \
            client.update_application_user(app.id, user.id, found_app_user)
        assert updated_app_user.credentials.user_name == UPDATED_USER_NAME

        # Deactivate and Delete User
        _, err = await client.deactivate_user(user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_app_remove_assigned_user(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # Create Password
        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        # Create User Credentials
        user_creds = models.UserCredentials({
            "password": password
        })

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Get"
        user_profile.email = "John.Doe-Get@example.com"
        user_profile.login = "John.Doe-Get@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": True}

        # Create User
        user, resp, err = await client.create_user(
            create_user_req, query_params_create)
        assert err is None

        # Create app user
        app_user_credentials_password = models.AppUserPasswordCredential({
            "value": "Password150kta"
        })
        app_user_credentials = models.AppUserCredentials({
            "password": app_user_credentials_password,
            "userName": user.profile.email
        })
        app_user = models.AppUser({
            "credentials": app_user_credentials,
            "id": user.id
        })

        # Assign
        created_app_user, _, err = await\
            client.assign_user_to_application(app.id, app_user)
        assert err is None
        assert isinstance(created_app_user, models.AppUser)
        assert created_app_user.scope == "USER"
        assert created_app_user.status == "ACTIVE"
        assert created_app_user.sync_state == "DISABLED"

        # Retrieve
        found_app_user, _, err = await\
            client.get_application_user(app.id, user.id)
        assert err is None
        assert found_app_user.id == user.id

        # Remove
        _, err = await client.delete_application_user(app.id, user.id)
        assert err is None

        # Ensure user is not in list
        users_assigned, _, err = await client.list_application_users(app.id)
        assert err is None
        assert len(users_assigned) == 0

        # Deactivate and Delete User
        _, err = await client.deactivate_user(user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_assign_group_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Assign app and group
        assign_ag_req = models.ApplicationGroupAssignment({
            "priority": 0,
            "applicationId": app.id,
            "groupId": group.id
        })

        assign_app_group, _, err = await \
            client.create_application_group_assignment(
                app.id, group.id, assign_ag_req)
        assert err is None

        # 3 second sleep for backend to update

        found_app_group, _, err = await \
            client.get_application_group_assignment(app.id, group.id)
        assert err is None
        assert found_app_group.id == assign_app_group.id
        assert found_app_group.priority == 0

        # Remove and deactivate+delete
        _, err = await client.delete_group(group.id)
        assert err is None

        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_assign_group_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        GROUP_NAME_2 = "Group-Target-Test-2"
        group_profile_2 = models.GroupProfile({
            "name": GROUP_NAME_2
        })
        group_obj_2 = models.Group({
            "profile": group_profile_2
        })

        # Create Groups
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)
        group_2, _, err = await client.create_group(group_obj_2)
        assert err is None
        assert isinstance(group, models.Group)

        # Assign app and group
        assign_ag_req = models.ApplicationGroupAssignment({
            "priority": 0,
            "applicationId": app.id,
            "groupId": group.id
        })
        assign_ag_req_2 = models.ApplicationGroupAssignment({
            "priority": 0,
            "applicationId": app.id,
            "groupId": group_2.id
        })

        assign_app_group, _, err = await \
            client.create_application_group_assignment(
                app.id, group.id, assign_ag_req)
        assert err is None
        assign_app_group_2, _, err = await \
            client.create_application_group_assignment(
                app.id, group_2.id, assign_ag_req_2)
        assert err is None

        # 3 second sleep for backend to update

        group_assign_list, _, err = await \
            client.list_application_group_assignments(app.id)
        assert err is None
        assert len(group_assign_list) == 2
        assert next(
            (grp for grp in group_assign_list
             if grp.id == assign_app_group.id))
        assert next(
            (grp for grp in group_assign_list
             if grp.id == assign_app_group_2.id))

        # Remove and deactivate+delete
        _, err = await client.delete_group(group.id)
        assert err is None
        _, err = await client.delete_group(group_2.id)
        assert err is None

        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_remove_assign_group_app(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Assign app and group
        assign_ag_req = models.ApplicationGroupAssignment({
            "priority": 0,
            "applicationId": app.id,
            "groupId": group.id
        })

        assign_app_group, _, err = await \
            client.create_application_group_assignment(
                app.id, group.id, assign_ag_req)
        assert err is None

        # 3 second sleep for backend to update

        found_app_group, _, err = await \
            client.get_application_group_assignment(app.id, group.id)
        assert err is None
        assert found_app_group.id == assign_app_group.id
        assert found_app_group.priority == 0

        # Remove
        _, err = await \
            client.delete_application_group_assignment(app.id, group.id)
        assert err is None

        # Verify gone
        group_assign_list, _, err = await \
            client.list_application_group_assignments(app.id)
        assert err is None
        assert len(group_assign_list) == 0

        # Remove and deactivate+delete
        _, err = await client.delete_group(group.id)
        assert err is None

        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_app_keys(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # List app keys
        app_keys, _, err = await client.list_application_keys(app.id)
        assert err is None
        assert len(app_keys) == 1

        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_app_keys(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # List app keys
        app_keys, _, err = await client.list_application_keys(app.id)
        assert err is None
        assert len(app_keys) == 1

        # Get default key
        default_key = app_keys[0]

        # Find key and verify details
        found_key, _, err = await \
            client.get_application_key(app.id, default_key.kid)
        assert err is None
        assert found_key.kid == default_key.kid
        assert found_key.created == default_key.created
        assert found_key.expires_at == default_key.expires_at
        assert found_key.x_5_c == default_key.x_5_c

        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_generate_app_key(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        # Generate key
        query_params_generate = {"validityYears": 2}
        generated, _, err = await\
            client.generate_application_key(app.id, query_params_generate)
        assert err is None

        # List app keys
        found, _, err = await\
            client.get_application_key(app.id, generated.kid)
        assert err is None
        assert found.created == generated.created
        assert found.expires_at == generated.expires_at
        assert found.x_5_c == generated.x_5_c

        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_clone_app_key(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

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

        APP_URL_2 = "https://example.com/bookmark2.htm"
        APP_LABEL_2 = "AddBookmarkApp2"
        app_settings_app_2 = models.BookmarkApplicationSettingsApplication({
            "requestIntegration": False,
            "url": APP_URL_2
        })
        app_settings_2 = models.BookmarkApplicationSettings({
            "app": app_settings_app_2
        })
        bookmark_app_obj_2 = models.BookmarkApplication({
            "label": APP_LABEL_2,
            "settings": app_settings_2
        })

        # Create App in org
        app, _, err = await client.create_application(bookmark_app_obj)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.BookmarkApplication)

        app_2, _, err = await client.create_application(bookmark_app_obj_2)
        assert err is None
        assert isinstance(app, models.Application)
        assert isinstance(app, models.BookmarkApplication)

        # Generate key
        query_params_generate = {"validityYears": 2}
        generated, _, err = await\
            client.generate_application_key(app.id, query_params_generate)
        assert err is None

        # Clone key into second app
        query_params_clone = {"targetAid": app_2.id}
        cloned, _, err = await\
            client.clone_application_key(
                app.id, generated.kid, query_params_clone)
        assert err is None
        assert cloned.kid == generated.kid
        assert cloned.expires_at == generated.expires_at
        assert cloned.x_5_c == generated.x_5_c

        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None
        _, err = await client.deactivate_application(app_2.id)
        assert err is None
        _, err = await client.delete_application(app_2.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_generate_csr(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create CSR
        csr_metadata = models.CsrMetadata({
            "subject": models.CsrMetadataSubject({
                "commonName": "SP Issuer",
                "countryName": "Canada",
                "localityName": "Toronto",
                "organizationName": "Okta, Inc.",
                "organizationalUnitName": "Dev"
            }),
            "subjectAltNames": models.CsrMetadataSubjectAltNames({
                "dnsNames": ["dev.okta.com"]
            })
        })

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

        # Generate CSR
        generated, _, err = await \
            client.generate_csr_for_application(app.id, csr_metadata)
        assert err is None
        assert generated.kty == "RSA"
        assert generated.csr is not None

        # Deactivate + delete app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_csr(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create CSR
        csr_metadata = models.CsrMetadata({
            "subject": models.CsrMetadataSubject({
                "commonName": "SP Issuer",
                "countryName": "Canada",
                "localityName": "Toronto",
                "organizationName": "Okta, Inc.",
                "organizationalUnitName": "Dev"
            }),
            "subjectAltNames": models.CsrMetadataSubjectAltNames({
                "dnsNames": ["dev.okta.com"]
            })
        })

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

        # Generate CSR
        generated, _, err = await \
            client.generate_csr_for_application(app.id, csr_metadata)
        assert err is None
        assert generated.kty == "RSA"
        assert generated.csr is not None

        # Get CSR
        found, _, err = await client.get_csr_for_application(app.id,
                                                             generated.id)
        assert err is None
        assert found is not None

        # Deactivate + delete app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_revoke_csr(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create CSR
        csr_metadata = models.CsrMetadata({
            "subject": models.CsrMetadataSubject({
                "commonName": "SP Issuer",
                "countryName": "Canada",
                "localityName": "Toronto",
                "organizationName": "Okta, Inc.",
                "organizationalUnitName": "Dev"
            }),
            "subjectAltNames": models.CsrMetadataSubjectAltNames({
                "dnsNames": ["dev.okta.com"]
            })
        })

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

        # Generate CSR
        generated, _, err = await \
            client.generate_csr_for_application(app.id, csr_metadata)
        assert err is None
        assert generated.kty == "RSA"
        assert generated.csr is not None

        # Get CSR
        found, _, err = await client.get_csr_for_application(app.id,
                                                             generated.id)
        assert err is None
        assert found is not None

        # Revoke
        _, err = await client.revoke_csr_from_application(app.id, generated.id)
        assert err is None

        # Verify deletion
        csr_list, _, err = await client.list_csrs_for_application(app.id)
        assert err is None
        assert next((csr for csr in csr_list if csr.id == generated.id), None)\
            is None

        # Deactivate + delete app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_grant_consent_to_scope(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create OIDC Application Object
        APP_LABEL = "AddOpenIdConnectApp-Grant-Consent-SCOPE"
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

        # Create grant request
        issuer = client.get_base_url()
        SCOPE_ID = "okta.roles.read"
        oauth_scope_consent_grant = models.OAuth2ScopeConsentGrant({
            "issuer": issuer,
            "scopeId": SCOPE_ID
        })

        # Grant consent
        _, _, err = await client.grant_consent_to_scope(
            app.id,
            oauth_scope_consent_grant)
        assert err is None

        # Check grant
        grants, _, err = await client.list_scope_consent_grants(app.id)
        assert err is None
        assert grants is not None
        assert next((grant for grant in grants if grant.scope_id == SCOPE_ID
                     and grant.issuer == issuer))

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_consent_grant(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create OIDC Application Object
        APP_LABEL = "AddOpenIdConnectApp-Get-Consent-Grant"
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
        CLIENT_ID = "testclientid123456"
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

        # Create grant request
        issuer = client.get_base_url()
        SCOPE_ID = "okta.roles.read"
        oauth_scope_consent_grant = models.OAuth2ScopeConsentGrant({
            "issuer": issuer,
            "scopeId": SCOPE_ID
        })

        # Grant consent
        _, _, err = await client.grant_consent_to_scope(
            app.id,
            oauth_scope_consent_grant)
        assert err is None

        # Check grant
        grants, _, err = await client.list_scope_consent_grants(app.id)
        assert err is None
        assert grants is not None
        found_grant = next((grant for grant in grants if grant.scope_id
                            == SCOPE_ID and grant.issuer == issuer))
        assert found_grant
        found, _, err = await\
            client.get_scope_consent_grant(app.id, found_grant.id)
        assert err is None
        assert found is not None

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_revoke_consent_grant(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create OIDC Application Object
        APP_LABEL = "AddOpenIdConnectApp-Revoke-Consent"
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
        CLIENT_ID = "testclientid123456"
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

        # Create grant request
        issuer = client.get_base_url()
        SCOPE_ID = "okta.users.read"
        oauth_scope_consent_grant = models.OAuth2ScopeConsentGrant({
            "issuer": issuer,
            "scopeId": SCOPE_ID
        })

        # Grant consent
        _, _, err = await client.grant_consent_to_scope(
            app.id,
            oauth_scope_consent_grant)
        assert err is None

        # Check grant
        grants, _, err = await client.list_scope_consent_grants(app.id)
        assert err is None
        assert grants is not None
        found_grant = next((grant for grant in grants if grant.scope_id
                            == SCOPE_ID and grant.issuer == issuer))
        assert found_grant
        found, _, err = await\
            client.get_scope_consent_grant(app.id, found_grant.id)
        assert err is None
        assert found is not None

        # Revoke
        _, err = await client.revoke_scope_consent_grant(app.id,
                                                         found_grant.id)
        assert err is None

        # Check again
        updated_grants, _, err = await client.list_scope_consent_grants(app.id)
        assert err is None
        found_grant = next((grant for grant in updated_grants if grant.scope_id
                            == SCOPE_ID and grant.issuer == issuer), None)
        assert found_grant is None

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None
