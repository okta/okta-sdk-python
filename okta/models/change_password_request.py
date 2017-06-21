"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .password_credential import PasswordCredential
from .password_credential import PasswordCredential


class ChangePasswordRequest(object):

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
    def new_password(self):
        if 'newPassword' not in self._map:
            self._map['newPassword'] = {}
        return PasswordCredential(self._map['newPassword'], self._client)

    @new_password.setter
    def new_password(self, val):
        self._map['newPassword'] = val

    @new_password.deleter
    def new_password(self):
        del self._map['newPassword']

    @property
    def old_password(self):
        if 'oldPassword' not in self._map:
            self._map['oldPassword'] = {}
        return PasswordCredential(self._map['oldPassword'], self._client)

    @old_password.setter
    def old_password(self, val):
        self._map['oldPassword'] = val

    @old_password.deleter
    def old_password(self):
        del self._map['oldPassword']

    def json(self):
        return Utils.to_json(self)
