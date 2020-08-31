from __future__ import unicode_literals


class TrustedOriginResponse:

    types = {
        'status': str,
        'name': str,
        'origin': str,
    }

    def __init__(self):

        self.status = None  # str
        self.name = None  # str
        self.origin = None  # str
