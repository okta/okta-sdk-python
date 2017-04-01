from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.framework.PagedResults import PagedResults
from okta.models.user import AppLinks
from okta.models.user.User import User
from okta.models.user.TempPassword import TempPassword
from okta.models.user.ResetPasswordToken import ResetPasswordToken
from okta.models.user.LoginCredentials import LoginCredentials


class UsersClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/users'
        ApiClient.__init__(self, *args, **kwargs)

    # CRUD

    def get_users(self, limit=None, query=None, filter_string=None):
        """Get a list of Users

        :param limit: maximum number of users to return
        :type limit: int or None
        :param query: string to search users' first names, last names, and emails
        :type query: str or None
        :param filter_string: string to filter users
        :type filter_string: str or None
        :rtype: list of User
        """
        params = {
            'limit': limit,
            'q': query,
            'filter': filter_string
        }
        response = ApiClient.get_path(self, '/', params=params)
        return Utils.deserialize(response.text, User)

    def get_user(self, uid):
        """Get a single user

        :param uid: the user id or login
        :type uid: str
        :rtype: User
        """
        response = ApiClient.get_path(self, '/{0}'.format(uid))
        return Utils.deserialize(response.text, User)

    def get_user_applinks(self, uid):
        """Get applinks of a single user

        :param uid: the user id or login
        :type uid: str
        :rtype: AppLinks
        """
        response = ApiClient.get_path(self, '/{0}/appLinks'.format(uid))
        return Utils.deserialize(response.text, AppLinks)

    def update_user(self, user):
        """Update a user

        :param user: the user to update
        :type user: User
        :rtype: User
        """
        return self.update_user_by_id(user.id, user)

    def update_user_by_id(self, uid, user):
        """Update a user, defined by an id

        :param uid: the target user id
        :type uid: str
        :param user: the data to update the target user
        :type user: User
        :rtype: User
        """
        response = ApiClient.put_path(self, '/{0}'.format(uid), user)
        return Utils.deserialize(response.text, User)

    def create_user(self, user, activate=None):
        """Create a user

        :param user: the data to create a user
        :type user: User
        :param activate: whether to activate the user
        :type activate: bool
        :rtype: User
        """
        if activate is None:
            response = ApiClient.post_path(self, '/', user)
        else:
            params = {
                'activate': activate
            }
            response = ApiClient.post_path(self, '/', user, params=params)
        return Utils.deserialize(response.text, User)

    def delete_user(self, uid):
        """Delete user by target id

        :param uid: the target user id
        :type uid: str
        :return: None
        """
        response = ApiClient.delete_path(self, '/{0}'.format(uid))
        return Utils.deserialize(response.text, User)

    def get_paged_users(self, limit=None, filter_string=None, after=None, url=None):
        """Get a paged list of Users

        :param limit: maximum number of users to return
        :type limit: int or None
        :param filter_string: string to filter users
        :type filter_string: str or None
        :param after: user id that filtering will resume after
        :type after: str
        :param url: url that returns a list of User
        :type url: str
        :rtype: PagedResults of User
        """
        if url:
            response = ApiClient.get(self, url)
        else:
            params = {
                'limit': limit,
                'after': after,
                'filter': filter_string
            }
            response = ApiClient.get_path(self, '/', params=params)
        return PagedResults(response, User)

    # LIFECYCLE
    
    def activate_user(self, uid):
        """Activate user by target id

        :param uid: the target user id
        :type uid: str
        :return: User
        """
        response = ApiClient.post_path(self, '/{0}/lifecycle/activate'.format(uid))
        return Utils.deserialize(response.text, User)

    def deactivate_user(self, uid):
        """Deactivate user by target id

        :param uid: the target user id
        :type uid: str
        :return: User
        """
        response = ApiClient.post_path(self, '/{0}/lifecycle/deactivate'.format(uid))
        return Utils.deserialize(response.text, User)

    def suspend_user(self, uid):
        """Suspend user by target id

        :param uid: the target user id
        :type uid: str
        :return: User
        """
        response = ApiClient.post_path(self, '/{0}/lifecycle/suspend'.format(uid))
        return Utils.deserialize(response.text, User)

    def unsuspend_user(self, uid):
        """Unsuspend user by target id

        :param uid: the target user id
        :type uid: str
        :return: User
        """
        response = ApiClient.post_path(self, '/{0}/lifecycle/unsuspend'.format(uid))
        return Utils.deserialize(response.text, User)

    def unlock_user(self, uid):
        """Unlock user by target id

        :param uid: the target user id
        :type uid: str
        :return: User
        """
        response = ApiClient.post_path(self, '/{0}/lifecycle/unlock'.format(uid))
        return Utils.deserialize(response.text, User)

    def reset_password(self, uid, send_email=True):
        """Reset user's password by target user id

        :param uid: the target user id
        :type uid: str
        :param send_email: whether a password reset email should be sent
        :type send_email: bool
        :return: None or ResetPasswordToken
        """
        params = {
            'sendEmail': send_email
        }
        response = ApiClient.post_path(self, '/{0}/lifecycle/reset_password'.format(uid), params=params)
        return Utils.deserialize(response.text, ResetPasswordToken)

    def change_password(self, uid, old_password, new_password):
        """Change user's password by target user id

        :param uid: the target user id
        :type uid: str
        :param old_password: the user's old password
        :type old_password: str
        :param new_password: the desired new password
        :type new_password: str
        :return: None or LoginCredentials
        """
        data = {
            'oldPassword': {
                'value': old_password
            },
            'newPassword': {
                'value': new_password
            }
        }
        response = ApiClient.post_path(self, '/{0}/credentials/change_password'.format(uid), data)
        return Utils.deserialize(response.text, LoginCredentials)

    def expire_password(self, uid, temp_password=False):
        """Expire user's password by target user id

        :param uid: the target user id
        :type uid: str
        :param temp_password: whether a temporary password should be set
        :type temp_password: bool
        :return: None or TempPassword
        """
        if not temp_password:
            response = ApiClient.post_path(self, '/{0}/lifecycle/expire_password'.format(uid))
        else:
            params = {
                'tempPassword': temp_password
            }
            response = ApiClient.post_path(self, '/{0}/lifecycle/expire_password'.format(uid), params=params)
        return Utils.deserialize(response.text, TempPassword)

    def reset_factors(self, uid):
        """Reset all user factors by target id

        :param uid: the target user id
        :type uid: str
        :return: None
        """
        response = ApiClient.post_path(self, '/{0}/lifecycle/reset_factors'.format(uid))
        return Utils.deserialize(response.text, User)
