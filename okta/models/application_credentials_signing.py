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


class ApplicationCredentialsSigning:
    def __init__(self, config=None):
        if config:
            self.kid = config["kid"]
            self.last_rotated = config["lastRotated"]
            self.next_rotation = config["nextRotation"]
            self.rotation_mode = config["rotationMode"]
            self.use = config["use"]
        else:
            self.kid = None
            self.last_rotated = None
            self.next_rotation = None
            self.rotation_mode = None
            self.use = None


# End of File Generation
