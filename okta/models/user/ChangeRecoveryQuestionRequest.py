from okta.models.user import Password, RecoveryQuestion


class ChangeRecoveryQuestionRequest:

    types = {
        'password': Password,
        'recovery_question': RecoveryQuestion
    }

    def __init__(self):

        self.password = None  # Password

        self.recovery_question = None  # RecoveryQuestion
