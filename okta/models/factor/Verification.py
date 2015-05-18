class Verification:

    types = {
        'activationToken': str,
        'answer': str,
        'passCode': str,
        'nextPassCode': str
    }

    def __init__(self):

        self.activationToken = None  # str

        self.answer = None  # str

        self.passCode = None  # str

        self.nextPassCode = None  # str
