class FactorVerificationResponse:

    types = {
        'factorResult': str,
        'state': str,
        'factorResultMessage': str,
        'expiryTime': str
    }

    def __init__(self):

        self.factorResult = None  # str

        self.state = None  # str

        self.factorResultMessage = None  # str

        self.expiryTime = None  # str

        self.links = None  # Map<String, LinksUnion>

        self.embedded = None  # Map<String, Object>
