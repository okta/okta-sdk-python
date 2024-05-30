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
from okta.models import access_policy_constraints\
    as access_policy_constraints


class VerificationMethod(
    OktaObject
):
    """
    A class for VerificationMethod objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.constraints = OktaCollection.form_list(
                config["constraints"] if "constraints"\
                    in config else [],
                access_policy_constraints.AccessPolicyConstraints
            )
            self.factor_mode = config["factorMode"]\
                if "factorMode" in config else None
            self.inactivity_period = config["inactivityPeriod"]\
                if "inactivityPeriod" in config else None
            self.reauthenticate_in = config["reauthenticateIn"]\
                if "reauthenticateIn" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.constraints = []
            self.factor_mode = None
            self.inactivity_period = None
            self.reauthenticate_in = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "constraints": self.constraints,
            "factorMode": self.factor_mode,
            "inactivityPeriod": self.inactivity_period,
            "reauthenticateIn": self.reauthenticate_in,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
