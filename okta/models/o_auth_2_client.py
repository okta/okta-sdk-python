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
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]\
                if "_links" in config else None
            self.client_id = config["client_id"]\
                if "client_id" in config else None
            self.client_name = config["client_name"]\
                if "client_name" in config else None
            self.client_uri = config["client_uri"]\
                if "client_uri" in config else None
            self.logo_uri = config["logo_uri"]\
                if "logo_uri" in config else None
        else:
            self.links = None
            self.client_id = None
            self.client_name = None
            self.client_uri = None
            self.logo_uri = None
