class Error:
    """
    Base Error Class
    """

    def __init__(self):
        self.message = ""

    def __repr__(self):
        return str({
            "message": self.message
        })
