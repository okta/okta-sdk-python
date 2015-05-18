class FactorProfile:

    types = {
        'question': str,
        'questionText': str,
        'answer': str,
        'phoneNumber': str,
        'credentialId': str
    }

    def __init__(self):

        # unique key for question
        self.question = None  # str

        # display text for question
        self.questionText = None  # str

        # answer to question
        self.answer = None  # str

        # phone number of mobile device
        self.phoneNumber = None  # str

        # unique id for instance
        self.credentialId = None  # str
