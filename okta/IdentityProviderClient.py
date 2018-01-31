from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.idp.IdentityProvider import IdentityProvider


class IdentityProviderClient(ApiClient):

    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/idps'
        ApiClient.__init__(self, *args, **kwargs)

    # CRUD

    def create_identity_provider(self, identity_provider):
        """Create an identity provider

        :param identity_provider: the data to create the idp
        :type app_instance: IdentityProvider
        :rtype: IdentityProvider
        """
        response = ApiClient.post_path(self, '/', identity_provider)
        return Utils.deserialize(response.text, IdentityProvider)