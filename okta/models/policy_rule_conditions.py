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


class PolicyRuleConditions:
    def __init__(self, config=None):
        if config:
            self.app = config["app"]
            self.apps = config["apps"]
            self.auth_context = config["authContext"]
            self.auth_provider = config["authProvider"]
            self.before_scheduled_action = config["beforeScheduledAction"]
            self.clients = config["clients"]
            self.context = config["context"]
            self.device = config["device"]
            self.grant_types = config["grantTypes"]
            self.groups = config["groups"]
            self.identity_provider = config["identityProvider"]
            self.mdm_enrollment = config["mdmEnrollment"]
            self.network = config["network"]
            self.people = config["people"]
            self.platform = config["platform"]
            self.risk = config["risk"]
            self.risk_score = config["riskScore"]
            self.scopes = config["scopes"]
            self.user_identifier = config["userIdentifier"]
            self.user_status = config["userStatus"]
            self.users = config["users"]
        else:
            self.app = None
            self.apps = None
            self.auth_context = None
            self.auth_provider = None
            self.before_scheduled_action = None
            self.clients = None
            self.context = None
            self.device = None
            self.grant_types = None
            self.groups = None
            self.identity_provider = None
            self.mdm_enrollment = None
            self.network = None
            self.people = None
            self.platform = None
            self.risk = None
            self.risk_score = None
            self.scopes = None
            self.user_identifier = None
            self.user_status = None
            self.users = None

# End of File Generation
