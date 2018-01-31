from okta.models.idp.PolicySubject import PolicySubject

class PolicyIdentityProvider:

    types = {
        'provisioning': dict,
        'accountLink': dict,
        'subject': PolicySubject,
        'maxClockSkew': int
    }

    def __init__(self):

        self.provisioning = None

        self.accountLink = None

        self.subject = None

        self.maxClockSkew = None