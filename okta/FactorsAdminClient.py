from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.factor.OrgAuthFactor import OrgAuthFactor


class FactorsAdminClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/org'
        ApiClient.__init__(self, *args, **kwargs)

    def get_org_factors(self, filter_string=None):
        """Get a list of OrgAuthFactors

        :param filter_string: string to filter factors
        :type filter_string: str or None
        :rtype: list of OrgAuthFactor
        """
        params = {
            'filter': filter_string
        }
        response = ApiClient.get_path(self, '/factors', params=params)
        return Utils.deserialize(response.text, OrgAuthFactor)

    def activate_org_factor(self, org_factor_id, org_auth_factor=None):
        """Activate OrgAuthFactor

        :param org_factor_id: target factor id
        :type org_factor_id: str
        :param org_auth_factor: additional factor data
        :param org_auth_factor: OrgAuthFactor
        :rtype: OrgAuthFactor
        """
        response = ApiClient.post_path(self, '/factors/{0}/lifecycle/activate'.format(org_factor_id), org_auth_factor)
        return Utils.deserialize(response.text, OrgAuthFactor)

    def deactivate_org_factor(self, org_factor_id):
        """Deactivate OrgAuthFactor

        :param org_factor_id: target factor id
        :type org_factor_id: str
        :rtype: OrgAuthFactor
        """
        response = ApiClient.post_path(self, '/factors/{0}/lifecycle/deactivate'.format(org_factor_id))
        return Utils.deserialize(response.text, OrgAuthFactor)