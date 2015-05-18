from Verification import Verification


class FactorDeviceRequest:

    types = {
        'verify': Verification,
        'profile': dict
    }

    def __init__(self):

        self.verify = None  # Verification

        self.profile = None  # Map<String, Object>

        self.links = None  # Map<String, LinksUnion>

        self.embedded = None  # Map<String, Object>
