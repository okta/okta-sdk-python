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


class AccessPolicyConstraint(
    OktaObject
):
    """
    A class for AccessPolicyConstraint objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.methods = OktaCollection.form_list(
                config["methods"] if "methods"\
                    in config else [],
                str
            )
            self.reauthenticate_in = config["reauthenticateIn"]\
                if "reauthenticateIn" in config else None
            self.types = OktaCollection.form_list(
                config["types"] if "types"\
                    in config else [],
                str
            )
        else:
            self.methods = []
            self.reauthenticate_in = None
            self.types = []

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "methods": self.methods,
            "reauthenticateIn": self.reauthenticate_in,
            "types": self.types
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
