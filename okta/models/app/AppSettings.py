class AppSettings:

    types = {
        'url': str,
        'requestIntegration': bool,
        'authURL': str,
        'usernameField': str,
        'passwordField': str,
        'buttonField': str,
        'extraFieldSelector': str,
        'extraFieldValue': str,
        'optionalField1': str,
        'optionalField1Value': str,
        'optionalField2': str,
        'optionalField2Value': str,
        'optionalField3': str,
        'optionalField3Value': str
    }

    def __init__(self):

        # The URL of the login page for this app
        self.url = None  # str

        # Would you like Okta to add an integration for this app?
        self.requestIntegration = None  # bool

        # The URL of the authenticating site for this app
        self.authURL = None  # str

        # CSS selector for the username field in the login form
        self.usernameField = None  # str

        # CSS selector for the password field in the login form
        self.passwordField = None  # str

        # CSS selector for the login button in the login form
        self.buttonField = None  # str

        # CSS selector for the extra field in the form
        self.extraFieldSelector = None  # str

        # Value for extra field form field
        self.extraFieldValue = None  # str

        # Name of the optional parameter in the login form
        self.optionalField1 = None  # str

        # Name of the optional value in the login form
        self.optionalField1Value = None  # str

        # Name of the optional parameter in the login form
        self.optionalField2 = None  # str

        # Name of the optional value in the login form
        self.optionalField2Value = None  # str

        # Name of the optional parameter in the login form
        self.optionalField3 = None  # str

        # Name of the optional value in the login form
        self.optionalField3Value = None  # str
