from datetime import datetime


class Role:
    types = {
        'id': str,
        'label': str,
        'type': str,
        'status': str,
        'created': datetime,
        'lastUpdated': datetime,
    }

    def __init__(self, **kwargs):

        # unique key for user
        self.id = None  # str

        # display name of role
        self.label = None  # str

        # type of role
        self.type = None  # SUPER_ADMIN, ORG_ADMIN, APP_ADMIN, USER_ADMIN,
        # MOBILE_ADMIN, READ_ONLY_ADMIN

        # status of role assignment
        self.status = None  # str

        # timestamp when app user was created
        self.created = None  # datetime

        # timestamp when app user was last updated
        self.lastUpdated = None  # datetime
