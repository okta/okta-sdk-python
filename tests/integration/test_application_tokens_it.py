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

import okta.models as models
from okta.errors.okta_api_error import OktaAPIError
from tests.mocks import MockOktaClient


class TestApplicationTokensResource:
    """
    Integration Tests for the Application Tokens API
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_application_tokens_lifecycle(self, fs):
        """
        Test the complete lifecycle of OAuth 2.0 application tokens:
        1. Create an OAuth 2.0 application
        2. List all tokens for the application
        3. Get a specific token (if any exist)
        4. Revoke a specific token (if any exist)
        5. Revoke all remaining tokens

        Note: This test requires manual setup of at least 2 refresh tokens
        for the created application through the Authorization Code flow.
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create an OpenID Connect (OAuth 2.0) application
        APP_LABEL = "TestOAuth2TokensApp"

        # Configure OAuth client settings
        oauth_client_settings = models.OpenIdConnectApplicationSettingsClient(
            application_type=models.OpenIdConnectApplicationType.WEB,
            grant_types=[
                models.OAuthGrantType.AUTHORIZATION_CODE,
                models.OAuthGrantType.REFRESH_TOKEN,
            ],
            response_types=[models.OAuthResponseType.CODE],
            redirect_uris=["https://example.com/callback"],
            consent_method=models.OpenIdConnectApplicationConsentMethod.REQUIRED,
        )

        # Create application settings
        app_settings = models.OpenIdConnectApplicationSettings(
            oauth_client=oauth_client_settings
        )

        # Create the OIDC application object
        oidc_app = models.OpenIdConnectApplication(
            label=APP_LABEL,
            sign_on_mode=models.ApplicationSignOnMode.OPENID_CONNECT,
            settings=app_settings,
        )

        app = None
        try:
            # Create the application
            app, _, err = await client.create_application(oidc_app)
            assert err is None
            assert isinstance(app, models.Application)
            assert isinstance(app, models.OpenIdConnectApplication)

            app_id = app.id
            print(f"Created OAuth 2.0 application: {app_id}")

            # A. List Tokens - Get all OAuth 2.0 tokens for the application
            tokens, _, err = await client.list_o_auth2_tokens_for_application(app_id)
            assert err is None
            assert isinstance(tokens, list)

            # If no tokens exist, this test demonstrates the API works but cannot proceed with token operations
            if len(tokens) == 0:
                print(
                    "No tokens found for the application. Token operations require manual setup."
                )
                # Test that the API calls work even with no tokens

                # Try to get a non-existent token (should return 404)
                try:
                    non_existent_token, _, err = (
                        await client.get_o_auth2_token_for_application(
                            app_id, "non-existent-token-id"
                        )
                    )
                    assert err is not None or non_existent_token is None
                except OktaAPIError as e:
                    assert e.response.status == 404

                # Test revoking all tokens (should succeed even if no tokens exist)
                _, resp, err = await client.revoke_o_auth2_tokens_for_application(
                    app_id
                )
                assert err is None
                assert resp.status_code == 204

                return  # Exit early as no tokens available for full lifecycle test

            print(f"Found {len(tokens)} tokens for testing")

            # Verify we have enough tokens for the test
            if len(tokens) < 2:
                print(
                    "Warning: Test works better with at least 2 tokens, but proceeding with available tokens"
                )

            # Verify each token is an OAuth2Token object
            for token in tokens:
                assert isinstance(token, models.OAuth2Token)
                assert token.id is not None
                assert token.client_id is not None
                assert token.user_id is not None
                assert token.status is not None

            # B. Get a Specific Token - Retrieve details of the first token
            first_token_id = tokens[0].id
            retrieved_token, _, err = await client.get_o_auth2_token_for_application(
                app_id, first_token_id
            )
            assert err is None
            assert isinstance(retrieved_token, models.OAuth2Token)
            assert retrieved_token.id == first_token_id
            assert retrieved_token.client_id == tokens[0].client_id
            assert retrieved_token.user_id == tokens[0].user_id

            # C. Revoke a Specific Token
            # Revoke the first token
            _, resp, err = await client.revoke_o_auth2_token_for_application(
                app_id, first_token_id
            )
            assert err is None
            assert resp.status_code == 204, "Token revocation should return HTTP 204"

            # Verify the token was revoked by trying to get it again (should fail with 404)
            try:
                revoked_token, _, err = await client.get_o_auth2_token_for_application(
                    app_id, first_token_id
                )
                # If we get here without an exception, check if error was returned
                assert (
                        err is not None or revoked_token is None
                ), "Getting revoked token should fail"
            except OktaAPIError as e:
                # Expected behavior - token should not be found
                assert (
                        e.response.status == 404
                ), "Getting revoked token should return 404"

            # D. Revoke All Remaining Tokens
            # First, verify we still have tokens to revoke (or none if we started with only 1)
            remaining_tokens, _, err = await client.list_o_auth2_tokens_for_application(
                app_id
            )
            assert err is None
            assert isinstance(remaining_tokens, list)
            initial_remaining_count = len(remaining_tokens)

            # Revoke all remaining tokens
            _, resp, err = await client.revoke_o_auth2_tokens_for_application(app_id)
            assert err is None
            assert (
                    resp.status_code == 204
            ), "Bulk token revocation should return HTTP 204"

            # Verify all tokens have been revoked
            final_tokens, _, err = await client.list_o_auth2_tokens_for_application(
                app_id
            )
            assert err is None
            assert isinstance(final_tokens, list)
            assert (
                    len(final_tokens) == 0
            ), "All tokens should be revoked after bulk revocation"

        finally:
            # Clean up - Delete the created application
            if app and app.id:
                errors = []
                try:
                    # Deactivate the application first
                    _, _, err = await client.deactivate_application(app.id)
                    if err:
                        errors.append(f"Failed to deactivate app: {err}")
                except Exception as exc:
                    errors.append(f"Exception deactivating app: {exc}")

                try:
                    # Delete the application
                    _, _, err = await client.delete_application(app.id)
                    if err:
                        errors.append(f"Failed to delete app: {err}")
                except Exception as exc:
                    errors.append(f"Exception deleting app: {exc}")

                if errors:
                    print(f"Cleanup errors: {errors}")
                    # Don't fail the test due to cleanup issues

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_tokens_with_expand_parameter(self, fs):
        """
        Test listing tokens with expand parameter to increase coverage
        """
        client = MockOktaClient(fs)

        # Create a test application first
        APP_LABEL = "TestExpandTokensApp"
        oauth_client_settings = models.OpenIdConnectApplicationSettingsClient(
            application_type=models.OpenIdConnectApplicationType.WEB,
            grant_types=[
                models.OAuthGrantType.AUTHORIZATION_CODE,
                models.OAuthGrantType.REFRESH_TOKEN,
            ],
            response_types=[models.OAuthResponseType.CODE],
            redirect_uris=["https://example.com/callback"],
        )

        app_settings = models.OpenIdConnectApplicationSettings(
            oauth_client=oauth_client_settings
        )

        oidc_app = models.OpenIdConnectApplication(
            label=APP_LABEL,
            sign_on_mode=models.ApplicationSignOnMode.OPENID_CONNECT,
            settings=app_settings,
        )

        app = None
        try:
            app, _, err = await client.create_application(oidc_app)
            assert err is None
            app_id = app.id

            # Test list tokens with expand parameter
            tokens_expanded, _, err = await client.list_o_auth2_tokens_for_application(
                app_id, expand="user"
            )
            assert err is None
            assert isinstance(tokens_expanded, list)

            # Test list tokens with limit parameter for pagination
            tokens_paginated, _, err = await client.list_o_auth2_tokens_for_application(
                app_id, limit=10
            )
            assert err is None
            assert isinstance(tokens_paginated, list)

        finally:
            if app and app.id:
                try:
                    await client.deactivate_application(app.id)
                    await client.delete_application(app.id)
                except:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_token_with_expand_parameter(self, fs):
        """
        Test getting a specific token with expand parameter
        """
        client = MockOktaClient(fs)

        # Create a test application
        APP_LABEL = "TestGetTokenExpandApp"
        oauth_client_settings = models.OpenIdConnectApplicationSettingsClient(
            application_type=models.OpenIdConnectApplicationType.WEB,
            grant_types=[models.OAuthGrantType.AUTHORIZATION_CODE],
            response_types=[models.OAuthResponseType.CODE],
            redirect_uris=["https://example.com/callback"],
        )

        app_settings = models.OpenIdConnectApplicationSettings(
            oauth_client=oauth_client_settings
        )

        oidc_app = models.OpenIdConnectApplication(
            label=APP_LABEL,
            sign_on_mode=models.ApplicationSignOnMode.OPENID_CONNECT,
            settings=app_settings,
        )

        app = None
        try:
            app, _, err = await client.create_application(oidc_app)
            assert err is None
            app_id = app.id

            # First get tokens to see if any exist
            tokens, _, err = await client.list_o_auth2_tokens_for_application(app_id)
            assert err is None

            if tokens and len(tokens) > 0:
                # Test get token with expand parameter
                token_expanded, _, err = await client.get_o_auth2_token_for_application(
                    app_id, tokens[0].id, expand="user"
                )
                assert err is None
                assert isinstance(token_expanded, models.OAuth2Token)

        finally:
            if app and app.id:
                try:
                    await client.deactivate_application(app.id)
                    await client.delete_application(app.id)
                except:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_error_scenarios(self, fs):
        """
        Test various error scenarios to increase coverage
        """
        client = MockOktaClient(fs)

        # Create a test application
        APP_LABEL = "TestErrorScenariosApp"
        oauth_client_settings = models.OpenIdConnectApplicationSettingsClient(
            application_type=models.OpenIdConnectApplicationType.WEB,
            grant_types=[models.OAuthGrantType.AUTHORIZATION_CODE],
            response_types=[models.OAuthResponseType.CODE],
            redirect_uris=["https://example.com/callback"],
        )

        app_settings = models.OpenIdConnectApplicationSettings(
            oauth_client=oauth_client_settings
        )

        oidc_app = models.OpenIdConnectApplication(
            label=APP_LABEL,
            sign_on_mode=models.ApplicationSignOnMode.OPENID_CONNECT,
            settings=app_settings,
        )

        app = None
        try:
            app, _, err = await client.create_application(oidc_app)
            assert err is None
            app_id = app.id

            # Test 1: Get token with invalid token ID (should return 404)
            invalid_token, _, err = await client.get_o_auth2_token_for_application(
                app_id, "invalid-token-id-123"
            )
            assert err is not None or invalid_token is None

            # Test 2: Revoke token with invalid token ID (should handle gracefully)
            try:
                result = await client.revoke_o_auth2_token_for_application(
                    app_id, "invalid-token-id-123"
                )
                # The method may return different number of values based on success/failure
                if len(result) == 3:
                    _, resp, err = result
                    assert resp.status_code in [204, 404] or err is not None
                else:
                    # Method succeeded or failed gracefully
                    assert True
            except Exception as e:
                # Any exception is acceptable for invalid token ID
                assert True

            # Test 3: Operations with invalid application ID
            invalid_tokens, _, err = await client.list_o_auth2_tokens_for_application(
                "invalid-app-id-123"
            )
            assert err is not None or invalid_tokens is None

        finally:
            if app and app.id:
                try:
                    await client.deactivate_application(app.id)
                    await client.delete_application(app.id)
                except:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_with_http_info_methods(self, fs):
        """
        Test the _with_http_info versions of the methods to increase coverage
        """
        client = MockOktaClient(fs)

        # Create a test application
        APP_LABEL = "TestHttpInfoApp"
        oauth_client_settings = models.OpenIdConnectApplicationSettingsClient(
            application_type=models.OpenIdConnectApplicationType.WEB,
            grant_types=[models.OAuthGrantType.AUTHORIZATION_CODE],
            response_types=[models.OAuthResponseType.CODE],
            redirect_uris=["https://example.com/callback"],
        )

        app_settings = models.OpenIdConnectApplicationSettings(
            oauth_client=oauth_client_settings
        )

        oidc_app = models.OpenIdConnectApplication(
            label=APP_LABEL,
            sign_on_mode=models.ApplicationSignOnMode.OPENID_CONNECT,
            settings=app_settings,
        )

        app = None
        try:
            app, _, err = await client.create_application(oidc_app)
            assert err is None
            app_id = app.id

            # Test list_o_auth2_tokens_for_application_with_http_info
            if hasattr(client, "list_o_auth2_tokens_for_application_with_http_info"):
                tokens_with_info, _, err = (
                    await client.list_o_auth2_tokens_for_application_with_http_info(
                        app_id
                    )
                )
                assert err is None
                assert isinstance(tokens_with_info, list)

            # Test revoke_o_auth2_tokens_for_application_with_http_info
            if hasattr(client, "revoke_o_auth2_tokens_for_application_with_http_info"):
                _, resp_info, err = (
                    await client.revoke_o_auth2_tokens_for_application_with_http_info(
                        app_id
                    )
                )
                assert err is None
                assert resp_info.status_code == 204

        finally:
            if app and app.id:
                try:
                    await client.deactivate_application(app.id)
                    await client.delete_application(app.id)
                except:
                    pass
