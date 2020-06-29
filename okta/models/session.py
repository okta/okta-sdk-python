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


class Session:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.amr = config["amr"]
            self.created_at = config["createdAt"]
            self.expires_at = config["expiresAt"]
            self.id = config["id"]
            self.idp = config["idp"]
            self.last_factor_verification = config["lastFactorVerification"]
            self.last_password_verification = config["lastPasswordVerification"]
            self.login = config["login"]
            self.status = config["status"]
            self.user_id = config["userId"]
        else:
            self.links = None
            self.amr = None
            self.created_at = None
            self.expires_at = None
            self.id = None
            self.idp = None
            self.last_factor_verification = None
            self.last_password_verification = None
            self.login = None
            self.status = None
            self.user_id = None

# End of File Generation
