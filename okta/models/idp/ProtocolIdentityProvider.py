class ProtocolIdentityProvider:

    types = {
        'type': str, # enum
        'endpoints': dict,
        'scopes': list,
        'credentials': dict
    }

    def __init__(self):

        self.type = None

        self.endpoints = None

        self.scopes = None

        self.credentials = None