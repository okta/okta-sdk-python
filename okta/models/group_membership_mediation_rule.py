"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .group_membership_mediation_actions import GroupMembershipMediationActions
from .group_membership_mediation_conditions import GroupMembershipMediationConditions


class GroupMembershipMediationRule(object):

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
    def actions(self):
        if 'actions' not in self._map:
            self._map['actions'] = {}
        return GroupMembershipMediationActions(self._map['actions'], self._client)

    @actions.setter
    def actions(self, val):
        self._map['actions'] = val

    @actions.deleter
    def actions(self):
        del self._map['actions']

    @property
    def conditions(self):
        if 'conditions' not in self._map:
            self._map['conditions'] = {}
        return GroupMembershipMediationConditions(self._map['conditions'], self._client)

    @conditions.setter
    def conditions(self, val):
        self._map['conditions'] = val

    @conditions.deleter
    def conditions(self):
        del self._map['conditions']

    @property
    def created(self):
        return self._map.get('created')

    @created.setter
    def created(self, val):
        self._map['created'] = val

    @created.deleter
    def created(self):
        del self._map['created']

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
    def last_updated(self):
        return self._map.get('lastUpdated')

    @last_updated.setter
    def last_updated(self, val):
        self._map['lastUpdated'] = val

    @last_updated.deleter
    def last_updated(self):
        del self._map['lastUpdated']

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
    def status(self):
        return self._map.get('status')

    @status.setter
    def status(self, val):
        self._map['status'] = val

    @status.deleter
    def status(self):
        del self._map['status']

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
