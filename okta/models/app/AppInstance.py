from datetime import datetime
from okta.models.app.Accessibility import Accessibility
from okta.models.app.Visibility import Visibility
from okta.models.app.AppCredentials import AppCredentials
from okta.models.app.Settings import Settings
from okta.models.app.AppSettings import AppSettings


class AppInstance:

    types = {
        'id': str,
        'name': str,
        'label': str,
        'created': datetime,
        'lastUpdated': datetime,
        'status': str,
        'activated': datetime,
        'features': str,
        'signOnMode': str,
        'accessibility': Accessibility,
        'visibility': Visibility,
        'credentials': AppCredentials,
        'settings': Settings
    }

    def __init__(self):

        # unique key for app
        self.id = None  # str

        # unique key for app definition
        self.name = None  # str

        # unique user-defined display name for app
        self.label = None  # str

        # timestamp when app was created
        self.created = None  # datetime

        # timestamp when app was last updated
        self.lastUpdated = None  # datetime

        # status of app
        self.status = None  # enum

        # timestamp when transition to ACTIVE status completed
        self.activated = None  # datetime

        # enabled app features
        self.features = None  # enum

        # authentication mode of app
        self.signOnMode = None  # enum

        self.accessibility = None  # Accessibility

        self.visibility = None  # Visibility

        self.credentials = None  # AppCredentials

        self.settings = None  # Settings

    @staticmethod
    def build_bookmark(url, label=None, request_integration=False):
        app = AppInstance()
        app.name = "bookmark"
        app.label = label
        app.signOnMode = "BOOKMARK"
        app.settings = Settings()
        app.settings.app = AppSettings()
        app.settings.app.url = url
        app.settings.app.requestIntegration = request_integration
        return app