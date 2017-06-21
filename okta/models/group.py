"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .okta_object import OktaObject
from .okta_object import OktaObject
from .group_profile import GroupProfile


class Group(object):

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
            _dict[k] = OktaObject(v, self._client)
        return _dict

    @property
    def created(self):
        if self._map.get('created'):
            return Utils.parse_date(self._map.get('created'))
        return None

    @property
    def id(self):
        return self._map.get('id')

    @property
    def last_membership_updated(self):
        if self._map.get('lastMembershipUpdated'):
            return Utils.parse_date(self._map.get('lastMembershipUpdated'))
        return None

    @property
    def last_updated(self):
        if self._map.get('lastUpdated'):
            return Utils.parse_date(self._map.get('lastUpdated'))
        return None

    @property
    def object_class(self):
        if 'objectClass' not in self._map:
            self._map['objectClass'] = []
        return self._map.get('objectClass')

    @property
    def profile(self):
        if 'profile' not in self._map:
            self._map['profile'] = {}
        return GroupProfile(self._map['profile'], self._client)

    @profile.setter
    def profile(self, val):
        self._map['profile'] = val

    @profile.deleter
    def profile(self):
        del self._map['profile']

    @property
    def type(self):
        return self._map.get('type')

    def json(self):
        return Utils.to_json(self)
