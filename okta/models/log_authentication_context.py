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


class LogAuthenticationContext(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.authentication_provider = config["authenticationProvider"]\
                if "authenticationProvider" in config else None
            self.authentication_step = config["authenticationStep"]\
                if "authenticationStep" in config else None
            self.credential_provider = config["credentialProvider"]\
                if "credentialProvider" in config else None
            self.credential_type = config["credentialType"]\
                if "credentialType" in config else None
            self.external_session_id = config["externalSessionId"]\
                if "externalSessionId" in config else None
            self.interface = config["interface"]\
                if "interface" in config else None
            self.issuer = config["issuer"]\
                if "issuer" in config else None
        else:
            self.authentication_provider = None
            self.authentication_step = None
            self.credential_provider = None
            self.credential_type = None
            self.external_session_id = None
            self.interface = None
            self.issuer = None
