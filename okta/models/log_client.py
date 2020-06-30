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


class LogClient(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.device = config["device"]\
                if "device" in config else None
            self.geographical_context = config["geographicalContext"]\
                if "geographicalContext" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.ip_address = config["ipAddress"]\
                if "ipAddress" in config else None
            self.user_agent = config["userAgent"]\
                if "userAgent" in config else None
            self.zone = config["zone"]\
                if "zone" in config else None
        else:
            self.device = None
            self.geographical_context = None
            self.id = None
            self.ip_address = None
            self.user_agent = None
            self.zone = None

# End of File Generation
