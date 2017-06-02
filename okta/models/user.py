"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .okta_object import OktaObject
from .link import Link
from .user_credentials import UserCredentials
from .user_profile import UserProfile


class User(object):

    def __init__(self, dictionary={}, client=None):
        self._client = client

        if isinstance(dictionary, dict):
            self._map = dictionary
        else:
            self._map = dictionary._map

    def get(self, key):
        return self._map[key]

    def set(self, key, value):
        self._map[key] = value

    @property
    def embedded(self):
        if '_embedded' not in self._map:
            self._map['_embedded'] = {}

        _dict = {}
        for k, v in self._map['_embedded'].items():
            _dict[k] = OktaObject(v, self._client)
        return _dict

    @property
    def links(self):
        if '_links' not in self._map:
            self._map['_links'] = {}

        _dict = {}
        for k, v in self._map['_links'].items():
            _dict[k] = Link(v, self._client)
        return _dict

    @property
    def activated(self):
        return self._map.get('activated')

    @property
    def created(self):
        return self._map.get('created')

    @property
    def credentials(self):
        if 'credentials' not in self._map:
            self._map['credentials'] = {}
        return UserCredentials(self._map['credentials'], self._client)

    @credentials.setter
    def credentials(self, val):
        self._map['credentials'] = val

    @credentials.deleter
    def credentials(self):
        del self._map['credentials']

    @property
    def id(self):
        return self._map.get('id')

    @property
    def last_login(self):
        return self._map.get('lastLogin')

    @property
    def last_updated(self):
        return self._map.get('lastUpdated')

    @property
    def password_changed(self):
        return self._map.get('passwordChanged')

    @property
    def profile(self):
        if 'profile' not in self._map:
            self._map['profile'] = {}
        return UserProfile(self._map['profile'], self._client)

    @profile.setter
    def profile(self, val):
        self._map['profile'] = val

    @profile.deleter
    def profile(self):
        del self._map['profile']

    @property
    def status(self):
        return self._map.get('status')

    @property
    def status_changed(self):
        return self._map.get('statusChanged')

    @property
    def transitioning_to_status(self):
        return self._map.get('transitioningToStatus')

