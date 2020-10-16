import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from okta.constants import DATETIME_FORMAT
import datetime as dt


class TestLogEventsResource:
    """
    Integration Tests for the Log Events Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_get_logs(self):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Bookmark Application Object
        APP_URL = "https://example.com/bookmark.htm"
        APP_LABEL = "AddBookmarkApp-GetLogs"
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

        logs, _, err = await client.get_logs()
        assert err is None
        assert logs is not None
        assert isinstance(logs, list)
        if logs[0]:
            assert isinstance(logs[0], models.LogEvent)

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_get_logs_polling(self):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Bookmark Application Object
        APP_URL = "https://example.com/bookmark.htm"
        APP_LABEL = "AddBookmarkApp-GetLogs"
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

        now = dt.datetime.now(dt.timezone.utc)
        now = now.replace(microsecond=0)
        one_minute_after = now + dt.timedelta(minutes=1)

        log_query_params = {
            "sortOrder": "ASCENDING",
            "until": one_minute_after.strftime(DATETIME_FORMAT)
        }

        logs, _, err = await client.get_logs(log_query_params)
        assert err is None
        assert logs is not None
        assert isinstance(logs, list)
        if logs[0]:
            assert isinstance(logs[0], models.LogEvent)

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None

    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_get_logs_bounded(self):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Bookmark Application Object
        APP_URL = "https://example.com/bookmark.htm"
        APP_LABEL = "AddBookmarkApp-GetLogs"
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

        # Retrieve logs
        now = dt.datetime.now(dt.timezone.utc)
        now = now.replace(microsecond=0)
        one_hour_before = now - dt.timedelta(hours=1)

        log_query_params = {
            "since": one_hour_before.strftime(DATETIME_FORMAT),
            "until": now.strftime(DATETIME_FORMAT)
        }
        logs, _, err = await client.get_logs(log_query_params)
        assert err is None
        assert logs is not None
        assert isinstance(logs, list)
        if logs[0]:
            assert isinstance(logs[0], models.LogEvent)

        # Deactivate & Delete created app
        _, err = await client.deactivate_application(app.id)
        assert err is None
        _, err = await client.delete_application(app.id)
        assert err is None
