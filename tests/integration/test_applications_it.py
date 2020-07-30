import pytest
from tests.mocks import MockOktaClient
from http import HTTPStatus
import okta.models as models
from okta.client import Client
import time
# import sys
# import getopt


class TestApplicationsResource:
    """
    Integration Tests for the Applications Resource
    """

    # @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_bookmark_app(self):
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

        # Get app and verify details
        found_app, _, err = await client.get_application(app.id)
        assert err is None
        assert found_app.label == APP_LABEL
        assert found_app.sign_on_mode == models.ApplicationSignOnMode.BOOKMARK
        print(found_app)

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None
