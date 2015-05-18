class FactorRequest:

    types = {
        'answer': str,
        'passCode': str,
        'nextPassCode': str
    }

    def __init__(self):

        self.answer = None  # str

        self.passCode = None  # str

        self.nextPassCode = None  # str
