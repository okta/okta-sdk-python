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


class OAuth2Scope(
    OktaObject
):
    """
    A class for OAuth2Scope objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.consent = config["consent"]\
                if "consent" in config else None
            self.default = config["default"]\
                if "default" in config else None
            self.description = config["description"]\
                if "description" in config else None
            self.display_name = config["displayName"]\
                if "displayName" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.metadata_publish = config["metadataPublish"]\
                if "metadataPublish" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.system = config["system"]\
                if "system" in config else None
        else:
            self.consent = None
            self.default = None
            self.description = None
            self.display_name = None
            self.id = None
            self.metadata_publish = None
            self.name = None
            self.system = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "consent": self.consent,
            "default": self.default,
            "description": self.description,
            "displayName": self.display_name,
            "id": self.id,
            "metadataPublish": self.metadata_publish,
            "name": self.name,
            "system": self.system
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
