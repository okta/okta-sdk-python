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


class AppLink(
    OktaObject
):
    """
    A class for AppLink objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.app_assignment_id = config["appAssignmentId"]\
                if "appAssignmentId" in config else None
            self.app_instance_id = config["appInstanceId"]\
                if "appInstanceId" in config else None
            self.app_name = config["appName"]\
                if "appName" in config else None
            self.credentials_setup = config["credentialsSetup"]\
                if "credentialsSetup" in config else None
            self.hidden = config["hidden"]\
                if "hidden" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.label = config["label"]\
                if "label" in config else None
            self.link_url = config["linkUrl"]\
                if "linkUrl" in config else None
            self.logo_url = config["logoUrl"]\
                if "logoUrl" in config else None
            self.sort_order = config["sortOrder"]\
                if "sortOrder" in config else None
        else:
            self.app_assignment_id = None
            self.app_instance_id = None
            self.app_name = None
            self.credentials_setup = None
            self.hidden = None
            self.id = None
            self.label = None
            self.link_url = None
            self.logo_url = None
            self.sort_order = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "appAssignmentId": self.app_assignment_id,
            "appInstanceId": self.app_instance_id,
            "appName": self.app_name,
            "credentialsSetup": self.credentials_setup,
            "hidden": self.hidden,
            "id": self.id,
            "label": self.label,
            "linkUrl": self.link_url,
            "logoUrl": self.logo_url,
            "sortOrder": self.sort_order
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
