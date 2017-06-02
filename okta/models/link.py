"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class Link(object):

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
    def hints(self):
        if 'hints' not in self._map:
            self._map['hints'] = {}
        return self._map.get('hints')

    @hints.setter
    def hints(self, val):
        self._map['hints'] = val

    @hints.deleter
    def hints(self):
        del self._map['hints']

    @property
    def href(self):
        return self._map.get('href')

    @href.setter
    def href(self, val):
        self._map['href'] = val

    @href.deleter
    def href(self):
        del self._map['href']

    @property
    def method(self):
        return self._map.get('method')

    @method.setter
    def method(self, val):
        self._map['method'] = val

    @method.deleter
    def method(self):
        del self._map['method']

    @property
    def name(self):
        return self._map.get('name')

    @name.setter
    def name(self, val):
        self._map['name'] = val

    @name.deleter
    def name(self):
        del self._map['name']

    @property
    def rel(self):
        return self._map.get('rel')

    @rel.setter
    def rel(self, val):
        self._map['rel'] = val

    @rel.deleter
    def rel(self):
        del self._map['rel']

    @property
    def templated(self):
        return self._map.get('templated')

    @templated.setter
    def templated(self, val):
        self._map['templated'] = val

    @templated.deleter
    def templated(self):
        del self._map['templated']

    @property
    def title(self):
        return self._map.get('title')

    @title.setter
    def title(self, val):
        self._map['title'] = val

    @title.deleter
    def title(self):
        del self._map['title']

    @property
    def type(self):
        return self._map.get('type')

    @type.setter
    def type(self, val):
        self._map['type'] = val

    @type.deleter
    def type(self):
        del self._map['type']

    def json(self):
        return Utils.to_json(self)
