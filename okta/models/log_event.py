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
from okta.models.log_actor\
    import LogActor
from okta.models.log_authentication_context\
    import LogAuthenticationContext
from okta.models.log_client\
    import LogClient
from okta.models.log_debug_context\
    import LogDebugContext
from okta.models.log_outcome\
    import LogOutcome
from okta.models.log_request\
    import LogRequest
from okta.models.log_security_context\
    import LogSecurityContext
from okta.models.log_severity\
    import LogSeverity
from okta.models.log_transaction\
    import LogTransaction


class LogEvent(
    OktaObject
):
    """
    A class for LogEvent objects.
    """

    def __init__(self, config=None):
        if config:
            if "actor" in config:
                if isinstance(config["actor"],
                              LogActor):
                    self.actor = config["actor"]
                else:
                    self.actor = LogActor(
                        config["actor"]
                    )
            else:
                self.actor = None
            if "authenticationContext" in config:
                if isinstance(config["authenticationContext"],
                              LogAuthenticationContext):
                    self.authentication_context = config["authenticationContext"]
                else:
                    self.authentication_context = LogAuthenticationContext(
                        config["authenticationContext"]
                    )
            else:
                self.authentication_context = None
            if "client" in config:
                if isinstance(config["client"],
                              LogClient):
                    self.client = config["client"]
                else:
                    self.client = LogClient(
                        config["client"]
                    )
            else:
                self.client = None
            if "debugContext" in config:
                if isinstance(config["debugContext"],
                              LogDebugContext):
                    self.debug_context = config["debugContext"]
                else:
                    self.debug_context = LogDebugContext(
                        config["debugContext"]
                    )
            else:
                self.debug_context = None
            self.display_message = config["displayMessage"]\
                if "displayMessage" in config else None
            self.event_type = config["eventType"]\
                if "eventType" in config else None
            self.legacy_event_type = config["legacyEventType"]\
                if "legacyEventType" in config else None
            if "outcome" in config:
                if isinstance(config["outcome"],
                              LogOutcome):
                    self.outcome = config["outcome"]
                else:
                    self.outcome = LogOutcome(
                        config["outcome"]
                    )
            else:
                self.outcome = None
            self.published = config["published"]\
                if "published" in config else None
            if "request" in config:
                if isinstance(config["request"],
                              LogRequest):
                    self.request = config["request"]
                else:
                    self.request = LogRequest(
                        config["request"]
                    )
            else:
                self.request = None
            if "securityContext" in config:
                if isinstance(config["securityContext"],
                              LogSecurityContext):
                    self.security_context = config["securityContext"]
                else:
                    self.security_context = LogSecurityContext(
                        config["securityContext"]
                    )
            else:
                self.security_context = None
            if "severity" in config:
                if isinstance(config["severity"],
                              LogSeverity):
                    self.severity = config["severity"]
                else:
                    self.severity = LogSeverity(
                        config["severity"]
                    )
            else:
                self.severity = None
            self.target = config["target"]\
                if "target" in config else None
            if "transaction" in config:
                if isinstance(config["transaction"],
                              LogTransaction):
                    self.transaction = config["transaction"]
                else:
                    self.transaction = LogTransaction(
                        config["transaction"]
                    )
            else:
                self.transaction = None
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

    def request_format(self):
        return {
            "actor": self.actor,
            "authenticationContext": self.authentication_context,
            "client": self.client,
            "debugContext": self.debug_context,
            "displayMessage": self.display_message,
            "eventType": self.event_type,
            "legacyEventType": self.legacy_event_type,
            "outcome": self.outcome,
            "published": self.published,
            "request": self.request,
            "securityContext": self.security_context,
            "severity": self.severity,
            "target": self.target,
            "transaction": self.transaction,
            "uuid": self.uuid,
            "version": self.version
        }
