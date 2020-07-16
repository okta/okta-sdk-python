class OktaObject:
    PRIMITIVE_PY_TYPES = (int, str, bool, dict, set, tuple)
    """
    Base object for all Okta datatypes
    """
    def __init__():
        pass

    def __repr__(self):
        return str(vars(self))

    def as_dict(self):
        """
        Returns dictionary object of
        {{pascalCase model.modelName}} object.
        """
        result = {}
        for key, val in vars(self).items():
            if self._is_primitive(val) or val is None:
                result[key] = val
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
