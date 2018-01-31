class PolicySubject:

    types = {
        'userNameTemplate': dict,
        'filter': str,
        'matchType': str, # enum
        'matchAttribute': str
    }

    def __init__(self):

        self.userNameTemplate = None

        self.filter = None

        self.matchType = None

        self.matchAttribute = None