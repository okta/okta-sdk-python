"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .group_membership_mediation_group_condition import GroupMembershipMediationGroupCondition
from .group_membership_mediation_user_condition import GroupMembershipMediationUserCondition


class GroupMembershipMediationPeopleCondition(object):

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
    def groups(self):
        if 'groups' not in self._map:
            self._map['groups'] = {}
        return GroupMembershipMediationGroupCondition(self._map['groups'], self._client)

    @groups.setter
    def groups(self, val):
        self._map['groups'] = val

    @groups.deleter
    def groups(self):
        del self._map['groups']

    @property
    def users(self):
        if 'users' not in self._map:
            self._map['users'] = {}
        return GroupMembershipMediationUserCondition(self._map['users'], self._client)

    @users.setter
    def users(self, val):
        self._map['users'] = val

    @users.deleter
    def users(self):
        del self._map['users']

