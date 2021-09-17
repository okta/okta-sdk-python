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
from okta.models import domain_certificate_source_type\
    as domain_certificate_source_type
from okta.models import dns_record\
    as dns_record
from okta.models import domain_certificate_metadata\
    as domain_certificate_metadata
from okta.models import domain_validation_status\
    as domain_validation_status


class Domain(
    OktaObject
):
    """
    A class for Domain objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "certificateSourceType" in config:
                if isinstance(config["certificateSourceType"],
                              domain_certificate_source_type.DomainCertificateSourceType):
                    self.certificate_source_type = config["certificateSourceType"]
                elif config["certificateSourceType"] is not None:
                    self.certificate_source_type = domain_certificate_source_type.DomainCertificateSourceType(
                        config["certificateSourceType"].upper()
                    )
                else:
                    self.certificate_source_type = None
            else:
                self.certificate_source_type = None
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
            if "validationStatus" in config:
                if isinstance(config["validationStatus"],
                              domain_validation_status.DomainValidationStatus):
                    self.validation_status = config["validationStatus"]
                elif config["validationStatus"] is not None:
                    self.validation_status = domain_validation_status.DomainValidationStatus(
                        config["validationStatus"].upper()
                    )
                else:
                    self.validation_status = None
            else:
                self.validation_status = None
        else:
            self.certificate_source_type = None
            self.dns_records = []
            self.domain = None
            self.id = None
            self.public_certificate = None
            self.validation_status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "certificateSourceType": self.certificate_source_type,
            "dnsRecords": self.dns_records,
            "domain": self.domain,
            "id": self.id,
            "publicCertificate": self.public_certificate,
            "validationStatus": self.validation_status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
