from Verification import Verification


class FactorDeviceEnrollRequest:

    types = {
        'verify': Verification,
        'profile': dict
    }

    def __init__(self):

        self.verify = None  # Verification

        self.profile = None  # Map<String, Object>
