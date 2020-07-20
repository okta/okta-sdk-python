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
from okta.models.inline_hook_channel_config_auth_scheme\
    import InlineHookChannelConfigAuthScheme


class InlineHookChannelConfig(
    OktaObject
):
    """
    A class for InlineHookChannelConfig objects.
    """

    def __init__(self, config=None):
        if config:
            if "authScheme" in config:
                if isinstance(config["authScheme"],
                              InlineHookChannelConfigAuthScheme):
                    self.auth_scheme = config["authScheme"]
                else:
                    self.auth_scheme = InlineHookChannelConfigAuthScheme(
                        config["authScheme"]
                    )
            else:
                self.auth_scheme = None
            self.headers = config["headers"]\
                if "headers" in config else None
            self.uri = config["uri"]\
                if "uri" in config else None
        else:
            self.auth_scheme = None
            self.headers = None
            self.uri = None

    def request_format(self):
        return {
            "authScheme": self.auth_scheme,
            "headers": self.headers,
            "uri": self.uri
        }
