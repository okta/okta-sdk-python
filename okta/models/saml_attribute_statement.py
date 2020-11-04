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


class SamlAttributeStatement(
    OktaObject
):
    """
    A class for SamlAttributeStatement objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.filter_type = config["filterType"]\
                if "filterType" in config else None
            self.filter_value = config["filterValue"]\
                if "filterValue" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.namespace = config["namespace"]\
                if "namespace" in config else None
            self.type = config["type"]\
                if "type" in config else None
            self.values = OktaCollection.form_list(
                config["values"] if "values"\
                    in config else [],
                str
            )
        else:
            self.filter_type = None
            self.filter_value = None
            self.name = None
            self.namespace = None
            self.type = None
            self.values = []

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "filterType": self.filter_type,
            "filterValue": self.filter_value,
            "name": self.name,
            "namespace": self.namespace,
            "type": self.type,
            "values": self.values
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
