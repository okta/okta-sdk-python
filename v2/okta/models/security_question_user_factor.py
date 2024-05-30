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

from okta.models.user_factor\
    import UserFactor
from okta.models import security_question_user_factor_profile\
    as security_question_user_factor_profile


class SecurityQuestionUserFactor(
    UserFactor
):
    """
    A class for SecurityQuestionUserFactor objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.factor_type = "question"
            if "profile" in config:
                if isinstance(config["profile"],
                              security_question_user_factor_profile.SecurityQuestionUserFactorProfile):
                    self.profile = config["profile"]
                elif config["profile"] is not None:
                    self.profile = security_question_user_factor_profile.SecurityQuestionUserFactorProfile(
                        config["profile"]
                    )
                else:
                    self.profile = None
            else:
                self.profile = None
        else:
            self.profile = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "profile": self.profile
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
