"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class TempPassword(object):

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
    def temp_password(self):
        return self._map.get('tempPassword')

    @temp_password.setter
    def temp_password(self, val):
        self._map['tempPassword'] = val

    @temp_password.deleter
    def temp_password(self):
        del self._map['tempPassword']

    def json(self):
        return Utils.to_json(self)
