from okta.models.user import Password


class ChangePasswordRequest:

    types = {
        'oldPassword': Password,
        'newPassword': Password
    }

    def __init__(self):

        self.oldPassword = None  # Password

        self.newPassword = None  # Password
