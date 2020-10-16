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


class LogTarget(
    OktaObject
):
    """
    A class for LogTarget objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.alternate_id = config["alternateId"]\
                if "alternateId" in config else None
            self.detail_entry = config["detailEntry"]\
                if "detailEntry" in config else None
            self.display_name = config["displayName"]\
                if "displayName" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.alternate_id = None
            self.detail_entry = None
            self.display_name = None
            self.id = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "alternateId": self.alternate_id,
            "detailEntry": self.detail_entry,
            "displayName": self.display_name,
            "id": self.id,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
