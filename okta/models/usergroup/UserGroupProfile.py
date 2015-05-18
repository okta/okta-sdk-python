class UserGroupProfile:

    types = {
        'name': str,
        'description': str,
        'samAccountName': str,
        'dn': str,
        'windowsDomainQualifiedName': str,
        'externalId': str
    }

    def __init__(self):

        # name of the group
        self.name = None  # str

        # description of the group
        self.description = None  # str

        # pre-windows 2000 name of the windows group
        self.samAccountName = None  # str

        # the distinguished name of the windows group
        self.dn = None  # str

        # fully-qualified name of the windows group
        self.windowsDomainQualifiedName = None  # str

        # base-64 encoded GUID (objectGUID) of the windows group
        self.externalId = None  # str
