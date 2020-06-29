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


class LogAuthenticationContext:
    def __init__(self, config=None):
        if config:
            self.authentication_provider = config["authenticationProvider"]
            self.authentication_step = config["authenticationStep"]
            self.credential_provider = config["credentialProvider"]
            self.credential_type = config["credentialType"]
            self.external_session_id = config["externalSessionId"]
            self.interface = config["interface"]
            self.issuer = config["issuer"]
        else:
            self.authentication_provider = None
            self.authentication_step = None
            self.credential_provider = None
            self.credential_type = None
            self.external_session_id = None
            self.interface = None
            self.issuer = None

# End of File Generation
