class AppLinks:

    types = {
        "appAssignmentId": str,
        "appInstanceId": str,
        "appName": str,
        "credentialsSetup": bool,
        "hidden": bool,
        "id": str,
        "label":  str,
        "linkUrl": str,
        "logoUrl": str,
        "sortOrder": int
    }

    def __init__(self):

        self.appAssignmentId = None  # str

        self.appInstanceId = None  # str

        self.appName = None  # str

        self.credentialsSetup = None  # bool

        self.hidden = None  # bool

        self.id = None  # str

        self.label = None  # str

        self.linkUrl = None  # str

        self.logoUrl = None  # str

        self.sortOrder = None  # int
