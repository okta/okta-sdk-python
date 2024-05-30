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


class ClientSecret(
    OktaObject
):
    """
    A class for ClientSecret objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "_links" in config:
                self.links = config["_links"]
            self.client_secret = config["clientSecret"]\
                if "clientSecret" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.secret_hash = config["secretHash"]\
                if "secretHash" in config else None
            self.status = config["status"]\
                if "status" in config else None
        else:
            self.links = None
            self.client_secret = None
            self.created = None
            self.id = None
            self.last_updated = None
            self.secret_hash = None
            self.status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "client_secret": self.client_secret,
            "created": self.created,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "secret_hash": self.secret_hash,
            "status": self.status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
