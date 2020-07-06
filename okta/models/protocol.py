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


class Protocol(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.algorithms = config["algorithms"]\
                if "algorithms" in config else None
            self.credentials = config["credentials"]\
                if "credentials" in config else None
            self.endpoints = config["endpoints"]\
                if "endpoints" in config else None
            self.issuer = config["issuer"]\
                if "issuer" in config else None
            self.relay_state = config["relayState"]\
                if "relayState" in config else None
            self.scopes = config["scopes"]\
                if "scopes" in config else None
            self.settings = config["settings"]\
                if "settings" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.algorithms = None
            self.credentials = None
            self.endpoints = None
            self.issuer = None
            self.relay_state = None
            self.scopes = None
            self.settings = None
            self.type = None
