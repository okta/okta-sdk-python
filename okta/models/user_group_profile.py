"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class UserGroupProfile(object):

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
    def description(self):
        return self._map.get('description')

    @description.setter
    def description(self, val):
        self._map['description'] = val

    @description.deleter
    def description(self):
        del self._map['description']

    @property
    def name(self):
        return self._map.get('name')

    @name.setter
    def name(self, val):
        self._map['name'] = val

    @name.deleter
    def name(self):
        del self._map['name']

    def json(self):
        return Utils.to_json(self)
