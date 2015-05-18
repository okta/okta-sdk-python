from datetime import datetime
from okta.models.app.AppUserCredentials import AppUserCredentials
from okta.models.app.AppUserProfile import AppUserProfile


class AppUser:

    types = {
        'id': str,
        'externalId': str,
        'created': datetime,
        'lastUpdated': datetime,
        'scope': str,
        'status': str,
        'statusChanged': datetime,
        'passwordChanged': datetime,
        'syncState': str,
        'lastSynced': datetime,
        'credentials': AppUserCredentials,
        'profile': AppUserProfile
    }

    def __init__(self):

        # unique key of user
        self.id = None  # str

        # id of user in target app (must be imported or provisioned)
        self.externalId = None  # str

        # timestamp when user was created
        self.created = None  # datetime

        # timestamp when user was last updated
        self.lastUpdated = None  # datetime

        # toggles the assignment between user or group scope
        self.scope = None  # str

        # status of app user
        self.status = None  # str

        # timestamp when status last changed
        self.statusChanged = None  # datetime

        # timestamp when app password last changed
        self.passwordChanged = None  # datetime

        # synchronization state for app user
        self.syncState = None  # str

        # timestamp when last sync operation was executed
        self.lastSynced = None  # datetime

        # credentials for assigned app
        self.credentials = None  # AppUserCredentials

        # app-specific profile for the user
        self.profile = None  # AppUserProfile

        self.links = None  # Map<String, LinksUnion>

        self.embedded = None  # Map<String, Object>
