class OktaObject:
    """
    Base object for all Okta datatypes
    """
    def __init__():
        pass

    def as_dict(self):
        """
        Returns dictionary object of
        {{pascalCase model.modelName}} object.
        """
        return vars(self)
