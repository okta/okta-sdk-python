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


class IonForm(
    OktaObject
):
    """
    A class for IonForm objects.
    """

    def __init__(self, config=None):
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
            self.rel = config["rel"]\
                if "rel" in config else None
            self.relates_to = config["relatesTo"]\
                if "relatesTo" in config else None
            self.value = config["value"]\
                if "value" in config else None
        else:
            self.accepts = None
            self.href = None
            self.method = None
            self.name = None
            self.produces = None
            self.refresh = None
            self.rel = None
            self.relates_to = None
            self.value = None
