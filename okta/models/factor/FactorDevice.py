from __future__ import unicode_literals


class FactorDevice:

    types = {
        'id': str,
        'status': str
    }

    def __init__(self):

        self.id = None  # str

        self.status = None  # str

        self.links = None  # Map<String, LinksUnion>

        self.embedded = None  # Map<String, Object>
