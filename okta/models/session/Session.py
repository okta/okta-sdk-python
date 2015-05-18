class Session:

    types = {
        'id': str,
        'userId': str,
        'mfaActive': bool,
        'cookieToken': str,
        'cookieTokenUrl': str
    }

    def __init__(self):

        # unique key for session
        self.id = None  # str

        # unique key for the user
        self.userId = None  # str

        # indicates whether the user has enrolled a valid MFA credential
        self.mfaActive = None  # bool

        # One-time token which can be used to obtain a session cookie for your organization
        # by visiting either an applications embed link or a session redirect URL.
        self.cookieToken = None  # str

        # URL for a a transparent 1x1 pixel image which contains a one-time token which
        # when visited sets the session cookie in your browser for your organization.
        self.cookieTokenUrl = None  # str
