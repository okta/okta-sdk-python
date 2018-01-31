from datetime import datetime
from okta.models.Link import Link
from okta.models.idp.ProtocolIdentityProvider import ProtocolIdentityProvider
from okta.models.idp.PolicyIdentityProvider import PolicyIdentityProvider
from okta.models.idp.PolicySubject import PolicySubject

class IdentityProvider:

    types = {
        'id': str,
        'type': str, # enum
        'name': str,
        'status': str, # enum
        'created': datetime,
        'lastUpdated': datetime,
        'protocol': ProtocolIdentityProvider,
        'policy': PolicyIdentityProvider
    }

    dict_types = {
        '_links': Link
    }

    alt_names = {
        '_links': 'links'
    }

    def __init__(self):

        self.type = None

        self.name = None
        
        self.protocol = None # ProtocolIdentityProvider

        self.policy = None # PolicyIdentityProvider