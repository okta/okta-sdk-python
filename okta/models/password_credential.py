"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .hashed_password import HashedPassword


class PasswordCredential(object):

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
    def hash(self):
        if 'hash' not in self._map:
            self._map['hash'] = {}
        return HashedPassword(self._map['hash'], self._client)

    @hash.setter
    def hash(self, val):
        self._map['hash'] = val

    @hash.deleter
    def hash(self):
        del self._map['hash']

    def json(self):
        return Utils.to_json(self)
