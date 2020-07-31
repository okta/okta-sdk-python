from enum import Enum


class OktaObject:
    PRIMITIVE_PY_TYPES = (int, str, bool, dict, set, tuple, list)
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
            elif self._is_primitive(val):
                result[key] = val
            elif issubclass(type(val), Enum):
                result[key] = val.value
            else:
                result[key] = val.as_dict()
        return result

    def _is_primitive(self, var):
        """
        Returns status if variable given is a primitive datatype:
        int, str, bool, float, dict, set

        Args:
            var (any): variable given
        """
        return isinstance(var, OktaObject.PRIMITIVE_PY_TYPES)

    def request_format(self):
        return {}
