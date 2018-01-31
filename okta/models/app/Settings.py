from okta.models.app.AppSettings import AppSettings
from okta.models.app.OAuthClientSettings import OAuthClientSettings


class Settings:

    types = {
        'app': AppSettings,
        'oauthClient': OAuthClientSettings,
        'notifications': dict
    }

    def __init__(self):

        self.app = None  # AppSettings
        
        self.oauthClient = None # OAuthClientSettings

        self.notifications = None