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
from okta.models import csr_metadata_subject\
    as csr_metadata_subject
from okta.models import csr_metadata_subject_alt_names\
    as csr_metadata_subject_alt_names


class CsrMetadata(
    OktaObject
):
    """
    A class for CsrMetadata objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "subject" in config:
                if isinstance(config["subject"],
                              csr_metadata_subject.CsrMetadataSubject):
                    self.subject = config["subject"]
                elif config["subject"] is not None:
                    self.subject = csr_metadata_subject.CsrMetadataSubject(
                        config["subject"]
                    )
                else:
                    self.subject = None
            else:
                self.subject = None
            if "subjectAltNames" in config:
                if isinstance(config["subjectAltNames"],
                              csr_metadata_subject_alt_names.CsrMetadataSubjectAltNames):
                    self.subject_alt_names = config["subjectAltNames"]
                elif config["subjectAltNames"] is not None:
                    self.subject_alt_names = csr_metadata_subject_alt_names.CsrMetadataSubjectAltNames(
                        config["subjectAltNames"]
                    )
                else:
                    self.subject_alt_names = None
            else:
                self.subject_alt_names = None
        else:
            self.subject = None
            self.subject_alt_names = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "subject": self.subject,
            "subjectAltNames": self.subject_alt_names
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
