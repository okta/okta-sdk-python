from __future__ import unicode_literals


class RecoveryQuestion:

    types = {
        'question': str,
        'answer': str
    }

    def __init__(self):

        self.question = None  # str

        self.answer = None  # str
