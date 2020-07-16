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
from okta.models.password_credential\
    import PasswordCredential
from okta.models.authentication_provider\
    import AuthenticationProvider
from okta.models.recovery_question_credential\
    import RecoveryQuestionCredential


class UserCredentials(
    OktaObject
):
    """
    A class for UserCredentials objects.
    """

    def __init__(self, config=None):
        if config:
            if "password" in config:
                if isinstance(config["password"],
                              PasswordCredential):
                    self.password = config["password"]
                else:
                    self.password = PasswordCredential(
                        config["password"]
                    )
            else:
                self.password = None
            if "provider" in config:
                if isinstance(config["provider"],
                              AuthenticationProvider):
                    self.provider = config["provider"]
                else:
                    self.provider = AuthenticationProvider(
                        config["provider"]
                    )
            else:
                self.provider = None
            if "recovery_question" in config:
                if isinstance(config["recovery_question"],
                              RecoveryQuestionCredential):
                    self.recovery_question = config["recovery_question"]
                else:
                    self.recovery_question = RecoveryQuestionCredential(
                        config["recovery_question"]
                    )
            else:
                self.recovery_question = None
        else:
            self.password = None
            self.provider = None
            self.recovery_question = None
