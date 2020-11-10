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
from okta.models import authorization_server_credentials\
    as authorization_server_credentials


class AuthorizationServer(
    OktaObject
):
    """
    A class for AuthorizationServer objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.audiences = OktaCollection.form_list(
                config["audiences"] if "audiences"\
                    in config else [],
                str
            )
            self.created = config["created"]\
                if "created" in config else None
            if "credentials" in config:
                if isinstance(config["credentials"],
                              authorization_server_credentials.AuthorizationServerCredentials):
                    self.credentials = config["credentials"]
                elif config["credentials"] is not None:
                    self.credentials = authorization_server_credentials.AuthorizationServerCredentials(
                        config["credentials"]
                    )
                else:
                    self.credentials = None
            else:
                self.credentials = None
            self.description = config["description"]\
                if "description" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.issuer = config["issuer"]\
                if "issuer" in config else None
            self.issuer_mode = config["issuerMode"]\
                if "issuerMode" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.status = config["status"]\
                if "status" in config else None
        else:
            self.links = None
            self.audiences = []
            self.created = None
            self.credentials = None
            self.description = None
            self.id = None
            self.issuer = None
            self.issuer_mode = None
            self.last_updated = None
            self.name = None
            self.status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "audiences": self.audiences,
            "created": self.created,
            "credentials": self.credentials,
            "description": self.description,
            "id": self.id,
            "issuer": self.issuer,
            "issuerMode": self.issuer_mode,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "status": self.status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
