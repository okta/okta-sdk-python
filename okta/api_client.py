"""
 THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
import requests
import os
from .shared.okta_utils import Utils
from .shared.collection import Collection
from .shared.http import Http
from .models import *


class Client:

    USER_AGENT = Utils.get_okta_user_agent()

    def __init__(self, **kwargs):
        
        # Set configuration values from kwargs
        if kwargs:
            self.__dict__.update(kwargs)
        else:
            # Default
            self.__dict__.update(
                {
                    'orgUrl': None,
                    'token': None,
                    'headers': None
                }
            )
        
        for key, value in self.__dict__.items():
            # Verify each attr is set
            if value is None:
                # Get environment or yaml config
                setattr(self, key, Utils.get_config(key))

        # Set Authorization and User-Agent Header
        try:
            getattr(self, "headers")
            # Set default header, unless overriden
            self.headers['Authorization'] = self.headers.get(
                'Authorization',
                'SSWS {}'.format(self.token)
            )
            self.headers['User-Agent'] = self.headers.get(
                'User-Agent',
                self.USER_AGENT
            )
        except AttributeError:
            # Set default headers
            self.headers = {
                'Authorization': 'SSWS {}'.format(self.token),
                'User-Agent': self.USER_AGENT
            }
        self.http = Http(self.headers)

    def list_groups(self, **kwargs):
        """
        Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query.
        """
        url = self.orgUrl + "/api/v1/groups"
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, UserGroup)

    def create_group(self, user_group):
        """
        Adds a new group with `OKTA_GROUP` type to your organization.
        """
        url = self.orgUrl + "/api/v1/groups"
        r = self.http.post(url, data=Utils.to_json(user_group))
        return UserGroup(Utils.validate_response(r), self)

    def list_rules(self, **kwargs):
        """
        Lists all group rules for your organization.
        """
        url = self.orgUrl + "/api/v1/groups/rules"
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, GroupMembershipMediationRule)

    def create_rule(self, group_membership_mediation_rule):
        """
        Creates a group rule to dynamically add users to the specified group if they match the condition
        """
        url = self.orgUrl + "/api/v1/groups/rules"
        r = self.http.post(url, data=Utils.to_json(group_membership_mediation_rule))
        return GroupMembershipMediationRule(Utils.validate_response(r), self)

    def delete_rule(self, rule_id, **kwargs):
        url = self.orgUrl + "/api/v1/groups/rules/{}".format(rule_id)
        url += Utils.build_query_params(**kwargs)
        r = self.http.delete(url)
        return r

    def get_rule(self, rule_id):
        url = self.orgUrl + "/api/v1/groups/rules/{}".format(rule_id)
        r = self.http.get(url)
        return GroupMembershipMediationRule(Utils.validate_response(r), self)

    def update_rule(self, rule_id, group_membership_mediation_rule):
        url = self.orgUrl + "/api/v1/groups/rules/{}".format(rule_id)
        r = self.http.put(url, data=Utils.to_json(group_membership_mediation_rule))
        return GroupMembershipMediationRule(Utils.validate_response(r), self)

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
        return UserGroup(Utils.validate_response(r), self)

    def update_group(self, group_id, user_group):
        url = self.orgUrl + "/api/v1/groups/{}".format(group_id)
        r = self.http.put(url, data=Utils.to_json(user_group))
        return UserGroup(Utils.validate_response(r), self)

    def get_user_group_stats(self, group_id):
        url = self.orgUrl + "/api/v1/groups/{}/stats".format(group_id)
        r = self.http.get(url)
        return UserGroupStats(Utils.validate_response(r), self)

    def list_group_users(self, group_id, **kwargs):
        url = self.orgUrl + "/api/v1/groups/{}/users".format(group_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, User)

    def remove_user_from_group(self, group_id, user_id):
        url = self.orgUrl + "/api/v1/groups/{}/users/{}".format(group_id, user_id)
        r = self.http.delete(url)
        return r

    def add_user_to_group(self, group_id, user_id):
        url = self.orgUrl + "/api/v1/groups/{}/users/{}".format(group_id, user_id)
        r = self.http.put(url)
        return r

    def list_users(self, **kwargs):
        """
        Lists users in your organization with pagination in most cases.  A subset of users can be returned that match a supported filter expression or search criteria.
        """
        url = self.orgUrl + "/api/v1/users"
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, User)

    def create_user(self, user, **kwargs):
        """
        Creates a new user in your Okta organization with or without credentials.
        """
        url = self.orgUrl + "/api/v1/users"
        url += Utils.build_query_params(**kwargs)
        r = self.http.post(url, data=Utils.to_json(user))
        return User(Utils.validate_response(r), self)

    def deactivate_or_delete_user(self, user_id):
        url = self.orgUrl + "/api/v1/users/{}".format(user_id)
        r = self.http.delete(url)
        return r

    def get_user(self, user_id):
        url = self.orgUrl + "/api/v1/users/{}".format(user_id)
        r = self.http.get(url)
        return User(Utils.validate_response(r), self)

    def update_user_with_defaults(self, user_id, user):
        url = self.orgUrl + "/api/v1/users/{}".format(user_id)
        r = self.http.post(url, data=Utils.to_json(user))
        return User(Utils.validate_response(r), self)

    def update_user(self, user_id, user):
        url = self.orgUrl + "/api/v1/users/{}".format(user_id)
        r = self.http.put(url, data=Utils.to_json(user))
        return User(Utils.validate_response(r), self)

    def list_app_links(self, user_id, **kwargs):
        url = self.orgUrl + "/api/v1/users/{}/appLinks".format(user_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, AppLink)

    def change_password(self, user_id, change_password_credentials):
        url = self.orgUrl + "/api/v1/users/{}/credentials/change_password".format(user_id)
        r = self.http.post(url, data=Utils.to_json(change_password_credentials))
        return UserCredentials(Utils.validate_response(r), self)

    def change_recovery_question(self, user_id, user_credentials):
        url = self.orgUrl + "/api/v1/users/{}/credentials/change_recovery_question".format(user_id)
        r = self.http.post(url, data=Utils.to_json(user_credentials))
        return UserCredentials(Utils.validate_response(r), self)

    def forgot_password_with_recovery_answer(self, user_id, user_credentials, **kwargs):
        url = self.orgUrl + "/api/v1/users/{}/credentials/forgot_password".format(user_id)
        url += Utils.build_query_params(**kwargs)
        r = self.http.post(url, data=Utils.to_json(user_credentials))
        return BaseCredentialsObject(Utils.validate_response(r), self)

    def list_user_groups(self, user_id, **kwargs):
        url = self.orgUrl + "/api/v1/users/{}/groups".format(user_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, UserGroup)

    def activate_user(self, user_id, **kwargs):
        url = self.orgUrl + "/api/v1/users/{}/lifecycle/activate".format(user_id)
        url += Utils.build_query_params(**kwargs)
        r = self.http.post(url)
        return ActivationToken(Utils.validate_response(r), self)

    def lifecycle_deactivate_user(self, user_id):
        url = self.orgUrl + "/api/v1/users/{}/lifecycle/deactivate".format(user_id)
        r = self.http.post(url)
        return r

    def forgot_password(self, user_id, **kwargs):
        url = self.orgUrl + "/api/v1/users/{}/lifecycle/forgot_password".format(user_id)
        url += Utils.build_query_params(**kwargs)
        r = self.http.post(url)
        return ResetPasswordToken(Utils.validate_response(r), self)

    def reset_all_factors(self, user_id):
        url = self.orgUrl + "/api/v1/users/{}/lifecycle/reset_factors".format(user_id)
        r = self.http.post(url)
        return r

    def suspend_user(self, user_id):
        url = self.orgUrl + "/api/v1/users/{}/lifecycle/suspend".format(user_id)
        r = self.http.post(url)
        return r

    def unlock_user(self, user_id):
        url = self.orgUrl + "/api/v1/users/{}/lifecycle/unlock".format(user_id)
        r = self.http.post(url)
        return r

    def unsuspend_user(self, user_id):
        url = self.orgUrl + "/api/v1/users/{}/lifecycle/unsuspend".format(user_id)
        r = self.http.post(url)
        return r

    def list_assigned_roles(self, user_id, **kwargs):
        url = self.orgUrl + "/api/v1/users/{}/roles".format(user_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, MediationRoleAssignment)

    def assign_role_to_user(self, user_id, mediation_role_assignment):
        url = self.orgUrl + "/api/v1/users/{}/roles".format(user_id)
        r = self.http.post(url, data=Utils.to_json(mediation_role_assignment))
        return MediationRoleAssignment(Utils.validate_response(r), self)

    def unassign_role_from_user(self, user_id, role_id):
        url = self.orgUrl + "/api/v1/users/{}/roles/{}".format(user_id, role_id)
        r = self.http.delete(url)
        return r

    def get_role_for_user(self, user_id, role_id):
        url = self.orgUrl + "/api/v1/users/{}/roles/{}".format(user_id, role_id)
        r = self.http.get(url)
        return MediationRoleAssignment(Utils.validate_response(r), self)

    def list_group_targets_for_role(self, user_id, role_id, **kwargs):
        url = self.orgUrl + "/api/v1/users/{}/roles/{}/targets/groups".format(user_id, role_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, UserGroup)

    def remove_group_target_from_role(self, user_id, role_id, group_id):
        url = self.orgUrl + "/api/v1/users/{}/roles/{}/targets/groups/{}".format(user_id, role_id, group_id)
        r = self.http.delete(url)
        return r

    def add_group_target_to_role(self, user_id, role_id, group_id):
        url = self.orgUrl + "/api/v1/users/{}/roles/{}/targets/groups/{}".format(user_id, role_id, group_id)
        r = self.http.put(url)
        return r

