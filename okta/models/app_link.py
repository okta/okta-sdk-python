"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class AppLink(object):

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
    def app_assignment_id(self):
        return self._map.get('appAssignmentId')

    @app_assignment_id.setter
    def app_assignment_id(self, val):
        self._map['appAssignmentId'] = val

    @app_assignment_id.deleter
    def app_assignment_id(self):
        del self._map['appAssignmentId']

    @property
    def app_instance_id(self):
        return self._map.get('appInstanceId')

    @app_instance_id.setter
    def app_instance_id(self, val):
        self._map['appInstanceId'] = val

    @app_instance_id.deleter
    def app_instance_id(self):
        del self._map['appInstanceId']

    @property
    def app_name(self):
        return self._map.get('appName')

    @app_name.setter
    def app_name(self, val):
        self._map['appName'] = val

    @app_name.deleter
    def app_name(self):
        del self._map['appName']

    @property
    def credentials_setup(self):
        return self._map.get('credentialsSetup')

    @credentials_setup.setter
    def credentials_setup(self, val):
        self._map['credentialsSetup'] = val

    @credentials_setup.deleter
    def credentials_setup(self):
        del self._map['credentialsSetup']

    @property
    def hidden(self):
        return self._map.get('hidden')

    @hidden.setter
    def hidden(self, val):
        self._map['hidden'] = val

    @hidden.deleter
    def hidden(self):
        del self._map['hidden']

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
    def label(self):
        return self._map.get('label')

    @label.setter
    def label(self, val):
        self._map['label'] = val

    @label.deleter
    def label(self):
        del self._map['label']

    @property
    def link_url(self):
        return self._map.get('linkUrl')

    @link_url.setter
    def link_url(self, val):
        self._map['linkUrl'] = val

    @link_url.deleter
    def link_url(self):
        del self._map['linkUrl']

    @property
    def logo_url(self):
        return self._map.get('logoUrl')

    @logo_url.setter
    def logo_url(self, val):
        self._map['logoUrl'] = val

    @logo_url.deleter
    def logo_url(self):
        del self._map['logoUrl']

    @property
    def sort_order(self):
        return self._map.get('sortOrder')

    @sort_order.setter
    def sort_order(self, val):
        self._map['sortOrder'] = val

    @sort_order.deleter
    def sort_order(self):
        del self._map['sortOrder']

    def json(self):
        return Utils.to_json(self)
