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
from okta.models import allowed_for_enum\
    as allowed_for_enum
from okta.models import channel_binding\
    as channel_binding
from okta.models import compliance\
    as compliance
from okta.models import user_verification_enum\
    as user_verification_enum


class AuthenticatorSettings(
    OktaObject
):
    """
    A class for AuthenticatorSettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "allowedFor" in config:
                if isinstance(config["allowedFor"],
                              allowed_for_enum.AllowedForEnum):
                    self.allowed_for = config["allowedFor"]
                elif config["allowedFor"] is not None:
                    self.allowed_for = allowed_for_enum.AllowedForEnum(
                        config["allowedFor"].upper()
                    )
                else:
                    self.allowed_for = None
            else:
                self.allowed_for = None
            self.app_instance_id = config["appInstanceId"]\
                if "appInstanceId" in config else None
            if "channelBinding" in config:
                if isinstance(config["channelBinding"],
                              channel_binding.ChannelBinding):
                    self.channel_binding = config["channelBinding"]
                elif config["channelBinding"] is not None:
                    self.channel_binding = channel_binding.ChannelBinding(
                        config["channelBinding"]
                    )
                else:
                    self.channel_binding = None
            else:
                self.channel_binding = None
            if "compliance" in config:
                if isinstance(config["compliance"],
                              compliance.Compliance):
                    self.compliance = config["compliance"]
                elif config["compliance"] is not None:
                    self.compliance = compliance.Compliance(
                        config["compliance"]
                    )
                else:
                    self.compliance = None
            else:
                self.compliance = None
            self.token_lifetime_in_minutes = config["tokenLifetimeInMinutes"]\
                if "tokenLifetimeInMinutes" in config else None
            if "userVerification" in config:
                if isinstance(config["userVerification"],
                              user_verification_enum.UserVerificationEnum):
                    self.user_verification = config["userVerification"]
                elif config["userVerification"] is not None:
                    self.user_verification = user_verification_enum.UserVerificationEnum(
                        config["userVerification"].upper()
                    )
                else:
                    self.user_verification = None
            else:
                self.user_verification = None
        else:
            self.allowed_for = None
            self.app_instance_id = None
            self.channel_binding = None
            self.compliance = None
            self.token_lifetime_in_minutes = None
            self.user_verification = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "allowedFor": self.allowed_for,
            "appInstanceId": self.app_instance_id,
            "channelBinding": self.channel_binding,
            "compliance": self.compliance,
            "tokenLifetimeInMinutes": self.token_lifetime_in_minutes,
            "userVerification": self.user_verification
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
