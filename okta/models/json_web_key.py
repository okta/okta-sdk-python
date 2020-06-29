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


class JsonWebKey:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.alg = config["alg"]
            self.created = config["created"]
            self.e = config["e"]
            self.expires_at = config["expiresAt"]
            self.key_ops = config["key_ops"]
            self.kid = config["kid"]
            self.kty = config["kty"]
            self.last_updated = config["lastUpdated"]
            self.n = config["n"]
            self.status = config["status"]
            self.use = config["use"]
            self.x_5_c = config["x5c"]
            self.x_5_t = config["x5t"]
            self.x_5_t_s_256 = config["x5t#S256"]
            self.x_5_u = config["x5u"]
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

# End of File Generation
