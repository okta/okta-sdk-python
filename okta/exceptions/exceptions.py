class OktaBaseException(Exception):
    pass


class HTTPException(OktaBaseException):
    pass


class OktaAPIException(OktaBaseException):
    pass
