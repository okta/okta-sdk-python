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

    def remove(self, key):
        del self._map[key]

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
        if self._map.get('activated'):
            return Utils.parse_date(self._map.get('activated'))
        return None

    @property
    def created(self):
        if self._map.get('created'):
            return Utils.parse_date(self._map.get('created'))
        return None

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
        if self._map.get('lastLogin'):
            return Utils.parse_date(self._map.get('lastLogin'))
        return None

    @property
    def last_updated(self):
        if self._map.get('lastUpdated'):
            return Utils.parse_date(self._map.get('lastUpdated'))
        return None

    @property
    def password_changed(self):
        if self._map.get('passwordChanged'):
            return Utils.parse_date(self._map.get('passwordChanged'))
        return None

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
        if self._map.get('statusChanged'):
            return Utils.parse_date(self._map.get('statusChanged'))
        return None

    @property
    def transitioning_to_status(self):
        return self._map.get('transitioningToStatus')

    def json(self):
        return Utils.to_json(self)
