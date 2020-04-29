from __future__ import unicode_literals


class ResetPasswordToken:

    types = {
        'resetPasswordUrl': str
    }

    def __init__(self):

        self.resetPasswordUrl = None  # str
