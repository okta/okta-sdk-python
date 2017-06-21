"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class GroupRuleExpression(object):

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
    def type(self):
        return self._map.get('type')

    @type.setter
    def type(self, val):
        self._map['type'] = val

    @type.deleter
    def type(self):
        del self._map['type']

    @property
    def value(self):
        return self._map.get('value')

    @value.setter
    def value(self, val):
        self._map['value'] = val

    @value.deleter
    def value(self):
        del self._map['value']

    def json(self):
        return Utils.to_json(self)
