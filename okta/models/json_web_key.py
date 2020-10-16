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


class JsonWebKey(
    OktaObject
):
    """
    A class for JsonWebKey objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.alg = config["alg"]\
                if "alg" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.e = config["e"]\
                if "e" in config else None
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.key_ops = OktaCollection.form_list(
                config["keyOps"] if "keyOps"\
                    in config else [],
                str
            )
            self.kid = config["kid"]\
                if "kid" in config else None
            self.kty = config["kty"]\
                if "kty" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.n = config["n"]\
                if "n" in config else None
            self.status = config["status"]\
                if "status" in config else None
            self.use = config["use"]\
                if "use" in config else None
            self.x_5_c = OktaCollection.form_list(
                config["x5C"] if "x5C"\
                    in config else [],
                str
            )
            self.x_5_t = config["x5T"]\
                if "x5T" in config else None
            self.x_5_t_s_256 = config["x5TS256"]\
                if "x5TS256" in config else None
            self.x_5_u = config["x5U"]\
                if "x5U" in config else None
        else:
            self.links = None
            self.alg = None
            self.created = None
            self.e = None
            self.expires_at = None
            self.key_ops = []
            self.kid = None
            self.kty = None
            self.last_updated = None
            self.n = None
            self.status = None
            self.use = None
            self.x_5_c = []
            self.x_5_t = None
            self.x_5_t_s_256 = None
            self.x_5_u = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "alg": self.alg,
            "created": self.created,
            "e": self.e,
            "expiresAt": self.expires_at,
            "key_ops": self.key_ops,
            "kid": self.kid,
            "kty": self.kty,
            "lastUpdated": self.last_updated,
            "n": self.n,
            "status": self.status,
            "use": self.use,
            "x5c": self.x_5_c,
            "x5t": self.x_5_t,
            "x5t#S256": self.x_5_t_s_256,
            "x5u": self.x_5_u
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
