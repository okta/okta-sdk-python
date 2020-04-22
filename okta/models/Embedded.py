from __future__ import unicode_literals

from okta.models.user.User import User
from okta.models.factor.Factor import Factor


class Embedded:

    types = {
        'user': User,
        'factors': Factor
    }

    def __init__(self):

        self.user = None

        self.factors = None