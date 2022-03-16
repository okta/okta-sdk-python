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


class NotificationType(
    str,
    MultiValueEnum
):
    """
    An enumeration class for NotificationType.
    """

    CONNECTOR_AGENT = "CONNECTOR_AGENT", "connector_agent"
    USER_LOCKED_OUT = "USER_LOCKED_OUT", "user_locked_out"
    APP_IMPORT = "APP_IMPORT", "app_import"
    LDAP_AGENT = "LDAP_AGENT", "ldap_agent"
    AD_AGENT = "AD_AGENT", "ad_agent"
    OKTA_ANNOUNCEMENT = "OKTA_ANNOUNCEMENT", "okta_announcement"
    OKTA_ISSUE = "OKTA_ISSUE", "okta_issue"
    OKTA_UPDATE = "OKTA_UPDATE", "okta_update"
    IWA_AGENT = "IWA_AGENT", "iwa_agent"
    USER_DEPROVISION = "USER_DEPROVISION", "user_deprovision"
    REPORT_SUSPICIOUS_ACTIVITY = "REPORT_SUSPICIOUS_ACTIVITY", "report_suspicious_activity"
    RATELIMIT_NOTIFICATION = "RATELIMIT_NOTIFICATION", "ratelimit_notification"
