from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.role.Role import Role


class AdminRolesClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/users'
        ApiClient.__init__(self, *args, **kwargs)

    def get_user_admin_roles(self, uid):
        """Get all roles assigned to a user.

        :param uid: the user id
        :type uid: str
        :rtype: list of Role
        """
        response = ApiClient.get_path(self, '/{0}/roles'.format(uid))
        return Utils.deserialize(response.text, Role)

    def assign_roles_to_user(self, uid, role_type):
        """Assigns a role to a user.

        :param uid: str
        :param role_type: str
        :return: Role
        """
        data = {
            'type': role_type
        }
        response = ApiClient.post_path(self, '/{0}/roles'.format(uid), data)
        return Utils.deserialize(response.text, Role)
