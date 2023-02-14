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
from okta.models import o_auth_2_actor\
    as o_auth_2_actor


class OAuth2RefreshToken(
    OktaObject
):
    """
    A class for OAuth2RefreshToken objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            self.client_id = config["clientId"]\
                if "clientId" in config else None
            self.created = config["created"]\
                if "created" in config else None
            if "createdBy" in config:
                if isinstance(config["createdBy"],
                              o_auth_2_actor.OAuth2Actor):
                    self.created_by = config["createdBy"]
                elif config["createdBy"] is not None:
                    self.created_by = o_auth_2_actor.OAuth2Actor(
                        config["createdBy"]
                    )
                else:
                    self.created_by = None
            else:
                self.created_by = None
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.issuer = config["issuer"]\
                if "issuer" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.scopes = OktaCollection.form_list(
                config["scopes"] if "scopes"\
                    in config else [],
                str
            )
            self.status = config["status"]\
                if "status" in config else None
            self.user_id = config["userId"]\
                if "userId" in config else None
        else:
            self.embedded = None
            self.links = None
            self.client_id = None
            self.created = None
            self.created_by = None
            self.expires_at = None
            self.id = None
            self.issuer = None
            self.last_updated = None
            self.scopes = []
            self.status = None
            self.user_id = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_embedded": self.embedded,
            "_links": self.links,
            "clientId": self.client_id,
            "created": self.created,
            "createdBy": self.created_by,
            "expiresAt": self.expires_at,
            "id": self.id,
            "issuer": self.issuer,
            "lastUpdated": self.last_updated,
            "scopes": self.scopes,
            "status": self.status,
            "userId": self.user_id
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
