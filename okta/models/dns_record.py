# flake8: noqa
"""
Copyright 2021 - Present Okta, Inc.

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
from okta.models import dns_record_type\
    as dns_record_type


class DnsRecord(
    OktaObject
):
    """
    A class for DnsRecord objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.expiration = config["expiration"]\
                if "expiration" in config else None
            self.fqdn = config["fqdn"]\
                if "fqdn" in config else None
            if "recordType" in config:
                if isinstance(config["recordType"],
                              dns_record_type.DnsRecordType):
                    self.record_type = config["recordType"]
                elif config["recordType"] is not None:
                    self.record_type = dns_record_type.DnsRecordType(
                        config["recordType"].upper()
                    )
                else:
                    self.record_type = None
            else:
                self.record_type = None
            self.values = OktaCollection.form_list(
                config["values"] if "values"\
                    in config else [],
                str
            )
        else:
            self.expiration = None
            self.fqdn = None
            self.record_type = None
            self.values = []

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "expiration": self.expiration,
            "fqdn": self.fqdn,
            "recordType": self.record_type,
            "values": self.values
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
