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

from aenum import MultiValueEnum


class ApplicationCredentialsScheme(
    str,
    MultiValueEnum
):
    """
    An enumeration class for ApplicationCredentialsScheme.
    """

    SHARED_USERNAME_AND_PASSWORD = "SHARED_USERNAME_AND_PASSWORD", "shared_username_and_password"
    EXTERNAL_PASSWORD_SYNC = "EXTERNAL_PASSWORD_SYNC", "external_password_sync"
    EDIT_USERNAME_AND_PASSWORD = "EDIT_USERNAME_AND_PASSWORD", "edit_username_and_password"
    EDIT_PASSWORD_ONLY = "EDIT_PASSWORD_ONLY", "edit_password_only"
    ADMIN_SETS_CREDENTIALS = "ADMIN_SETS_CREDENTIALS", "admin_sets_credentials"
