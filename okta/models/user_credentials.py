"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .password_credential import PasswordCredential
from .auth_provider import AuthProvider
from .recovery_question_credential import RecoveryQuestionCredential


class UserCredentials(object):

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
    def password(self):
        if 'password' not in self._map:
            self._map['password'] = {}
        return PasswordCredential(self._map['password'], self._client)

    @password.setter
    def password(self, val):
        self._map['password'] = val

    @password.deleter
    def password(self):
        del self._map['password']

    @property
    def provider(self):
        if 'provider' not in self._map:
            self._map['provider'] = {}
        return AuthProvider(self._map['provider'], self._client)

    @property
    def recovery_question(self):
        if 'recovery_question' not in self._map:
            self._map['recovery_question'] = {}
        return RecoveryQuestionCredential(self._map['recovery_question'], self._client)

    @recovery_question.setter
    def recovery_question(self, val):
        self._map['recovery_question'] = val

    @recovery_question.deleter
    def recovery_question(self):
        del self._map['recovery_question']

