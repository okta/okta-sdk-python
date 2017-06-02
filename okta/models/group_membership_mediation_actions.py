"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .assign_user_to_groups_mediation_action import AssignUserToGroupsMediationAction


class GroupMembershipMediationActions(object):

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
    def assign_user_to_groups(self):
        if 'assignUserToGroups' not in self._map:
            self._map['assignUserToGroups'] = {}
        return AssignUserToGroupsMediationAction(self._map['assignUserToGroups'], self._client)

    @assign_user_to_groups.setter
    def assign_user_to_groups(self, val):
        self._map['assignUserToGroups'] = val

    @assign_user_to_groups.deleter
    def assign_user_to_groups(self):
        del self._map['assignUserToGroups']

