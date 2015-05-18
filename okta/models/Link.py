class Link:

    types = {
        'href': str,
        'method': str,
        'type': str,
        'name': str,
        'hints': dict
    }

    def __init__(self):

        self.href = None

        self.method = None

        self.type = None

        self.name = None

        self.hints = None