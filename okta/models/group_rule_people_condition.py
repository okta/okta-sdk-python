"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .group_rule_group_condition import GroupRuleGroupCondition
from .group_rule_user_condition import GroupRuleUserCondition


class GroupRulePeopleCondition(object):

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
    def groups(self):
        if 'groups' not in self._map:
            self._map['groups'] = {}
        return GroupRuleGroupCondition(self._map['groups'], self._client)

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
        return GroupRuleUserCondition(self._map['users'], self._client)

    @users.setter
    def users(self, val):
        self._map['users'] = val

    @users.deleter
    def users(self):
        del self._map['users']

    def json(self):
        return Utils.to_json(self)
