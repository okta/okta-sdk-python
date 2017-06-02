"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .okta_object import OktaObject


class MediationRoleAssignment(object):

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
    def embedded(self):
        if '_embedded' not in self._map:
            self._map['_embedded'] = {}

        _dict = {}
        for k, v in self._map['_embedded'].items():
            _dict[k] = OktaObject(v, self._client)
        return _dict

    @property
    def created(self):
        if self._map.get('created'):
            return Utils.parse_date(self._map.get('created'))
        return None

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
    def id(self):
        return self._map.get('id')

    @property
    def label(self):
        return self._map.get('label')

    @property
    def last_updated(self):
        if self._map.get('lastUpdated'):
            return Utils.parse_date(self._map.get('lastUpdated'))
        return None

    @property
    def status(self):
        return self._map.get('status')

    @property
    def type(self):
        return self._map.get('type')

    def json(self):
        return Utils.to_json(self)
