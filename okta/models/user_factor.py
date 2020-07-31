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
from okta.models.factor_type\
    import FactorType
from okta.models.factor_provider\
    import FactorProvider
from okta.models.factor_status\
    import FactorStatus
from okta.models.verify_factor_request\
    import VerifyFactorRequest


class UserFactor(
    OktaObject
):
    """
    A class for UserFactor objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            self.created = config["created"]\
                if "created" in config else None
            if "factorType" in config:
                if isinstance(config["factorType"],
                              FactorType):
                    self.factor_type = config["factorType"]
                else:
                    self.factor_type = FactorType(
                        config["factorType"].upper()
                    )
            else:
                self.factor_type = None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            if "provider" in config:
                if isinstance(config["provider"],
                              FactorProvider):
                    self.provider = config["provider"]
                else:
                    self.provider = FactorProvider(
                        config["provider"].upper()
                    )
            else:
                self.provider = None
            if "status" in config:
                if isinstance(config["status"],
                              FactorStatus):
                    self.status = config["status"]
                else:
                    self.status = FactorStatus(
                        config["status"].upper()
                    )
            else:
                self.status = None
            if "verify" in config:
                if isinstance(config["verify"],
                              VerifyFactorRequest):
                    self.verify = config["verify"]
                else:
                    self.verify = VerifyFactorRequest(
                        config["verify"]
                    )
            else:
                self.verify = None
        else:
            self.embedded = None
            self.links = None
            self.created = None
            self.factor_type = None
            self.id = None
            self.last_updated = None
            self.provider = None
            self.status = None
            self.verify = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_embedded": self.embedded,
            "_links": self.links,
            "created": self.created,
            "factorType": self.factor_type,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "provider": self.provider,
            "status": self.status,
            "verify": self.verify
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
