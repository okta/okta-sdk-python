from __future__ import unicode_literals


class Question:

    types = {
        'question': str,
        'questionText': str
    }

    def __init__(self):

        self.question = None  # str

        self.questionText = None  # str
