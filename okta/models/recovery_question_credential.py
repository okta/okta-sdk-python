"""
  THIS FILE IS AUTO GENERATED - SEE CONTRIBUTOR DOCUMENTATION
"""


class RecoveryQuestionCredential(object):

    def __init__(self, dictionary={}, client=None):
        self._client = client

        if isinstance(dictionary, dict):
            self._map = dictionary
        else:
            self._map = dictionary._map

    def get(self, key):
        return self._map[key]

    def set(self, key, value):
        self._map[key] = value

    @property
    def question(self):
        return self._map.get('question')

    @question.setter
    def question(self, val):
        self._map['question'] = val

    @question.deleter
    def question(self):
        del self._map['question']

