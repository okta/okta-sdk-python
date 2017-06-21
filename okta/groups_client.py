"""
 THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .shared.okta_utils import Utils
from .shared.collection import Collection
from .shared.http import Http
from .models import *


class GroupsClient(Collection):

    def __init__(self, client=None):
        self.path_url = '/api/v1/groups'
        Collection.__init__(self, Group, client, self.path_url)

    def list_groups(self, **kwargs):
        """
        Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query.
        """
        url = self.orgUrl + "/api/v1/groups"
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, Group)

    def create_group(self, group):
        """
        Adds a new group with `OKTA_GROUP` type to your organization.
        """
        url = self.orgUrl + "/api/v1/groups"
        r = self.http.post(url, data=Utils.to_json(group))
        return Group(Utils.validate_response(r), self)

    def list_rules(self, **kwargs):
        """
        Lists all group rules for your organization.
        """
        url = self.orgUrl + "/api/v1/groups/rules"
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, GroupRule)

    def create_rule(self, group_rule):
        """
        Creates a group rule to dynamically add users to the specified group if they match the condition
        """
        url = self.orgUrl + "/api/v1/groups/rules"
        r = self.http.post(url, data=Utils.to_json(group_rule))
        return GroupRule(Utils.validate_response(r), self)

    def delete_rule(self, rule_id, **kwargs):
        url = self.orgUrl + "/api/v1/groups/rules/{}".format(rule_id)
        url += Utils.build_query_params(**kwargs)
        r = self.http.delete(url)
        return r

    def get_rule(self, rule_id):
        url = self.orgUrl + "/api/v1/groups/rules/{}".format(rule_id)
        r = self.http.get(url)
        return GroupRule(Utils.validate_response(r), self)

    def update_rule(self, rule_id, group_rule):
        url = self.orgUrl + "/api/v1/groups/rules/{}".format(rule_id)
        r = self.http.put(url, data=Utils.to_json(group_rule))
        return GroupRule(Utils.validate_response(r), self)

    def activate_rule(self, rule_id):
        url = self.orgUrl + "/api/v1/groups/rules/{}/lifecycle/activate".format(rule_id)
        r = self.http.post(url)
        return r

    def deactivate_rule(self, rule_id):
        url = self.orgUrl + "/api/v1/groups/rules/{}/lifecycle/deactivate".format(rule_id)
        r = self.http.post(url)
        return r

    def delete_group(self, group_id):
        url = self.orgUrl + "/api/v1/groups/{}".format(group_id)
        r = self.http.delete(url)
        return r

    def get_group(self, group_id, **kwargs):
        url = self.orgUrl + "/api/v1/groups/{}".format(group_id)
        url += Utils.build_query_params(**kwargs)
        r = self.http.get(url)
        return Group(Utils.validate_response(r), self)

    def update_group(self, group_id, group):
        url = self.orgUrl + "/api/v1/groups/{}".format(group_id)
        r = self.http.put(url, data=Utils.to_json(group))
        return Group(Utils.validate_response(r), self)

    def get_group_stats(self, group_id):
        url = self.orgUrl + "/api/v1/groups/{}/stats".format(group_id)
        r = self.http.get(url)
        return GroupStats(Utils.validate_response(r), self)

    def list_group_users(self, group_id, **kwargs):
        url = self.orgUrl + "/api/v1/groups/{}/users".format(group_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, User)

    def remove_group_user(self, group_id, user_id):
        url = self.orgUrl + "/api/v1/groups/{}/users/{}".format(group_id, user_id)
        r = self.http.delete(url)
        return r

    def add_user_to_group(self, group_id, user_id):
        url = self.orgUrl + "/api/v1/groups/{}/users/{}".format(group_id, user_id)
        r = self.http.put(url)
        return r

