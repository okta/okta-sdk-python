class OAuthClientSettings:

    types = {
        'client_uri': str,
        'logo_uri': str,
        'redirect_uris': list,
        'response_types': list,
        'grant_types': list,
        'application_type': str
    }

    def __init__(self):

        self.client_uri = None

        self.logo_uri = None

        self.redirect_uris = None

        self.response_types = None

        self.grant_types = None

        self.application_type = None