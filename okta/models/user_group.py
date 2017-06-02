"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .embedded_object import EmbeddedObject
from .links_union import LinksUnion
from .user_group_profile import UserGroupProfile


class UserGroup(object):

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
            _dict[k] = EmbeddedObject(v, self._client)
        return _dict

    @property
    def links(self):
        if '_links' not in self._map:
            self._map['_links'] = {}

        _dict = {}
        for k, v in self._map['_links'].items():
            _dict[k] = LinksUnion(v, self._client)
        return _dict

    @property
    def created(self):
        return self._map.get('created')

    @property
    def id(self):
        return self._map.get('id')

    @property
    def last_membership_updated(self):
        return self._map.get('lastMembershipUpdated')

    @property
    def last_updated(self):
        return self._map.get('lastUpdated')

    @property
    def object_class(self):
        if 'objectClass' not in self._map:
            self._map['objectClass'] = []
        return self._map.get('objectClass')

    @property
    def profile(self):
        if 'profile' not in self._map:
            self._map['profile'] = {}
        return UserGroupProfile(self._map['profile'], self._client)

    @profile.setter
    def profile(self, val):
        self._map['profile'] = val

    @profile.deleter
    def profile(self):
        del self._map['profile']

    @property
    def type(self):
        return self._map.get('type')

