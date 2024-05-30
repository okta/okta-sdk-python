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


class LogSecurityContext(
    OktaObject
):
    """
    A class for LogSecurityContext objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.as_number = config["asNumber"]\
                if "asNumber" in config else None
            self.as_org = config["asOrg"]\
                if "asOrg" in config else None
            self.domain = config["domain"]\
                if "domain" in config else None
            self.is_proxy = config["isProxy"]\
                if "isProxy" in config else None
            self.isp = config["isp"]\
                if "isp" in config else None
        else:
            self.as_number = None
            self.as_org = None
            self.domain = None
            self.is_proxy = None
            self.isp = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "asNumber": self.as_number,
            "asOrg": self.as_org,
            "domain": self.domain,
            "isProxy": self.is_proxy,
            "isp": self.isp
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
