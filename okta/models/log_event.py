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
from okta.okta_collection import OktaCollection
from okta.models import log_actor\
    as log_actor
from okta.models import log_authentication_context\
    as log_authentication_context
from okta.models import log_client\
    as log_client
from okta.models import log_debug_context\
    as log_debug_context
from okta.models import log_outcome\
    as log_outcome
from okta.models import log_request\
    as log_request
from okta.models import log_security_context\
    as log_security_context
from okta.models import log_severity\
    as log_severity
from okta.models import log_target\
    as log_target
from okta.models import log_transaction\
    as log_transaction


class LogEvent(
    OktaObject
):
    """
    A class for LogEvent objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "actor" in config:
                if isinstance(config["actor"],
                              log_actor.LogActor):
                    self.actor = config["actor"]
                elif config["actor"] is not None:
                    self.actor = log_actor.LogActor(
                        config["actor"]
                    )
                else:
                    self.actor = None
            else:
                self.actor = None
            if "authenticationContext" in config:
                if isinstance(config["authenticationContext"],
                              log_authentication_context.LogAuthenticationContext):
                    self.authentication_context = config["authenticationContext"]
                elif config["authenticationContext"] is not None:
                    self.authentication_context = log_authentication_context.LogAuthenticationContext(
                        config["authenticationContext"]
                    )
                else:
                    self.authentication_context = None
            else:
                self.authentication_context = None
            if "client" in config:
                if isinstance(config["client"],
                              log_client.LogClient):
                    self.client = config["client"]
                elif config["client"] is not None:
                    self.client = log_client.LogClient(
                        config["client"]
                    )
                else:
                    self.client = None
            else:
                self.client = None
            if "debugContext" in config:
                if isinstance(config["debugContext"],
                              log_debug_context.LogDebugContext):
                    self.debug_context = config["debugContext"]
                elif config["debugContext"] is not None:
                    self.debug_context = log_debug_context.LogDebugContext(
                        config["debugContext"]
                    )
                else:
                    self.debug_context = None
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
                              log_outcome.LogOutcome):
                    self.outcome = config["outcome"]
                elif config["outcome"] is not None:
                    self.outcome = log_outcome.LogOutcome(
                        config["outcome"]
                    )
                else:
                    self.outcome = None
            else:
                self.outcome = None
            self.published = config["published"]\
                if "published" in config else None
            if "request" in config:
                if isinstance(config["request"],
                              log_request.LogRequest):
                    self.request = config["request"]
                elif config["request"] is not None:
                    self.request = log_request.LogRequest(
                        config["request"]
                    )
                else:
                    self.request = None
            else:
                self.request = None
            if "securityContext" in config:
                if isinstance(config["securityContext"],
                              log_security_context.LogSecurityContext):
                    self.security_context = config["securityContext"]
                elif config["securityContext"] is not None:
                    self.security_context = log_security_context.LogSecurityContext(
                        config["securityContext"]
                    )
                else:
                    self.security_context = None
            else:
                self.security_context = None
            if "severity" in config:
                if isinstance(config["severity"],
                              log_severity.LogSeverity):
                    self.severity = config["severity"]
                elif config["severity"] is not None:
                    self.severity = log_severity.LogSeverity(
                        config["severity"].upper()
                    )
                else:
                    self.severity = None
            else:
                self.severity = None
            self.target = OktaCollection.form_list(
                config["target"] if "target"\
                    in config else [],
                log_target.LogTarget
            )
            if "transaction" in config:
                if isinstance(config["transaction"],
                              log_transaction.LogTransaction):
                    self.transaction = config["transaction"]
                elif config["transaction"] is not None:
                    self.transaction = log_transaction.LogTransaction(
                        config["transaction"]
                    )
                else:
                    self.transaction = None
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
            self.target = []
            self.transaction = None
            self.uuid = None
            self.version = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
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
        parent_req_format.update(current_obj_format)
        return parent_req_format
