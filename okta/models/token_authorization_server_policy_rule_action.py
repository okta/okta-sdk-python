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
from okta.models import token_authorization_server_policy_rule_action_inline_hook\
    as token_authorization_server_policy_rule_action_inline_hook


class TokenAuthorizationServerPolicyRuleAction(
    OktaObject
):
    """
    A class for TokenAuthorizationServerPolicyRuleAction objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.access_token_lifetime_minutes = config["accessTokenLifetimeMinutes"]\
                if "accessTokenLifetimeMinutes" in config else None
            if "inlineHook" in config:
                if isinstance(config["inlineHook"],
                              token_authorization_server_policy_rule_action_inline_hook.TokenAuthorizationServerPolicyRuleActionInlineHook):
                    self.inline_hook = config["inlineHook"]
                elif config["inlineHook"] is not None:
                    self.inline_hook = token_authorization_server_policy_rule_action_inline_hook.TokenAuthorizationServerPolicyRuleActionInlineHook(
                        config["inlineHook"]
                    )
                else:
                    self.inline_hook = None
            else:
                self.inline_hook = None
            self.refresh_token_lifetime_minutes = config["refreshTokenLifetimeMinutes"]\
                if "refreshTokenLifetimeMinutes" in config else None
            self.refresh_token_window_minutes = config["refreshTokenWindowMinutes"]\
                if "refreshTokenWindowMinutes" in config else None
        else:
            self.access_token_lifetime_minutes = None
            self.inline_hook = None
            self.refresh_token_lifetime_minutes = None
            self.refresh_token_window_minutes = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "accessTokenLifetimeMinutes": self.access_token_lifetime_minutes,
            "inlineHook": self.inline_hook,
            "refreshTokenLifetimeMinutes": self.refresh_token_lifetime_minutes,
            "refreshTokenWindowMinutes": self.refresh_token_window_minutes
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
