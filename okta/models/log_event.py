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


class LogEvent(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.actor = config["actor"]\
                if "actor" in config else None
            self.authentication_context = config["authenticationContext"]\
                if "authenticationContext" in config else None
            self.client = config["client"]\
                if "client" in config else None
            self.debug_context = config["debugContext"]\
                if "debugContext" in config else None
            self.display_message = config["displayMessage"]\
                if "displayMessage" in config else None
            self.event_type = config["eventType"]\
                if "eventType" in config else None
            self.legacy_event_type = config["legacyEventType"]\
                if "legacyEventType" in config else None
            self.outcome = config["outcome"]\
                if "outcome" in config else None
            self.published = config["published"]\
                if "published" in config else None
            self.request = config["request"]\
                if "request" in config else None
            self.security_context = config["securityContext"]\
                if "securityContext" in config else None
            self.severity = config["severity"]\
                if "severity" in config else None
            self.target = config["target"]\
                if "target" in config else None
            self.transaction = config["transaction"]\
                if "transaction" in config else None
            self.uuid = config["uuid"]\
                if "uuid" in config else None
            self.version = config["version"]\
                if "version" in config else None
        else:
            self.actor = None
            self.authentication_context = None
            self.client = None
            self.debug_context = None
            self.display_message = None
            self.event_type = None
            self.legacy_event_type = None
            self.outcome = None
            self.published = None
            self.request = None
            self.security_context = None
            self.severity = None
            self.target = None
            self.transaction = None
            self.uuid = None
            self.version = None

# End of File Generation
