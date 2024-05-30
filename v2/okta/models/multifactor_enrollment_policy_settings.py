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
from okta.okta_collection import OktaCollection
from okta.models import multifactor_enrollment_policy_authenticator_settings\
    as multifactor_enrollment_policy_authenticator_settings
from okta.models import multifactor_enrollment_policy_settings_type\
    as multifactor_enrollment_policy_settings_type


class MultifactorEnrollmentPolicySettings(
    OktaObject
):
    """
    A class for MultifactorEnrollmentPolicySettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.authenticators = OktaCollection.form_list(
                config["authenticators"] if "authenticators"\
                    in config else [],
                multifactor_enrollment_policy_authenticator_settings.MultifactorEnrollmentPolicyAuthenticatorSettings
            )
            if "type" in config:
                if isinstance(config["type"],
                              multifactor_enrollment_policy_settings_type.MultifactorEnrollmentPolicySettingsType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = multifactor_enrollment_policy_settings_type.MultifactorEnrollmentPolicySettingsType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
        else:
            self.authenticators = []
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "authenticators": self.authenticators,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
