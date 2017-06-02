"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class FactorDevice(object):

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
    def id(self):
        return self._map.get('id')

    @id.setter
    def id(self, val):
        self._map['id'] = val

    @id.deleter
    def id(self):
        del self._map['id']

    @property
    def links(self):
        if 'links' not in self._map:
            self._map['links'] = {}
        return (self._map['links'], self._client)

    @links.setter
    def links(self, val):
        self._map['links'] = val

    @links.deleter
    def links(self):
        del self._map['links']

    @property
    def status(self):
        return self._map.get('status')

    @status.setter
    def status(self, val):
        self._map['status'] = val

    @status.deleter
    def status(self):
        del self._map['status']

    def json(self):
        return Utils.to_json(self)
