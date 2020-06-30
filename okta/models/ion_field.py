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


class IonField(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.form = config["form"]\
                if "form" in config else None
            self.label = config["label"]\
                if "label" in config else None
            self.mutable = config["mutable"]\
                if "mutable" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.required = config["required"]\
                if "required" in config else None
            self.secret = config["secret"]\
                if "secret" in config else None
            self.type = config["type"]\
                if "type" in config else None
            self.value = config["value"]\
                if "value" in config else None
            self.visible = config["visible"]\
                if "visible" in config else None
        else:
            self.form = None
            self.label = None
            self.mutable = None
            self.name = None
            self.required = None
            self.secret = None
            self.type = None
            self.value = None
            self.visible = None

# End of File Generation
