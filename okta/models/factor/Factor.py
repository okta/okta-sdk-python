from datetime import datetime
from okta.models.factor.FactorProfile import FactorProfile


class Factor:

    types = {
        'id': str,
        'factorType': str,
        'provider': str,
        'status': str,
        'created': datetime,
        'lastUpdated': datetime,
        'profile': FactorProfile
    }

    def __init__(self):

        # unique key for factor
        self.id = None  # str

        # type of factor
        self.factorType = None  # str

        # factor provider
        self.provider = None  # str

        # status of factor
        self.status = None  # str

        # timestamp when factor was created
        self.created = None  # datetime

        # timestamp when factor was last updated
        self.lastUpdated = None  # datetime

        # profile of a supported factor
        self.profile = None  # FactorProfile

        self.links = None  # Map<String, LinksUnion>

        self.embedded = None  # Map<String, Object>