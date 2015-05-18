class Accessibility:

    types = {
        'selfService': bool,
        'errorRedirectUrl': str
    }

    def __init__(self):

        # Enable self-service application assignment
        self.selfService = None  # bool

        # Custom error page for this application
        self.errorRedirectUrl = None  # str
