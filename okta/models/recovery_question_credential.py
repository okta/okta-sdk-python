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

    def remove(self, key):
        del self._map[key]

    @property
    def answer(self):
        return self._map.get('answer')

    @answer.setter
    def answer(self, val):
        self._map['answer'] = val

    @answer.deleter
    def answer(self):
        del self._map['answer']

    @property
    def question(self):
        return self._map.get('question')

    @question.setter
    def question(self, val):
        self._map['question'] = val

    @question.deleter
    def question(self):
        del self._map['question']

    def json(self):
        return Utils.to_json(self)
