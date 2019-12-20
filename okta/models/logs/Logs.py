from datetime import datetime
from okta.models.logs.Action import Action
from okta.models.logs.Actor import Actor
from okta.models.logs.Target import Target
from okta.models.logs.Outcome import Outcome



class Logs:

    types = {
        'uuid': str,
        'displayMessage': str,
        'published': datetime,
        'actor': Actor,
        'target': Target,
        'severity': str,
        'outcome': Outcome,
        'eventType': str,
    }

    def __init__(self):

        # unique key for event
        self.uuid = None  # str

        # timestamp when event was published  
        self.published = None  # datetime

        self.actor = None

        self.target = None

        self.target = None

        self.severity = None

        self.outcome = None

        self.eventType = None
