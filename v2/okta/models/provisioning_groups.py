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


class ProvisioningGroups(
    OktaObject
):
    """
    A class for ProvisioningGroups objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.action = config["action"]\
                if "action" in config else None
            self.assignments = OktaCollection.form_list(
                config["assignments"] if "assignments"\
                    in config else [],
                str
            )
            self.filter = OktaCollection.form_list(
                config["filter"] if "filter"\
                    in config else [],
                str
            )
            self.source_attribute_name = config["sourceAttributeName"]\
                if "sourceAttributeName" in config else None
        else:
            self.action = None
            self.assignments = []
            self.filter = []
            self.source_attribute_name = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "action": self.action,
            "assignments": self.assignments,
            "filter": self.filter,
            "sourceAttributeName": self.source_attribute_name
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
