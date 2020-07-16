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


class JsonWebKey(
    OktaObject
):
    """
    A class for JsonWebKey objects.
    """

    def __init__(self, config=None):
        if config:
            self.links = config["_links"]\
                if "_links" in config else None
            self.alg = config["alg"]\
                if "alg" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.e = config["e"]\
                if "e" in config else None
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.key_ops = config["key_ops"]\
                if "key_ops" in config else None
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
            self.x_5_c = config["x5c"]\
                if "x5c" in config else None
            self.x_5_t = config["x5t"]\
                if "x5t" in config else None
            self.x_5_t_s_256 = config["x5t#S256"]\
                if "x5t#S256" in config else None
            self.x_5_u = config["x5u"]\
                if "x5u" in config else None
        else:
            self.links = None
            self.alg = None
            self.created = None
            self.e = None
            self.expires_at = None
            self.key_ops = None
            self.kid = None
            self.kty = None
            self.last_updated = None
            self.n = None
            self.status = None
            self.use = None
            self.x_5_c = None
            self.x_5_t = None
            self.x_5_t_s_256 = None
            self.x_5_u = None
