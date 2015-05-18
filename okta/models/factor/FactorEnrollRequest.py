from Verification import Verification


class FactorEnrollRequest:

    types = {
        'factorType': str,
        'provider': str,
        'verify': Verification,
        'profile': dict
    }

    def __init__(self):

        self.factorType = None  # str

        self.provider = None  # str

        self.verify = None  # Verification

        self.profile = None  # Map<String, Object>
