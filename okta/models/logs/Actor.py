class Actor:

    types = {
        'id': str,
        'type': str,
        'alternateId': str,
        'displayName': str,
        'detailEntry': str,
    }

    def __init__(self):

        # Unique key for actor
        self.id = None  # str

        # Name of actor used for display purposes
        self.displayName = None  # str

        self.type = None

        self.alternateId = None

        self.detailEntry = None

