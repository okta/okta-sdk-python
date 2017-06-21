"""
 THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .shared.okta_utils import Utils
from .shared.collection import Collection
from .shared.http import Http
from .models import *
from .groups_client import GroupsClient
from .users_client import UsersClient



class Client:

    USER_AGENT = Utils.get_okta_user_agent()

    def __init__(self, **kwargs):
        
        # Set configuration values from kwargs
        if kwargs:
            self.__dict__.update(kwargs)
        else:
            # Default
            self.__dict__.update(
                {
                    'orgUrl': None,
                    'token': None,
                    'headers': None
                }
            )
        
        for key, value in self.__dict__.items():
            # Verify each attr is set
            if value is None:
                # Get environment or yaml config
                setattr(self, key, Utils.get_config(key))

        # Set Authorization and User-Agent Header
        try:
            getattr(self, "headers")
            # Set default header, unless overriden
            self.headers['Authorization'] = self.headers.get(
                'Authorization',
                'SSWS {}'.format(self.token)
            )
            self.headers['User-Agent'] = self.headers.get(
                'User-Agent',
                self.USER_AGENT
            )
        except AttributeError:
            # Set default headers
            self.headers = {
                'Authorization': 'SSWS {}'.format(self.token),
                'User-Agent': self.USER_AGENT
            }
        self.http = Http(self.headers)

    @property
    def groups(self):
        if not hasattr(self, '__groups'):
            self.__groups = GroupsClient(self)
        return self.__groups

    @property
    def users(self):
        if not hasattr(self, '__users'):
            self.__users = UsersClient(self)
        return self.__users

