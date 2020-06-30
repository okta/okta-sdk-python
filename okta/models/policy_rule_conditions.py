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
            self.app = config["app"]\
                if "app" in config else None
            self.apps = config["apps"]\
                if "apps" in config else None
            self.auth_context = config["authContext"]\
                if "authContext" in config else None
            self.auth_provider = config["authProvider"]\
                if "authProvider" in config else None
            self.before_scheduled_action = config["beforeScheduledAction"]\
                if "beforeScheduledAction" in config else None
            self.clients = config["clients"]\
                if "clients" in config else None
            self.context = config["context"]\
                if "context" in config else None
            self.device = config["device"]\
                if "device" in config else None
            self.grant_types = config["grantTypes"]\
                if "grantTypes" in config else None
            self.groups = config["groups"]\
                if "groups" in config else None
            self.identity_provider = config["identityProvider"]\
                if "identityProvider" in config else None
            self.mdm_enrollment = config["mdmEnrollment"]\
                if "mdmEnrollment" in config else None
            self.network = config["network"]\
                if "network" in config else None
            self.people = config["people"]\
                if "people" in config else None
            self.platform = config["platform"]\
                if "platform" in config else None
            self.risk = config["risk"]\
                if "risk" in config else None
            self.risk_score = config["riskScore"]\
                if "riskScore" in config else None
            self.scopes = config["scopes"]\
                if "scopes" in config else None
            self.user_identifier = config["userIdentifier"]\
                if "userIdentifier" in config else None
            self.user_status = config["userStatus"]\
                if "userStatus" in config else None
            self.users = config["users"]\
                if "users" in config else None
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
