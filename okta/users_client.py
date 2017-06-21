"""
 THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""
from .shared.okta_utils import Utils
from .shared.collection import Collection
from .shared.http import Http
from .models import *


class UsersClient(Collection):
    
    def __init__(self, client=None):
        self._path_url = '/api/v1/users'
        self._client = client
        Collection.__init__(self, self._client, self._path_url, User)

    def q(self, q, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'q=' + str(q)
        return Collection(self._client, self._path_url + query, User)
    
    def after(self, after, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'after=' + str(after)
        return Collection(self._client, self._path_url + query, User)
    
    def limit(self, limit, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'limit=' + str(limit)
        return Collection(self._client, self._path_url + query, User)
    
    def filter(self, filter, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'filter=' + str(filter)
        return Collection(self._client, self._path_url + query, User)
    
    def format(self, format, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'format=' + str(format)
        return Collection(self._client, self._path_url + query, User)
    
    def search(self, search, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'search=' + str(search)
        return Collection(self._client, self._path_url + query, User)
    
    def expand(self, expand, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'expand=' + str(expand)
        return Collection(self._client, self._path_url + query, User)
    
    def activate(self, activate, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'activate=' + str(activate)
        return Collection(self._client, self._path_url + query, User)
    
    def provider(self, provider, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'provider=' + str(provider)
        return Collection(self._client, self._path_url + query, User)
    
    def show_all(self, showAll, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'showAll=' + str(showAll)
        return Collection(self._client, self._path_url + query, User)
    
    def send_email(self, sendEmail, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'sendEmail=' + str(sendEmail)
        return Collection(self._client, self._path_url + query, User)
    
    def temp_password(self, tempPassword, **kwargs):
        query = Utils.build_query_params(**kwargs) + 'tempPassword=' + str(tempPassword)
        return Collection(self._client, self._path_url + query, User)
    
    
    def list_users(self, **kwargs):
        """
        Lists users in your organization with pagination in most cases.  A subset of users can be returned that match a supported filter expression or search criteria.
        """
        url = self._client.orgUrl + "/api/v1/users"
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, User)

    def create_user(self, user, **kwargs):
        """
        Creates a new user in your Okta organization with or without credentials.
        """
        url = self._client.orgUrl + "/api/v1/users"
        url += Utils.build_query_params(**kwargs)
        r = self._client.http.post(url, data=Utils.to_json(user))
        return User(Utils.validate_response(r), self)

    def deactivate_or_delete_user(self, user_id):
        url = self._client.orgUrl + "/api/v1/users/{}".format(user_id)
        r = self._client.http.delete(url)
        return r

    def get_user(self, user_id):
        url = self._client.orgUrl + "/api/v1/users/{}".format(user_id)
        r = self._client.http.get(url)
        return User(Utils.validate_response(r), self)

    def update_user(self, user_id, user):
        url = self._client.orgUrl + "/api/v1/users/{}".format(user_id)
        r = self._client.http.put(url, data=Utils.to_json(user))
        return User(Utils.validate_response(r), self)

    def list_app_links(self, user_id, **kwargs):
        url = self._client.orgUrl + "/api/v1/users/{}/appLinks".format(user_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, AppLink)

    def change_password(self, user_id, change_password_request):
        url = self._client.orgUrl + "/api/v1/users/{}/credentials/change_password".format(user_id)
        r = self._client.http.post(url, data=Utils.to_json(change_password_request))
        return UserCredentials(Utils.validate_response(r), self)

    def change_recovery_question(self, user_id, user_credentials):
        url = self._client.orgUrl + "/api/v1/users/{}/credentials/change_recovery_question".format(user_id)
        r = self._client.http.post(url, data=Utils.to_json(user_credentials))
        return UserCredentials(Utils.validate_response(r), self)

    def forgot_password(self, user_id, user_credentials, **kwargs):
        url = self._client.orgUrl + "/api/v1/users/{}/credentials/forgot_password".format(user_id)
        url += Utils.build_query_params(**kwargs)
        r = self._client.http.post(url, data=Utils.to_json(user_credentials))
        return ForgotPasswordResponse(Utils.validate_response(r), self)

    def list_user_groups(self, user_id, **kwargs):
        url = self._client.orgUrl + "/api/v1/users/{}/groups".format(user_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, Group)

    def activate_user(self, user_id, **kwargs):
        url = self._client.orgUrl + "/api/v1/users/{}/lifecycle/activate".format(user_id)
        url += Utils.build_query_params(**kwargs)
        r = self._client.http.post(url)
        return UserActivationToken(Utils.validate_response(r), self)

    def deactivate_user(self, user_id):
        url = self._client.orgUrl + "/api/v1/users/{}/lifecycle/deactivate".format(user_id)
        r = self._client.http.post(url)
        return r

    def expire_password(self, user_id, **kwargs):
        url = self._client.orgUrl + "/api/v1/users/{}/lifecycle/expire_password".format(user_id)
        url += Utils.build_query_params(**kwargs)
        r = self._client.http.post(url)
        return TempPassword(Utils.validate_response(r), self)

    def reset_all_factors(self, user_id):
        url = self._client.orgUrl + "/api/v1/users/{}/lifecycle/reset_factors".format(user_id)
        r = self._client.http.post(url)
        return r

    def reset_password(self, user_id, **kwargs):
        url = self._client.orgUrl + "/api/v1/users/{}/lifecycle/reset_password".format(user_id)
        url += Utils.build_query_params(**kwargs)
        r = self._client.http.post(url)
        return ResetPasswordToken(Utils.validate_response(r), self)

    def suspend_user(self, user_id):
        url = self._client.orgUrl + "/api/v1/users/{}/lifecycle/suspend".format(user_id)
        r = self._client.http.post(url)
        return r

    def unlock_user(self, user_id):
        url = self._client.orgUrl + "/api/v1/users/{}/lifecycle/unlock".format(user_id)
        r = self._client.http.post(url)
        return r

    def unsuspend_user(self, user_id):
        url = self._client.orgUrl + "/api/v1/users/{}/lifecycle/unsuspend".format(user_id)
        r = self._client.http.post(url)
        return r

    def list_assigned_roles(self, user_id, **kwargs):
        url = self._client.orgUrl + "/api/v1/users/{}/roles".format(user_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, Role)

    def add_role_to_user(self, user_id, role):
        url = self._client.orgUrl + "/api/v1/users/{}/roles".format(user_id)
        r = self._client.http.post(url, data=Utils.to_json(role))
        return Role(Utils.validate_response(r), self)

    def remove_role_from_user(self, user_id, role_id):
        url = self._client.orgUrl + "/api/v1/users/{}/roles/{}".format(user_id, role_id)
        r = self._client.http.delete(url)
        return r

    def list_group_targets_for_role(self, user_id, role_id, **kwargs):
        url = self._client.orgUrl + "/api/v1/users/{}/roles/{}/targets/groups".format(user_id, role_id)
        url += Utils.build_query_params(**kwargs)
        return Collection(self, url, Group)

    def remove_group_target_from_role(self, user_id, role_id, group_id):
        url = self._client.orgUrl + "/api/v1/users/{}/roles/{}/targets/groups/{}".format(user_id, role_id, group_id)
        r = self._client.http.delete(url)
        return r

    def add_group_target_to_role(self, user_id, role_id, group_id):
        url = self._client.orgUrl + "/api/v1/users/{}/roles/{}/targets/groups/{}".format(user_id, role_id, group_id)
        r = self._client.http.put(url)
        return r

