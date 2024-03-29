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


class EmailTemplateCustomization(
    OktaObject
):
    """
    A class for EmailTemplateCustomization objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "_links" in config:
                self.links = config["_links"]
            self.body = config["body"]\
                if "body" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.is_default = config["isDefault"]\
                if "isDefault" in config else None
            self.language = config["language"]\
                if "language" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.subject = config["subject"]\
                if "subject" in config else None
        else:
            self.links = None
            self.body = None
            self.created = None
            self.id = None
            self.is_default = None
            self.language = None
            self.last_updated = None
            self.subject = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "body": self.body,
            "created": self.created,
            "id": self.id,
            "isDefault": self.is_default,
            "language": self.language,
            "lastUpdated": self.last_updated,
            "subject": self.subject
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
