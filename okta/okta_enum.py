from enum import Enum


class OktaEnum(Enum):
    """
    Class to enhance the Python Enum class
    """
    @classmethod
    def _missing_(cls, value):
        """
        Class method called when enum isn't found.
        Checks to make sure that case-insensitive enums
        can be found
        """
        for member in cls:
            if member.value.lower() == value.lower():
                return member
        raise ValueError("%r is not a valid %s" % (value, cls.__name__))
