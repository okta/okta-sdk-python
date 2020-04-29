from __future__ import unicode_literals


class Provider:

    types = {
        'type': str,
        'name': str
    }

    def __init__(self):

        self.type = None  # str

        self.name = None  # str
