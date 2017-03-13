from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.factor.FactorCatalogEntry import FactorCatalogEntry
from okta.models.factor.Factor import Factor
from okta.models.factor.Question import Question
from okta.models.factor.FactorVerificationResponse import FactorVerificationResponse
from okta.models.factor.FactorDevice import FactorDevice


class FactorsClient(ApiClient):

    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/users'
        ApiClient.__init__(self, *args, **kwargs)

    def get_factors_catalog(self, user_id):
        """Get available factors for a user

        :param user_id: target user id
        :type user_id: str
        :rtype: list of FactorCatalogEntry
        """
        response = ApiClient.get_path(self, '/{0}/factors/catalog'.format(user_id))
        return Utils.deserialize(response.text, FactorCatalogEntry)

    def get_lifecycle_factors(self, user_id):
        """Get enrolled factors for a user

        :param user_id: target user id
        :type user_id: str
        :rtype: list of Factor
        """
        response = ApiClient.get_path(self, '/{0}/factors'.format(user_id))
        return Utils.deserialize(response.text, Factor)

    # FACTOR CRUD

    def get_available_questions(self, user_id):
        """Get available factor questions

        :param user_id: target user id
        :type user_id: str
        :rtype: list of Question
        """
        response = ApiClient.get_path(self, '/{0}/factors/questions'.format(user_id))
        return Utils.deserialize(response.text, Question)

    def enroll_factor(self, user_id, factor_enroll_request, update_phone=None):
        """Enroll a user into a factor

        :param user_id: target user id
        :type user_id: str
        :param factor_enroll_request: the details to enroll the user
        :type factor_enroll_request: FactorEnrollRequest
        :param update_phone: whether to update the user's phone during enrollment
        :type update_phone: bool
        :rtype: Factor
        """
        params = {
            'updatePhone': update_phone
        }
        response = ApiClient.post_path(self, '/{0}/factors'.format(user_id), factor_enroll_request, params=params)
        return Utils.deserialize(response.text, Factor)

    def get_factor(self, user_id, user_factor_id):
        """Get information about an enrolled factor

        :param user_id: target user id
        :type user_id: str
        :param user_factor_id: target factor id
        :type user_factor_id: str
        :rtype: Factor
        """
        response = ApiClient.get_path(self, '/{0}/factors/{1}'.format(user_id, user_factor_id))
        return Utils.deserialize(response.text, Factor)

    def update_factor(self, user_id, user_factor_id, factor_enroll_request):
        """Update an enrolled factor

        :param user_id: target user id
        :type user_id: str
        :param user_factor_id: target factor id
        :type user_factor_id: str
        :param factor_enroll_request: data to update the factor
        :type factor_enroll_request: FactorEnrollRequest
        :rtype: Factor
        """
        response = ApiClient.put_path(self, '/{0}/factors/{1}'.format(user_id, user_factor_id), factor_enroll_request)
        return Utils.deserialize(response.text, Factor)

    def reset_factor(self, user_id, user_factor_id):
        """Reset an enrolled factor

        :param user_id: target user id
        :type user_id: str
        :param user_factor_id: target factor id
        :type user_factor_id: str
        :rtype: None
        """
        ApiClient.delete_path(self, '/{0}/factors/{1}'.format(user_id, user_factor_id))

    # FACTOR LIFECYCLE

    def activate_factor(self, user_id, user_factor_id, passcode, next_passcode=None):
        """Activate an enrolled factor

        :param user_id: target user id
        :type user_id: str
        :param user_factor_id: target factor id
        :type user_factor_id: str
        :param passcode: code required for activation
        :type passcode: str
        :param next_passcode: code usually required for TOTP
        :type next_passcode: str
        :rtype: Factor
        """
        request = {
            'passCode': passcode,
            'next_passcode': next_passcode
        }
        response = ApiClient.post_path(self, '/{0}/factors/{1}/lifecycle/activate'.format(user_id, user_factor_id), request)
        return Utils.deserialize(response.text, Factor)

    def resend_code(self, user_id, user_factor_id):
        """Resend code for a factor

        :param user_id: target user id
        :type user_id: str
        :param user_factor_id: target factor id
        :type user_factor_id: str
        :return:
        """
        response = ApiClient.post_path(self, '/{0}/factors/{1}/resend'.format(user_id, user_factor_id))
        return Utils.deserialize(response.text, Factor)

    def verify_factor(self, user_id, user_factor_id, activation_token=None, answer=None, passcode=None, next_passcode=None):
        """Verify an enrolled factor

        :param user_id: target user id
        :type user_id: str
        :param user_factor_id: target factor id
        :type user_factor_id: str
        :param activation_token: token required for activation
        :type activation_token: str
        :param answer: answer usually required for a question factor
        :type answer: str
        :param passcode: code required for verification
        :type passcode: str
        :param next_passcode: code usually required for TOTP
        :type next_passcode: str
        :return:
        """
        request = {
            'activationToken': activation_token,
            'answer': answer,
            'passCode': passcode,
            'nextPassCode': next_passcode
        }
        response = ApiClient.post_path(self, '/{0}/factors/{1}/verify'.format(user_id, user_factor_id), request)
        return Utils.deserialize(response.text, FactorVerificationResponse)

    # FACTOR DEVICE CRUD

    def enroll_factor_device(self, user_id, factor_enroll_request):
        """Enroll a factor device for a user

        :param user_id: target user id
        :type user_id: str
        :param factor_enroll_request: data to enroll the factor device
        :type factor_enroll_request: FactorEnrollRequest
        :rtype: FactorDevice
        """
        response = ApiClient.post_path(self, '/{0}/devices'.format(user_id), factor_enroll_request)
        return Utils.deserialize(response.text, FactorDevice)

    def get_factor_device(self, user_id, user_factor_id, device_id):
        """Get a factor device for a user

        :param user_id: target user id
        :type user_id: str
        :param user_factor_id: target factor id
        :type user_factor_id: str
        :param device_id: target factor device id
        :type device_id: str
        :rtype: FactorDevice
        """
        response = ApiClient.get_path(self, '/{0}/factors/{1}/device/{2}'.format(user_id, user_factor_id, device_id))
        return Utils.deserialize(response.text, FactorDevice)

    def update_factor_device(self, user_id, factor_device_request):
        """Update a factor device for a user

        :param user_id: target user id
        :type user_id: str
        :param factor_device_request: data to update the factor device
        :type factor_device_request: FactorDeviceRequest
        :rtype: FactorDevice
        """
        response = ApiClient.post_path(self, '/{0}/factors/{1}'.format(user_id), factor_device_request)
        return Utils.deserialize(response.text, FactorDevice)

    # FACTOR DEVICE LIFECYCLE

    def activate_factor_device(self, user_id, user_factor_id, device_id, passcode):
        """Activate a factor device for a user

        :param user_id: target user id
        :type user_id: str
        :param user_factor_id: target factor id
        :type user_factor_id: str
        :param device_id: target factor device id
        :type device_id: str
        :param passcode: code required to activate the factor device
        :type passcode: str
        :rtype: FactorDevice
        """
        request = {
            'passCode': passcode
        }
        response = ApiClient.post_path(self, '/{0}/factors/{1}/devices/{2}/lifecycle/activate'.format(
            user_id, user_factor_id, device_id), request)
        return Utils.deserialize(response.text, Factor)