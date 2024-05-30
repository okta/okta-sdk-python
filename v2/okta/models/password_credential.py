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
from okta.models import password_credential_hash\
    as password_credential_hash
from okta.models import password_credential_hook\
    as password_credential_hook


class PasswordCredential(
    OktaObject
):
    """
    A class for PasswordCredential objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "hash" in config:
                if isinstance(config["hash"],
                              password_credential_hash.PasswordCredentialHash):
                    self.hash = config["hash"]
                elif config["hash"] is not None:
                    self.hash = password_credential_hash.PasswordCredentialHash(
                        config["hash"]
                    )
                else:
                    self.hash = None
            else:
                self.hash = None
            if "hook" in config:
                if isinstance(config["hook"],
                              password_credential_hook.PasswordCredentialHook):
                    self.hook = config["hook"]
                elif config["hook"] is not None:
                    self.hook = password_credential_hook.PasswordCredentialHook(
                        config["hook"]
                    )
                else:
                    self.hook = None
            else:
                self.hook = None
            self.value = config["value"]\
                if "value" in config else None
        else:
            self.hash = None
            self.hook = None
            self.value = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "hash": self.hash,
            "hook": self.hook,
            "value": self.value
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
