from datetime import datetime


class AppGroup:

    types = {
        'id': str,
        'lastUpdated': datetime,
        'priority': int
    }

    def __init__(self):

        # unique key of group
        self.id = None  # str

        # timestamp when app group was last updated
        self.lastUpdated = None  # datetime

        # priority of group assignment
        self.priority = None  # int
