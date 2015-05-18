class Hide:

    types = {
        'iOS': bool,
        'web': bool
    }

    def __init__(self):

        # Okta Mobile for iOS or Android (pre-dates Android)
        self.iOS = None  # bool

        # Okta Web Browser Home Page
        self.web = None  # bool
