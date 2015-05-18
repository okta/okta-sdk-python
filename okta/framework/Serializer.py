from json import dumps, JSONEncoder
from datetime import datetime
from okta.framework.Utils import Utils


class Serializer(JSONEncoder):
    def default(self, obj):

        if isinstance(obj, datetime):
            return obj.strftime('dt(%Y-%m-%dT%H:%M:%SZ)')
        elif isinstance(obj, object):
            return Utils.remove_nulls(obj.__dict__)
        else:
            return JSONEncoder.default(self, obj)