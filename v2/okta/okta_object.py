from aenum import MultiValueEnum


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
            if isinstance(val, list):
                formatted_list = []
                for item in val:
                    if isinstance(item, OktaObject):
                        formatted_list.append(item.as_dict())
                    else:
                        formatted_list.append(item)
                result[key] = formatted_list
            elif not isinstance(val, OktaObject):
                result[key] = val
            elif issubclass(type(val), MultiValueEnum):
                result[key] = val.value
            else:
                result[key] = val.as_dict()
        return result

    def request_format(self):
        return {}
