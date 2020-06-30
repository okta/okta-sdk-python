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


class PushUserFactorProfile:
    def __init__(self, config=None):
        if config:
            self.credential_id = config["credentialId"]\
                if "credentialId" in config else None
            self.device_token = config["deviceToken"]\
                if "deviceToken" in config else None
            self.device_type = config["deviceType"]\
                if "deviceType" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.platform = config["platform"]\
                if "platform" in config else None
            self.version = config["version"]\
                if "version" in config else None
        else:
            self.credential_id = None
            self.device_token = None
            self.device_type = None
            self.name = None
            self.platform = None
            self.version = None

# End of File Generation
