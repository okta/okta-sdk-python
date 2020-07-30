# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject


class SecurityQuestion(
    OktaObject
):
    """
    A class for SecurityQuestion objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.answer = config["answer"]\
                if "answer" in config else None
            self.question = config["question"]\
                if "question" in config else None
            self.question_text = config["questionText"]\
                if "questionText" in config else None
        else:
            self.answer = None
            self.question = None
            self.question_text = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "answer": self.answer,
            "question": self.question,
            "questionText": self.question_text
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
