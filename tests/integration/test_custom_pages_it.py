# flake8: noqa
# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import pytest

from okta import models
from tests.mocks import MockOktaClient


class TestCustomPagesResource:
    """
    Integration Tests for the Custom Pages Resource

    This test suite provides comprehensive integration testing for the Custom Pages API
    within the Okta Python SDK. The tests validate real API interactions using VCR for recording
    and replaying HTTP requests/responses.

    API Methods Tested:
    - Sign-In Page: get_default, get_customized, replace_customized, get_preview, replace_preview, delete_preview, delete_customized
    - Error Page: get_default, get_customized, replace_customized, get_preview, replace_preview, delete_preview, delete_customized
    - Sign-Out Page: get_settings, replace_settings
    - Widget Versions: list_all_sign_in_widget_versions
    """

    SDK_PREFIX = "python_sdk_pages"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_custom_pages_lifecycle(self, fs):
        """
        Test the complete lifecycle of Custom Pages operations

        This test covers:
        - Creating a temporary brand
        - Sign-In Page: default, customized, preview operations
        - Error Page: default, customized, preview operations
        - Sign-Out Page: settings operations
        - Widget versions listing
        - Cleaning up the temporary brand
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        brand_id = None

        try:
            # ===== CREATE BRAND (Prerequisite) =====
            print("\n=== Creating Brand ===")

            create_brand_request = models.CreateBrandRequest(
                name=f"{TestCustomPagesResource.SDK_PREFIX}_brand"
            )

            created_brand, _, err = await client.create_brand(create_brand_request)

            assert err is None, f"Failed to create brand: {err}"
            assert created_brand is not None

            brand_id = created_brand.id
            print(f"Created brand: {brand_id}")

            # ===== SIGN-IN PAGE LIFECYCLE =====
            print("\n=== Sign-In Page Operations ===")

            # Get Default Sign-In Page
            print("\n--- Getting Default Sign-In Page ---")
            default_signin, _, err = await client.get_default_sign_in_page(brand_id)

            assert err is None, f"Failed to get default sign-in page: {err}"
            assert default_signin is not None
            assert isinstance(default_signin, models.SignInPage)
            print(f"Retrieved default sign-in page")

            # Update Customized Sign-In Page
            print("\n--- Updating Customized Sign-In Page ---")
            custom_signin_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Custom Sign-In</title>
</head>
<body>
    <div id="okta-sign-in"></div>
    <script>
        // Custom sign-in page for testing
    </script>
</body>
</html>
            """.strip()

            custom_signin = models.SignInPage(
                page_content=custom_signin_content,
                widget_version="*",
                widget_customizations=models.SignInPageAllOfWidgetCustomizations(
                    widget_generation="G3"
                )
            )

            updated_signin, _, err = await client.replace_customized_sign_in_page(
                brand_id, custom_signin
            )

            assert err is None, f"Failed to update customized sign-in page: {err}"
            assert updated_signin is not None
            print(f"Updated customized sign-in page")

            # Get Customized Sign-In Page
            print("\n--- Getting Customized Sign-In Page ---")
            retrieved_signin, _, err = await client.get_customized_sign_in_page(brand_id)

            assert err is None, f"Failed to get customized sign-in page: {err}"
            assert retrieved_signin is not None
            assert isinstance(retrieved_signin, models.SignInPage)
            print(f"Retrieved customized sign-in page")

            # Update Preview Sign-In Page
            print("\n--- Updating Preview Sign-In Page ---")
            preview_signin_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Preview Sign-In</title>
</head>
<body>
    <div id="okta-sign-in"></div>
    <script>
        // Preview sign-in page for testing
    </script>
