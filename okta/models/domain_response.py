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
from okta.models import domain_links\
    as domain_links
from okta.models import dns_record\
    as dns_record
from okta.models import domain_certificate_metadata\
    as domain_certificate_metadata


class DomainResponse(
    OktaObject
):
    """
    A class for DomainResponse objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "links" in config:
                if isinstance(config["links"],
                              domain_links.DomainLinks):
                    self.links = config["links"]
                elif config["links"] is not None:
                    self.links = domain_links.DomainLinks(
                        config["links"]
                    )
                else:
                    self.links = None
            else:
                self.links = None
            self.dns_records = OktaCollection.form_list(
                config["dnsRecords"] if "dnsRecords"\
                    in config else [],
                dns_record.DnsRecord
            )
            self.domain = config["domain"]\
                if "domain" in config else None
            self.id = config["id"]\
                if "id" in config else None
            if "publicCertificate" in config:
                if isinstance(config["publicCertificate"],
                              domain_certificate_metadata.DomainCertificateMetadata):
                    self.public_certificate = config["publicCertificate"]
                elif config["publicCertificate"] is not None:
                    self.public_certificate = domain_certificate_metadata.DomainCertificateMetadata(
                        config["publicCertificate"]
                    )
                else:
                    self.public_certificate = None
            else:
                self.public_certificate = None
            self.validation_status = config["validationStatus"]\
                if "validationStatus" in config else None
        else:
            self.links = None
            self.dns_records = []
            self.domain = None
            self.id = None
            self.public_certificate = None
            self.validation_status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "dnsRecords": self.dns_records,
            "domain": self.domain,
            "id": self.id,
            "publicCertificate": self.public_certificate,
            "validationStatus": self.validation_status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
