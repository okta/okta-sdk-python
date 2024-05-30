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
from okta.models import authenticator_provider_configuration_user_name_plate\
    as authenticator_provider_configuration_user_name_plate


class AuthenticatorProviderConfiguration(
    OktaObject
):
    """
    A class for AuthenticatorProviderConfiguration objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.auth_port = config["authPort"]\
                if "authPort" in config else None
            self.host = config["host"]\
                if "host" in config else None
            self.host_name = config["hostName"]\
                if "hostName" in config else None
            self.instance_id = config["instanceId"]\
                if "instanceId" in config else None
            self.integration_key = config["integrationKey"]\
                if "integrationKey" in config else None
            self.secret_key = config["secretKey"]\
                if "secretKey" in config else None
            self.shared_secret = config["sharedSecret"]\
                if "sharedSecret" in config else None
            if "userNameTemplate" in config:
                if isinstance(config["userNameTemplate"],
                              authenticator_provider_configuration_user_name_plate.AuthenticatorProviderConfigurationUserNamePlate):
                    self.user_name_template = config["userNameTemplate"]
                elif config["userNameTemplate"] is not None:
                    self.user_name_template = authenticator_provider_configuration_user_name_plate.AuthenticatorProviderConfigurationUserNamePlate(
                        config["userNameTemplate"]
                    )
                else:
                    self.user_name_template = None
            else:
                self.user_name_template = None
        else:
            self.auth_port = None
            self.host = None
            self.host_name = None
            self.instance_id = None
            self.integration_key = None
            self.secret_key = None
            self.shared_secret = None
            self.user_name_template = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "authPort": self.auth_port,
            "host": self.host,
            "hostName": self.host_name,
            "instanceId": self.instance_id,
            "integrationKey": self.integration_key,
            "secretKey": self.secret_key,
            "sharedSecret": self.shared_secret,
            "userNameTemplate": self.user_name_template
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
