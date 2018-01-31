class AppLinks:

    types = {
        'login': bool,
        'oidc_client_link': bool
    }

    def __init__(self):

        self.login = None  # bool

        self.oidc_client_link = None # bool