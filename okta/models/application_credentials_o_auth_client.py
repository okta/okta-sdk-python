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


from urllib.parse import urlencode


class ApplicationCredentialsOAuthClient:
    def __init__(self, config=None):
        if config:
            self.auto_key_rotation = config["autoKeyRotation"]
            self.client_id = config["client_id"]
            self.client_secret = config["client_secret"]
            self.token_endpoint_auth_method = config["token_endpoint_auth_method"]
        else:
            self.auto_key_rotation = None
            self.client_id = None
            self.client_secret = None
            self.token_endpoint_auth_method = None


# End of File Generation
