class OAuthClientCredentials:

    types = {
        'autoKeyRotation': bool,
        'client_id': str,
        'client_secret': str,
        'token_endpoint_auth_method': str
    }

    def __init__(self):
        
        self.autoKeyRotation = None

        self.client_id = None

        self.client_secret = None

        self.token_endpoint_auth_method = None