</body>
</html>
            """.strip()

            preview_signin = models.SignInPage(
                page_content=preview_signin_content,
                widget_version="*",
                widget_customizations=models.SignInPageAllOfWidgetCustomizations(
                    widget_generation="G3"
                )
            )

            updated_preview_signin, _, err = await client.replace_preview_sign_in_page(
                brand_id, preview_signin
            )

            assert err is None, f"Failed to update preview sign-in page: {err}"
            assert updated_preview_signin is not None
            print(f"Updated preview sign-in page")

            # Get Preview Sign-In Page
            print("\n--- Getting Preview Sign-In Page ---")
            retrieved_preview_signin, _, err = await client.get_preview_sign_in_page(brand_id)

            assert err is None, f"Failed to get preview sign-in page: {err}"
            assert retrieved_preview_signin is not None
            print(f"Retrieved preview sign-in page")

            # Delete Preview Sign-In Page
            print("\n--- Deleting Preview Sign-In Page ---")
            _, _, err = await client.delete_preview_sign_in_page(brand_id)

            assert err is None, f"Failed to delete preview sign-in page: {err}"
            print(f"Deleted preview sign-in page")

            # Delete Customized Sign-In Page
            print("\n--- Deleting Customized Sign-In Page ---")
            _, _, err = await client.delete_customized_sign_in_page(brand_id)

            assert err is None, f"Failed to delete customized sign-in page: {err}"
            print(f"Deleted customized sign-in page")

            # ===== ERROR PAGE LIFECYCLE =====
            print("\n=== Error Page Operations ===")

            # Get Default Error Page
            print("\n--- Getting Default Error Page ---")
            default_error, _, err = await client.get_default_error_page(brand_id)

            assert err is None, f"Failed to get default error page: {err}"
            assert default_error is not None
            assert isinstance(default_error, models.ErrorPage)
            print(f"Retrieved default error page")

            # Update Customized Error Page
            print("\n--- Updating Customized Error Page ---")
            custom_error_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Custom Error Page</title>
</head>
<body>
    <h1>Custom Error</h1>
    <p>Something went wrong. Please try again.</p>
</body>
</html>
            """.strip()

            custom_error = models.ErrorPage(
                page_content=custom_error_content
            )

            updated_error, _, err = await client.replace_customized_error_page(
                brand_id, custom_error
            )

            assert err is None, f"Failed to update customized error page: {err}"
            assert updated_error is not None
            print(f"Updated customized error page")

            # Get Customized Error Page
            print("\n--- Getting Customized Error Page ---")
            retrieved_error, _, err = await client.get_customized_error_page(brand_id)

            assert err is None, f"Failed to get customized error page: {err}"
            assert retrieved_error is not None
            assert isinstance(retrieved_error, models.ErrorPage)
            print(f"Retrieved customized error page")

            # Update Preview Error Page
            print("\n--- Updating Preview Error Page ---")
            preview_error_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Preview Error Page</title>
</head>
<body>
    <h1>Preview Error</h1>
    <p>This is a preview error page.</p>
</body>
</html>
            """.strip()

            preview_error = models.ErrorPage(
                page_content=preview_error_content
            )

            updated_preview_error, _, err = await client.replace_preview_error_page(
                brand_id, preview_error
            )

            assert err is None, f"Failed to update preview error page: {err}"
            assert updated_preview_error is not None
            print(f"Updated preview error page")

            # Get Preview Error Page
            print("\n--- Getting Preview Error Page ---")
            retrieved_preview_error, _, err = await client.get_preview_error_page(brand_id)

            assert err is None, f"Failed to get preview error page: {err}"
            assert retrieved_preview_error is not None
            print(f"Retrieved preview error page")

            # Delete Preview Error Page
            print("\n--- Deleting Preview Error Page ---")
            _, _, err = await client.delete_preview_error_page(brand_id)

            assert err is None, f"Failed to delete preview error page: {err}"
            print(f"Deleted preview error page")

            # Delete Customized Error Page
            print("\n--- Deleting Customized Error Page ---")
            _, _, err = await client.delete_customized_error_page(brand_id)

            assert err is None, f"Failed to delete customized error page: {err}"
            print(f"Deleted customized error page")

            # ===== SIGN-OUT PAGE SETTINGS =====
            print("\n=== Sign-Out Page Settings ===")

            # Get Sign-Out Page Settings
            print("\n--- Getting Sign-Out Page Settings ---")
            signout_settings, _, err = await client.get_sign_out_page_settings(brand_id)

            assert err is None, f"Failed to get sign-out page settings: {err}"
            assert signout_settings is not None
            assert isinstance(signout_settings, models.HostedPage)
            print(f"Retrieved sign-out page settings")

            # Update Sign-Out Page Settings
            print("\n--- Updating Sign-Out Page Settings ---")
            updated_signout_settings = models.HostedPage(
                type="OKTA_DEFAULT"
            )

            result_signout, _, err = await client.replace_sign_out_page_settings(
                brand_id, updated_signout_settings
            )

            assert err is None, f"Failed to update sign-out page settings: {err}"
            assert result_signout is not None
            print(f"Updated sign-out page settings")

            # ===== LIST WIDGET VERSIONS =====
            print("\n=== Listing Sign-In Widget Versions ===")

            widget_versions, _, err = await client.list_all_sign_in_widget_versions(brand_id)

            assert err is None, f"Failed to list widget versions: {err}"
            assert widget_versions is not None
            assert isinstance(widget_versions, list)
            print(f"Listed {len(widget_versions)} widget version(s)")

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

                except Exception as e:
                    print(f"Exception deleting brand: {e}")

            print("=== Cleanup completed ===")

