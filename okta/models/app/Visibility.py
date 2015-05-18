from okta.models.app.Hide import Hide
from okta.models.app.AppLinks import AppLinks


class Visibility:

    types = {
        'autoSubmitToolbar': bool,
        'hide': Hide,
        'appLinks': AppLinks
    }

    def __init__(self):

        # Automatically log in when user lands on login page
        self.autoSubmitToolbar = None  # bool

        # Hides this app for specific end-user apps
        self.hide = None  # Hide

        # Displays specific appLinks for the app
        self.appLinks = None  # AppLinks
