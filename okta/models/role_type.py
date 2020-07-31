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


class RoleType(
    str,
    MultiValueEnum
):
    """
    An enumeration class for RoleType.
    """

    SUPER_ADMIN = "SUPER_ADMIN", "super_admin"
    ORG_ADMIN = "ORG_ADMIN", "org_admin"
    APP_ADMIN = "APP_ADMIN", "app_admin"
    USER_ADMIN = "USER_ADMIN", "user_admin"
    HELP_DESK_ADMIN = "HELP_DESK_ADMIN", "help_desk_admin"
    READ_ONLY_ADMIN = "READ_ONLY_ADMIN", "read_only_admin"
    MOBILE_ADMIN = "MOBILE_ADMIN", "mobile_admin"
    API_ACCESS_MANAGEMENT_ADMIN = "API_ACCESS_MANAGEMENT_ADMIN", "api_access_management_admin"
    REPORT_ADMIN = "REPORT_ADMIN", "report_admin"
