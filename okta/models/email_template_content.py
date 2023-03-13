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


class EmailTemplateContent(
    OktaObject
):
    """
    A class for EmailTemplateContent objects.
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
            self.from_address = config["fromAddress"]\
                if "fromAddress" in config else None
            self.from_name = config["fromName"]\
                if "fromName" in config else None
            self.subject = config["subject"]\
                if "subject" in config else None
        else:
            self.links = None
            self.body = None
            self.from_address = None
            self.from_name = None
            self.subject = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "body": self.body,
            "fromAddress": self.from_address,
            "fromName": self.from_name,
            "subject": self.subject
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
