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
from okta.models import ion_field\
    as ion_field


class IonForm(
    OktaObject
):
    """
    A class for IonForm objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.accepts = config["accepts"]\
                if "accepts" in config else None
            self.href = config["href"]\
                if "href" in config else None
            self.method = config["method"]\
                if "method" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.produces = config["produces"]\
                if "produces" in config else None
            self.refresh = config["refresh"]\
                if "refresh" in config else None
            self.rel = OktaCollection.form_list(
                config["rel"] if "rel"\
                    in config else [],
                str
            )
            self.relates_to = OktaCollection.form_list(
                config["relatesTo"] if "relatesTo"\
                    in config else [],
                str
            )
            self.value = OktaCollection.form_list(
                config["value"] if "value"\
                    in config else [],
                ion_field.IonField
            )
        else:
            self.accepts = None
            self.href = None
            self.method = None
            self.name = None
            self.produces = None
            self.refresh = None
            self.rel = []
            self.relates_to = []
            self.value = []

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "accepts": self.accepts,
            "href": self.href,
            "method": self.method,
            "name": self.name,
            "produces": self.produces,
            "refresh": self.refresh,
            "rel": self.rel,
            "relatesTo": self.relates_to,
            "value": self.value
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
