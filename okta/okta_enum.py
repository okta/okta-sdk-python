from enum import Enum


class OktaEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value.lower() == value.lower():
                return member
        raise ValueError("%r is not a valid %s" % (value, cls.__name__))
