class Action:

    types = {
        'message': str,
        'categories': str,
        'objectType': str,
        'requestUri': str
    }

    def __init__(self):

        # Description of an action
        self.message = None  # str

        # Categories for an action
        self.categories = None

        # Identifies the unique type of an action
        self.objectType = None  # str

        # Relative uri of the request that generated the event.
        self.requestUri = None  # str
