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


class WsFederationApplicationSettingsApplication:
    def __init__(self, config=None):
        if config:
            self.attribute_statements = config["attributeStatements"]
            self.audience_restriction = config["audienceRestriction"]
            self.authn_context_class_ref = config["authnContextClassRef"]
            self.group_filter = config["groupFilter"]
            self.group_name = config["groupName"]
            self.group_value_format = config["groupValueFormat"]
            self.name_id_format = config["nameIDFormat"]
            self.realm = config["realm"]
            self.site_url = config["siteURL"]
            self.username_attribute = config["usernameAttribute"]
            self.w_reply_override = config["wReplyOverride"]
            self.w_reply_url = config["wReplyURL"]
        else:
            self.attribute_statements = None
            self.audience_restriction = None
            self.authn_context_class_ref = None
            self.group_filter = None
            self.group_name = None
            self.group_value_format = None
            self.name_id_format = None
            self.realm = None
            self.site_url = None
            self.username_attribute = None
            self.w_reply_override = None
            self.w_reply_url = None

# End of File Generation
