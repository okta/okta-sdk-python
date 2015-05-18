from okta.models.app.AppSettings import AppSettings


class Settings:

    types = {
        'app': AppSettings
    }

    def __init__(self):

        self.app = None  # AppSettings