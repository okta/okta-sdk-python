from __future__ import unicode_literals


class FactorCatalogEntry:

    types = {
        'factorType': str,
        'provider': str
    }

    def __init__(self):

        self.factorType = None  # str

        self.provider = None  # str
