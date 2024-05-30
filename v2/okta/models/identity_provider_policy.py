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

from okta.models.policy\
    import Policy
from okta.models.policy_type import PolicyType
from okta.models import policy_account_link\
    as policy_account_link
from okta.models import provisioning\
    as provisioning
from okta.models import policy_subject\
    as policy_subject


class IdentityProviderPolicy(
    Policy
):
    """
    A class for IdentityProviderPolicy objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.type = PolicyType("IDP_DISCOVERY")
            if "accountLink" in config:
                if isinstance(config["accountLink"],
                              policy_account_link.PolicyAccountLink):
                    self.account_link = config["accountLink"]
                elif config["accountLink"] is not None:
                    self.account_link = policy_account_link.PolicyAccountLink(
                        config["accountLink"]
                    )
                else:
                    self.account_link = None
            else:
                self.account_link = None
            self.max_clock_skew = config["maxClockSkew"]\
                if "maxClockSkew" in config else None
            if "provisioning" in config:
                if isinstance(config["provisioning"],
                              provisioning.Provisioning):
                    self.provisioning = config["provisioning"]
                elif config["provisioning"] is not None:
                    self.provisioning = provisioning.Provisioning(
                        config["provisioning"]
                    )
                else:
                    self.provisioning = None
            else:
                self.provisioning = None
            if "subject" in config:
                if isinstance(config["subject"],
                              policy_subject.PolicySubject):
                    self.subject = config["subject"]
                elif config["subject"] is not None:
                    self.subject = policy_subject.PolicySubject(
                        config["subject"]
                    )
                else:
                    self.subject = None
            else:
                self.subject = None
        else:
            self.account_link = None
            self.max_clock_skew = None
            self.provisioning = None
            self.subject = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "accountLink": self.account_link,
            "maxClockSkew": self.max_clock_skew,
            "provisioning": self.provisioning,
            "subject": self.subject
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
