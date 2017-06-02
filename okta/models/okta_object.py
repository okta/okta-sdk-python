class OktaObject:
    def __init__(self, client=None, dictionary={}):
        self._client = client

        if isinstance(dictionary, dict):
            self.__map = dictionary
        else:
            self.__map = dictionary.__map

    def get(self, key):
        return self.__map[key]

    def set(self, key, value):
        self.__map[key] = value
