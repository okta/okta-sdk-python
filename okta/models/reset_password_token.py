"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class ResetPasswordToken(object):

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
    def reset_password_url(self):
        return self._map.get('resetPasswordUrl')

    @reset_password_url.setter
    def reset_password_url(self, val):
        self._map['resetPasswordUrl'] = val

    @reset_password_url.deleter
    def reset_password_url(self):
        del self._map['resetPasswordUrl']

