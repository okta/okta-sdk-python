from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.user.User import User
from okta.models.usergroup.UserGroup import UserGroup
from okta.framework.PagedResults import PagedResults


class UserGroupsClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/groups'
        ApiClient.__init__(self, *args, **kwargs)

    # CRUD

    def get_groups(self, limit=None, query=None):
        """Get a list of UserGroups

        :param limit: maximum number of groups to return
        :type limit: int or None
        :param query: string to search group names
        :type query: str or None
        :rtype: list of UserGroup
        """
        params = {
            'limit': limit,
            'q': query
        }
        response = ApiClient.get_path(self, '/', params=params)
        return Utils.deserialize(response.text, UserGroup)

    def get_paged_groups(self, limit=None, after=None, url=None):
        """Get a paged list of UserGroups

        :param limit: maximum number of groups to return
        :type limit: int or None
        :param after: group id that filtering will resume after
        :type after: str
        :param url: url that returns a list of UserGroup
        :type url: str
        :rtype: PagedResults of UserGroup
        """
        if url:
            response = ApiClient.get(self, url)

        else:
            params = {
                'limit': limit,
                'after': after
            }
            response = ApiClient.get_path(self, '/', params=params)

        return PagedResults(response, User)

    def get_group(self, gid):
        """Get a single group

        :param gid: the group id
        :type gid: str
        :rtype: UserGroup
        """
        response = ApiClient.get_path(self, '/{0}'.format(gid))
        return Utils.deserialize(response.text, UserGroup)

    def get_group_users(self, gid):
        """Get the users of a group

        :param gid: the group id
        :type gid: str
        :rtype: User
        """
        response = ApiClient.get_path(self, '/{0}/users'.format(gid))
        return Utils.deserialize(response.text, User)

    def update_group(self, group):
        """Update a group

        :param group: the group to update
        :type group: UserGroup
        :rtype: UserGroup
        """
        return self.update_group_by_id(group.id, group)

    def update_group_by_id(self, gid, group):
        """Update a group, defined by an id

        :param gid: the target group id
        :type gid: str
        :param group: the data to update the target group
        :type group: UserGroup
        :rtype: UserGroup
        """
        response = ApiClient.put_path(self, '/{0}'.format(gid), group)
        return Utils.deserialize(response.text, UserGroup)

    def create_group(self, group):
        """Create a group

        :param group: the data to create a group
        :type group: UserGroup
        :rtype: UserGroup
        """
        response = ApiClient.post_path(self, '/', group)
        return Utils.deserialize(response.text, UserGroup)

    def delete_group(self, gid):
        """Delete group by target id

        :param gid: the target group id
        :type gid: str
        :return: None
        """
        response = ApiClient.delete_path(self, '/{0}'.format(gid))
        return Utils.deserialize(response.text, UserGroup)

    def add_user_to_group(self, group, user):
        """Add a user to a group

        :param group: the target group
        :type group: UserGroup
        :param user: the target user
        :type user: User
        :return: None
        """
        return self.add_user_to_group_by_id(group.id, user.id)

    def add_user_to_group_by_id(self, gid, uid):
        """Add a user to a group

        :param gid: the target group id
        :type gid: str
        :param uid: the target user id
        :type uid: str
        :return: None
        """
        response = ApiClient.put_path(self, '/{0}/users/{1}'.format(gid, uid))
