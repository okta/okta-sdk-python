"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .group_membership_mediation_expression_condition import GroupMembershipMediationExpressionCondition
from .group_membership_mediation_group_condition import GroupMembershipMediationGroupCondition
from .group_membership_mediation_people_condition import GroupMembershipMediationPeopleCondition
from .group_membership_mediation_user_condition import GroupMembershipMediationUserCondition


class GroupMembershipMediationConditions(object):

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
    def expression(self):
        if 'expression' not in self._map:
            self._map['expression'] = {}
        return GroupMembershipMediationExpressionCondition(self._map['expression'], self._client)

    @expression.setter
    def expression(self, val):
        self._map['expression'] = val

    @expression.deleter
    def expression(self):
        del self._map['expression']

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
    def people(self):
        if 'people' not in self._map:
            self._map['people'] = {}
        return GroupMembershipMediationPeopleCondition(self._map['people'], self._client)

    @people.setter
    def people(self, val):
        self._map['people'] = val

    @people.deleter
    def people(self):
        del self._map['people']

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

    def json(self):
        return Utils.to_json(self)
