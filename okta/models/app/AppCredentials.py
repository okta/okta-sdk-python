from okta.models.app.UserNameTemplate import UserNameTemplate
from okta.models.user.Password import Password


class AppCredentials:

    types = {
        'scheme': str,
        'userNameTemplate': UserNameTemplate,
        'userName': str,
        'password': Password
    }

    def __init__(self):

        # Determines how credentials are managed for the signOnMode
        self.scheme = None  # enum

        # Template used to generate a users username when the application is assigned via a group or directly to a user
        self.userNameTemplate = None  # UserNameTemplate

        # Shared username for app
        self.userName = None  # str

        # Shared password for app
        self.password = None  # Password
