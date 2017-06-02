"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class EmbeddedObject(object):

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
    def key(self):
        return self._map.get('key')

    @key.setter
    def key(self, val):
        self._map['key'] = val

    @key.deleter
    def key(self):
        del self._map['key']

