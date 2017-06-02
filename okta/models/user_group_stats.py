"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .link import Link


class UserGroupStats(object):

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
    def links(self):
        if '_links' not in self._map:
            self._map['_links'] = {}

        _dict = {}
        for k, v in self._map['_links'].items():
            _dict[k] = Link(v, self._client)
        return _dict

    @property
    def apps_count(self):
        return self._map.get('appsCount')

    @apps_count.setter
    def apps_count(self, val):
        self._map['appsCount'] = val

    @apps_count.deleter
    def apps_count(self):
        del self._map['appsCount']

    @property
    def group_push_mappings_count(self):
        return self._map.get('groupPushMappingsCount')

    @group_push_mappings_count.setter
    def group_push_mappings_count(self, val):
        self._map['groupPushMappingsCount'] = val

    @group_push_mappings_count.deleter
    def group_push_mappings_count(self):
        del self._map['groupPushMappingsCount']

    @property
    def users_count(self):
        return self._map.get('usersCount')

    @users_count.setter
    def users_count(self, val):
        self._map['usersCount'] = val

    @users_count.deleter
    def users_count(self):
        del self._map['usersCount']

    def json(self):
        return Utils.to_json(self)
