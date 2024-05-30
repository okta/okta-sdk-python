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
from okta.models import log_geographical_context\
    as log_geographical_context
from okta.models import log_user_agent\
    as log_user_agent


class LogClient(
    OktaObject
):
    """
    A class for LogClient objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.device = config["device"]\
                if "device" in config else None
            if "geographicalContext" in config:
                if isinstance(config["geographicalContext"],
                              log_geographical_context.LogGeographicalContext):
                    self.geographical_context = config["geographicalContext"]
                elif config["geographicalContext"] is not None:
                    self.geographical_context = log_geographical_context.LogGeographicalContext(
                        config["geographicalContext"]
                    )
                else:
                    self.geographical_context = None
            else:
                self.geographical_context = None
            self.id = config["id"]\
                if "id" in config else None
            self.ip_address = config["ipAddress"]\
                if "ipAddress" in config else None
            if "userAgent" in config:
                if isinstance(config["userAgent"],
                              log_user_agent.LogUserAgent):
                    self.user_agent = config["userAgent"]
                elif config["userAgent"] is not None:
                    self.user_agent = log_user_agent.LogUserAgent(
                        config["userAgent"]
                    )
                else:
                    self.user_agent = None
            else:
                self.user_agent = None
            self.zone = config["zone"]\
                if "zone" in config else None
        else:
            self.device = None
            self.geographical_context = None
            self.id = None
            self.ip_address = None
            self.user_agent = None
            self.zone = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "device": self.device,
            "geographicalContext": self.geographical_context,
            "id": self.id,
            "ipAddress": self.ip_address,
            "userAgent": self.user_agent,
            "zone": self.zone
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
