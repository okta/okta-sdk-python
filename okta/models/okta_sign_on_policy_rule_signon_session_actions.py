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


from urllib.parse import urlencode


class OktaSignOnPolicyRuleSignonSessionActions:
    def __init__(self, config=None):
        if config:
            self.max_session_idle_minutes = config["maxSessionIdleMinutes"]
            self.max_session_lifetime_minutes = config["maxSessionLifetimeMinutes"]
            self.use_persistent_cookie = config["usePersistentCookie"]
        else:
            self.max_session_idle_minutes = "120"
            self.max_session_lifetime_minutes = "0"
            self.use_persistent_cookie = "false"


# End of File Generation
