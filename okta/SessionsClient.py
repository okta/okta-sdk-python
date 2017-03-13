from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.session.Credentials import Credentials
from okta.models.session.Session import Session


class SessionsClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/sessions'
        ApiClient.__init__(self, *args, **kwargs)

    # CRUD

    def create_session(self, username, password, additional_fields=None):
        """Create a session

        :param username: the user's username
        :type username: str
        :param password: the user's password
        :type password: str
        :param additional_fields: additional fields that will be included in the response
        :type additional_fields: str
        :rtype: Session
        """
        creds = Credentials()
        creds.username = username
        creds.password = password
        params = {'additionalFields': additional_fields}
        response = ApiClient.post_path(self, '/', creds, params=params)
        return Utils.deserialize(response.text, Session)

    def create_session_with_cookie_token(self, username, password):
        """Create a session that contains a cookie token

        :param username: the user's username
        :type username: str
        :param password: the user's password
        :type password: str
        :rtype: Session
        """
        return self.create_session(username, password, 'cookieToken')

    def create_session_with_cookie_token_url(self, username, password):
        """Create a session that contains a cookie token url

        :param username: the user's username
        :type username: str
        :param password: the user's password
        :type password: str
        :rtype: Session
        """
        return self.create_session(username, password, 'cookieTokenUrl')

    def create_session_by_session_token(self, session_token, additional_fields=None):
        """Create a session using a session token

        :param session_token: a token that can be exchanged for a session
        :type session_token: str
        :param additional_fields: additional fields that will be included in the response
        :type additional_fields: str
        :rtype: Session
        """
        data = {'sessionToken': session_token}
        params = {'additionalFields': additional_fields}
        response = ApiClient.post_path(self, '/', data, params=params)
        return Utils.deserialize(response.text, Session)

    def validate_session(self, id):
        """Validate a session

        :param id: the target session id
        :rtype: Session
        """
        response = ApiClient.get_path(self, '/{0}'.format(id))
        return Utils.deserialize(response.text, Session)

    def extend_session(self, id):
        """Extend a session's lifespan

        :param id: the target session id
        :rtype: Session
        """
        response = ApiClient.put_path(self, '/{0}'.format(id), None)
        return Utils.deserialize(response.text, Session)

    def clear_session(self, id):
        """Terminate a session

        :param id: the target session id
        :rtype: Session
        """
        ApiClient.delete_path(self, '/{0}'.format(id))