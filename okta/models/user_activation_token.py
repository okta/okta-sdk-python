"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class UserActivationToken(object):

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
    def activation_token(self):
        return self._map.get('activationToken')

    @activation_token.setter
    def activation_token(self, val):
        self._map['activationToken'] = val

    @activation_token.deleter
    def activation_token(self):
        del self._map['activationToken']

    @property
    def activation_url(self):
        return self._map.get('activationUrl')

    @activation_url.setter
    def activation_url(self, val):
        self._map['activationUrl'] = val

    @activation_url.deleter
    def activation_url(self):
        del self._map['activationUrl']

    def json(self):
        return Utils.to_json(self)
