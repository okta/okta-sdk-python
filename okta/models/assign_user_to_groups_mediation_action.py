"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class AssignUserToGroupsMediationAction(object):

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
    def group_ids(self):
        if 'groupIds' not in self._map:
            self._map['groupIds'] = []
        return self._map.get('groupIds')

    @group_ids.setter
    def group_ids(self, val):
        self._map['groupIds'] = val

    @group_ids.deleter
    def group_ids(self):
        del self._map['groupIds']

