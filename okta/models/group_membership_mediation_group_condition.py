"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class GroupMembershipMediationGroupCondition(object):

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
    def exclude(self):
        if 'exclude' not in self._map:
            self._map['exclude'] = []
        return self._map.get('exclude')

    @exclude.setter
    def exclude(self, val):
        self._map['exclude'] = val

    @exclude.deleter
    def exclude(self):
        del self._map['exclude']

    @property
    def include(self):
        if 'include' not in self._map:
            self._map['include'] = []
        return self._map.get('include')

    @include.setter
    def include(self, val):
        self._map['include'] = val

    @include.deleter
    def include(self):
        del self._map['include']

    def json(self):
        return Utils.to_json(self)
