from datetime import datetime

from okta.models.user.LoginCredentials import LoginCredentials
from okta.models.user.UserProfile import UserProfile
from okta.models.Link import Link


class User:

    types = {
        'id': str,
        'status': str,
        'created': datetime,
        'activated': datetime,
        'statusChanged': datetime,
        'lastLogin': datetime,
        'lastUpdated': datetime,
        'passwordChanged': datetime,
        'transitioningToStatus': str,
        'profile': UserProfile,
        'credentials': LoginCredentials
    }

    dict_types = {
        '_links': Link
    }

    alt_names = {
        '_links': 'links'
    }

    def __init__(self, **kwargs):

        # unique key for user
        self.id = None  # str

        # current status of user
        self.status = None  # str

        # timestamp when user was created
        self.created = None  # datetime

        # timestamp when transition to ACTIVE status completed
        self.activated = None  # datetime

        # timestamp when status last changed
        self.statusChanged = None  # datetime

        # timestamp of last login
        self.lastLogin = None  # datetime

        # timestamp when user was last updated
        self.lastUpdated = None  # datetime

        # timestamp when password last changed
        self.passwordChanged = None  # datetime

        # target status of an in progress asynchronous status transition
        self.transitioningToStatus = None  # str

        self.profile = None  # UserProfile

        self.credentials = None  # LoginCredentials

        self.links = None

        # Populate profile
        profile_attrs = ['login', 'email', 'secondEmail', 'firstName', 'lastName', 'mobilePhone']
        for attr in profile_attrs:
            if attr in kwargs:
                self.profile = self.profile or UserProfile()
                setattr(self.profile, attr, kwargs[attr])