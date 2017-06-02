class OktaObject:
    def __init__(self, client=None, dictionary={}):
        self._client = client

        if isinstance(map, dict):
            self.__map = map
        else:
            self.__map = map.__map

    def get(self, key):
        return self.__map[key]

    def set(self, key, value):
        self.__map[key] = value