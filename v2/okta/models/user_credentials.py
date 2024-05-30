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
from okta.models import password_credential\
    as password_credential
from okta.models import authentication_provider\
    as authentication_provider
from okta.models import recovery_question_credential\
    as recovery_question_credential


class UserCredentials(
    OktaObject
):
    """
    A class for UserCredentials objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "password" in config:
                if isinstance(config["password"],
                              password_credential.PasswordCredential):
                    self.password = config["password"]
                elif config["password"] is not None:
                    self.password = password_credential.PasswordCredential(
                        config["password"]
                    )
                else:
                    self.password = None
            else:
                self.password = None
            if "provider" in config:
                if isinstance(config["provider"],
                              authentication_provider.AuthenticationProvider):
                    self.provider = config["provider"]
                elif config["provider"] is not None:
                    self.provider = authentication_provider.AuthenticationProvider(
                        config["provider"]
                    )
                else:
                    self.provider = None
            else:
                self.provider = None
            if "recoveryQuestion" in config:
                if isinstance(config["recoveryQuestion"],
                              recovery_question_credential.RecoveryQuestionCredential):
                    self.recovery_question = config["recoveryQuestion"]
                elif config["recoveryQuestion"] is not None:
                    self.recovery_question = recovery_question_credential.RecoveryQuestionCredential(
                        config["recoveryQuestion"]
                    )
                else:
                    self.recovery_question = None
            else:
                self.recovery_question = None
        else:
            self.password = None
            self.provider = None
            self.recovery_question = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "password": self.password,
            "provider": self.provider,
            "recovery_question": self.recovery_question
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
