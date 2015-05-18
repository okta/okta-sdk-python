class OrgAuthFactor:

    types = {
        'id': str,
        'factorType': str,
        'provider': str,
        'status': str
    }

    def __init__(self):

        self.id = None  # str

        self.factorType = None  # str

        self.provider = None  # str

        self.status = None  # str

        self.links = None  # Map<String, Object>

        self.embedded = None  # Map<String, Object>
