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
import okta.models.log_authentication_provider\
    as log_authentication_provider
import okta.models.log_credential_provider\
    as log_credential_provider
import okta.models.log_credential_type\
    as log_credential_type
import okta.models.log_issuer\
    as log_issuer


class LogAuthenticationContext(
    OktaObject
):
    """
    A class for LogAuthenticationContext objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "authenticationProvider" in config:
                if isinstance(config["authenticationProvider"],
                              log_authentication_provider.LogAuthenticationProvider):
                    self.authentication_provider = config["authenticationProvider"]
                else:
                    self.authentication_provider = log_authentication_provider.LogAuthenticationProvider(
                        config["authenticationProvider"].upper()
                    )
            else:
                self.authentication_provider = None
            self.authentication_step = config["authenticationStep"]\
                if "authenticationStep" in config else None
            if "credentialProvider" in config:
                if isinstance(config["credentialProvider"],
                              log_credential_provider.LogCredentialProvider):
                    self.credential_provider = config["credentialProvider"]
                else:
                    self.credential_provider = log_credential_provider.LogCredentialProvider(
                        config["credentialProvider"].upper()
                    )
            else:
                self.credential_provider = None
            if "credentialType" in config:
                if isinstance(config["credentialType"],
                              log_credential_type.LogCredentialType):
                    self.credential_type = config["credentialType"]
                else:
                    self.credential_type = log_credential_type.LogCredentialType(
                        config["credentialType"].upper()
                    )
            else:
                self.credential_type = None
            self.external_session_id = config["externalSessionId"]\
                if "externalSessionId" in config else None
            self.interface = config["interface"]\
                if "interface" in config else None
            if "issuer" in config:
                if isinstance(config["issuer"],
                              log_issuer.LogIssuer):
                    self.issuer = config["issuer"]
                else:
                    self.issuer = log_issuer.LogIssuer(
                        config["issuer"]
                    )
            else:
                self.issuer = None
        else:
            self.authentication_provider = None
            self.authentication_step = None
            self.credential_provider = None
            self.credential_type = None
            self.external_session_id = None
            self.interface = None
            self.issuer = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "authenticationProvider": self.authentication_provider,
            "authenticationStep": self.authentication_step,
            "credentialProvider": self.credential_provider,
            "credentialType": self.credential_type,
            "externalSessionId": self.external_session_id,
            "interface": self.interface,
            "issuer": self.issuer
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
