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


class LogIpAddress(
    OktaObject
):
    """
    A class for LogIpAddress objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
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
            self.ip = config["ip"]\
                if "ip" in config else None
            self.source = config["source"]\
                if "source" in config else None
            self.version = config["version"]\
                if "version" in config else None
        else:
            self.geographical_context = None
            self.ip = None
            self.source = None
            self.version = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "geographicalContext": self.geographical_context,
            "ip": self.ip,
            "source": self.source,
            "version": self.version
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
