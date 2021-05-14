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
from okta.models import password_credential_hash_algorithm\
    as password_credential_hash_algorithm


class PasswordCredentialHash(
    OktaObject
):
    """
    A class for PasswordCredentialHash objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "algorithm" in config:
                if isinstance(config["algorithm"],
                              password_credential_hash_algorithm.PasswordCredentialHashAlgorithm):
                    self.algorithm = config["algorithm"]
                elif config["algorithm"] is not None:
                    self.algorithm = password_credential_hash_algorithm.PasswordCredentialHashAlgorithm(
                        config["algorithm"].upper()
                    )
                else:
                    self.algorithm = None
            else:
                self.algorithm = None
            self.salt = config["salt"]\
                if "salt" in config else None
            self.salt_order = config["saltOrder"]\
                if "saltOrder" in config else None
            self.value = config["value"]\
                if "value" in config else None
            self.work_factor = config["workFactor"]\
                if "workFactor" in config else None
        else:
            self.algorithm = None
            self.salt = None
            self.salt_order = None
            self.value = None
            self.work_factor = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "algorithm": self.algorithm,
            "salt": self.salt,
            "saltOrder": self.salt_order,
            "value": self.value,
            "workFactor": self.work_factor
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
