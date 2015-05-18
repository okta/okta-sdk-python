from okta.models.Embedded import Embedded


class AuthResult:

    types = {
        'stateToken': str,
        'status': str,
        'expiresAt': str,
        'relayState': str,
        'factorResult': str,
        'factorResultMessage': str,
        'recoveryToken': str,
        'sessionToken': str,
        'idToken': str,
        '_embedded': Embedded
    }

    alt_names = {
        '_embedded': 'embedded'
    }

    def __init__(self):

        self.stateToken = None  # str

        self.status = None  # str

        self.expiresAt = None  # str

        self.relayState = None  # str

        self.factorResult = None  # str

        self.factorResultMessage = None  # str

        self.recoveryToken = None  # str

        self.sessionToken = None  # str

        self.idToken = None  # str

        self.embedded = None # Embedded