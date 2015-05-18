class Target:

    types = {
        'id': str,
        'displayName': str,
        'objectType': str
    }

    def __init__(self):

        # Unique key for actor
        self.id = None  # str

        # Name of actor used for display purposes
        self.displayName = None  # str

        # User, Client, or AppInstance
        self.objectType = None  # str
