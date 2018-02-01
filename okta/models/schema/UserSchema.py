from datetime import datetime
from okta.models.schema.UserProfileCustomSubschema import UserProfileCustomSubschema

class UserSchema:

    types = {
        'id': str,
        'name': str,
        'title': str,
        'lastUpdated': datetime,
        'created': datetime,
        'definitions': dict,
        'type': str,
        'properties': dict
    }

    def __init__(self):

        self.id = None

        self.name = None

        self.title = None

        self.lastUpdated = None

        self.created = None

        self.definitions = None

        self.type = None

        self.properties = None
