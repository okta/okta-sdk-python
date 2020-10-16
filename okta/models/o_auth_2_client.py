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


class OAuth2Client(
    OktaObject
):
    """
    A class for OAuth2Client objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.client_id = config["clientId"]\
                if "clientId" in config else None
            self.client_name = config["clientName"]\
                if "clientName" in config else None
            self.client_uri = config["clientUri"]\
                if "clientUri" in config else None
            self.logo_uri = config["logoUri"]\
                if "logoUri" in config else None
        else:
            self.links = None
            self.client_id = None
            self.client_name = None
            self.client_uri = None
            self.logo_uri = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "client_id": self.client_id,
            "client_name": self.client_name,
            "client_uri": self.client_uri,
            "logo_uri": self.logo_uri
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
