from __future__ import unicode_literals


class AppUserProfile:

    types = {
        'username': str,
        'password': str
    }

    def __init__(self):

        self.username = None  # str

        self.password = None  # str
