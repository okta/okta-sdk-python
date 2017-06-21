"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .authentication_provider_type import AuthenticationProviderType


class AuthenticationProvider(object):

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
    def name(self):
        return self._map.get('name')

    @name.setter
    def name(self, val):
        self._map['name'] = val

    @name.deleter
    def name(self):
        del self._map['name']

    @property
    def type(self):
        if 'type' not in self._map:
            self._map['type'] = {}
        return AuthenticationProviderType(self._map['type'], self._client)

    @type.setter
    def type(self, val):
        self._map['type'] = val

    @type.deleter
    def type(self):
        del self._map['type']

    def json(self):
        return Utils.to_json(self)
