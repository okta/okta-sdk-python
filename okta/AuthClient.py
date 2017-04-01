from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.auth.AuthResult import AuthResult


class AuthClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/authn'
        ApiClient.__init__(self, *args, **kwargs)

    def authenticate(self, username, password,
                     relay_state=None, response_type=None, force_mfa=None, context=None):
        """Begin the authentication process with a username and password

        :param username: user's username
        :type username: str
        :param password: user's password
        :type password: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :param response_type: the type of session to return (session_token or session_token_url usually)
        :type response_type: str
        :param force_mfa: whether to force mfa even if the auth is exempt
        :type force_mfa: bool
        :param context: contextual info about the auth request like ip and location
        :type context: Context
        :rtype: AuthResult
        """
        request = {
            'username': username,
            'password': password,
            'relayState': relay_state,
            'context': context
        }

        params = {
            'force_mfa': force_mfa,
            'response_type': response_type
        }

        response = ApiClient.post_path(self, '/', request, params=params)
        return Utils.deserialize(response.text, AuthResult)

    def auth_with_factor(self, state_token, factor_id, passcode,
                         relay_state=None, remember_device=None):
        """Continue authentication with an MFA attempt

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param factor_id: target factor id
        :type factor_id: str
        :param passcode: passcode required for authenticating the factor
        :type passcode: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :param remember_device: whether to remember this device to avoid requiring MFA next time
        :type remember_device: bool
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'passCode': passcode,
            'relayState': relay_state
        }

        params = {
            'rememberDevice': remember_device
        }

        response = ApiClient.post_path(self, '/factors/{0}/verify'.format(factor_id),
                                      request, params=params)
        return Utils.deserialize(response.text, AuthResult)

    # MFA MANAGEMENT

    def enroll_factor(self, state_token, factor_type, provider, profile, relay_state=None):
        """Enroll in an MFA factor during the auth flow. Usually only encountered if MFA is required for authentication

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param factor_type: type of factor (sms, token, question, token:software:totp, token:hardware etc)
        :type factor_type: str
        :param provider: factor provider (OKTA, RSA, SYMANTEC, GOOGLE etc)
        :type provider: str
        :param profile: factor profile that depends on the factor type
        :type profile: FactorProfile
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'factorType': factor_type,
            'provider': provider,
            'profile': profile,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/factors', request)
        return Utils.deserialize(response.text, AuthResult)

    def activate_factor(self, state_token, factor_id, passcode, relay_state=None):
        """Activate an MFA factor during the auth flow

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param factor_id: target factor id
        :type factor_id: str
        :param passcode: passcode required to activate the factor
        :type passcode: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'passCode': passcode,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/factors/{0}/lifecycle/activate'.format(factor_id), request)
        return Utils.deserialize(response.text, AuthResult)

    def resend_code(self, state_token, factor_id, relay_state=None):
        """Resend an a passcode for an authentication factor

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param factor_id: target factor id
        :type factor_id: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/factors/{0}/lifecycle/resend'.format(factor_id), request)
        return Utils.deserialize(response.text, AuthResult)

    # CREDENTIAL MANAGEMENT

    def change_password(self, state_token, old_password, new_password, relay_state=None):
        """Change a user's password during an authentication flow

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param old_password: user's current password
        :type old_password: str
        :param new_password: user's desired password
        :type new_password: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'oldPassword': old_password,
            'newPassword': new_password,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/credentials/change_password', request)
        return Utils.deserialize(response.text, AuthResult)

    def reset_password(self, state_token, new_password, relay_state=None):
        """Reset a user's password during an authentication flow

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param new_password: user's desired password
        :type new_password: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'newPassword': new_password,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/credentials/reset_password', request)
        return Utils.deserialize(response.text, AuthResult)

    def forgot_password(self, username, relay_state=None):
        """Initiate a forgot password flow for a user

        :param username: user's username
        :type username: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'username': username,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/recovery/password', request)
        return Utils.deserialize(response.text, AuthResult)

    def forgot_password_answer(self, state_token, security_answer, new_password, relay_state=None):
        """Answer the forgot password during an authentication flow

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param security_answer: answer to a user's security question
        :type security_answer: str
        :param new_password: user's desired password
        :type new_password: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'securityAnswer': security_answer,
            'newPassword': new_password,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/recovery/answer', request)
        return Utils.deserialize(response.text, AuthResult)

    # RECOVERY

    def validate_recovery_token(self, recovery_token, relay_state=None):
        """Validate a token for recovery

        :param recovery_token: token distributed to end-user via out-of-band mechanism such as email
        :type recovery_token: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'recoveryToken': recovery_token,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/recovery/token', request)
        return Utils.deserialize(response.text, AuthResult)

    def unlock_account(self, username, relay_state=None):
        """Begin unlocking an account

        :param username: user's username
        :type username: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'username': username,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/recovery/unlock', request)
        return Utils.deserialize(response.text, AuthResult)

    def unlock_account_answer(self, state_token, security_answer, relay_state=None):
        """Unlock an account during an authentication

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param security_answer: answer to the user's security question
        :type security_answer: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'securityAnswer': security_answer,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/recovery/answer', request)
        return Utils.deserialize(response.text, AuthResult)

    # STATE MANAGEMENT

    def previous_state(self, state_token, relay_state=None):
        """Get the previous state of an in-progress authentication

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/previous', request)
        return Utils.deserialize(response.text, AuthResult)

    def get_status(self, state_token, relay_state=None):
        """Get the status of an in-progress authentication

        :param state_token: current state token from the previous AuthResult
        :type state_token: str
        :param relay_state: data that will persist for the lifetime of the authentication or recovery token
        :type relay_state: str or None
        :rtype: AuthResult
        """
        request = {
            'stateToken': state_token,
            'relayState': relay_state
        }

        response = ApiClient.post_path(self, '/', request)
        return Utils.deserialize(response.text, AuthResult)

    def verify_transaction(self, factor_id, transaction_id, user_response):
        """Verify a transaction

        :param factor_id: target factor id
        :type factor_id: str
        :param transaction_id: target transaction id
        :type transaction_id: str
        :param user_response: APPROVE or REJECT
        :type user_response: str
        :rtype: AuthResult
        """
        request = {
            'result': user_response
        }

        response = ApiClient.post_path(self, '/factors/{0}/transactions/{1}/verify'.format(factor_id, transaction_id), request)
        return Utils.deserialize(response.text, AuthResult)