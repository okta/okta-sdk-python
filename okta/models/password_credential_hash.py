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


class PasswordCredentialHash(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.algorithm = config["algorithm"]\
                if "algorithm" in config else None
            self.salt = config["salt"]\
                if "salt" in config else None
            self.salt_order = config["saltOrder"]\
                if "saltOrder" in config else None
            self.value = config["value"]\
                if "value" in config else None
            self.worker_factor = config["workerFactor"]\
                if "workerFactor" in config else None
        else:
            self.algorithm = None
            self.salt = None
            self.salt_order = None
            self.value = None
            self.worker_factor = None
