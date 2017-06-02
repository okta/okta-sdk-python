"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class UserProfile(object):

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
    def email(self):
        return self._map.get('email')

    @email.setter
    def email(self, val):
        self._map['email'] = val

    @email.deleter
    def email(self):
        del self._map['email']

    @property
    def first_name(self):
        return self._map.get('firstName')

    @first_name.setter
    def first_name(self, val):
        self._map['firstName'] = val

    @first_name.deleter
    def first_name(self):
        del self._map['firstName']

    @property
    def last_name(self):
        return self._map.get('lastName')

    @last_name.setter
    def last_name(self, val):
        self._map['lastName'] = val

    @last_name.deleter
    def last_name(self):
        del self._map['lastName']

    @property
    def login(self):
        return self._map.get('login')

    @login.setter
    def login(self, val):
        self._map['login'] = val

    @login.deleter
    def login(self):
        del self._map['login']

    @property
    def mobile_phone(self):
        return self._map.get('mobilePhone')

    @mobile_phone.setter
    def mobile_phone(self, val):
        self._map['mobilePhone'] = val

    @mobile_phone.deleter
    def mobile_phone(self):
        del self._map['mobilePhone']

    @property
    def second_email(self):
        return self._map.get('secondEmail')

    @second_email.setter
    def second_email(self, val):
        self._map['secondEmail'] = val

    @second_email.deleter
    def second_email(self):
        del self._map['secondEmail']

