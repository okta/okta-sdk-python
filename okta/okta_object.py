from enum import Enum


class OktaObject:
    """
    Base object for all Okta datatypes
    """

    def __init__(self, config=None):
        pass

    def __repr__(self):
        return str(vars(self))

    def as_dict(self):
        """
        Returns dictionary object of
        {{pascalCase model.modelName}} object.
        """
        result = {}
        for key, val in self.request_format().items():
            if val is None:
                continue
            if not isinstance(val, OktaObject):
                result[key] = val
            elif issubclass(type(val), Enum):
                result[key] = val.value
            else:
                result[key] = val.as_dict()
        return result

    def request_format(self):
        return {}
