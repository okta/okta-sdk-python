from okta.models.app.AppLink import AppLink


class Links:
    types = {
        'appLinks': AppLink
    }
    def __init__(self):
        self.appLinks = None