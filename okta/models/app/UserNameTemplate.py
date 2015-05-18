class UserNameTemplate:

    types = {
        'template': str,
        'type': str,
        'userSuffix': str
    }

    def __init__(self):

        # mapping expression for username
        self.template = None  # str

        # type of mapping expression
        self.type = None  # enum

        # suffix for built-in mapping expressions
        self.userSuffix = None  # str
