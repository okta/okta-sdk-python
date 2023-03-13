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
from okta.models import profile_enrollment_policy_rule_activation_requirement\
    as profile_enrollment_policy_rule_activation_requirement
from okta.models import pre_registration_inline_hook\
    as pre_registration_inline_hook
from okta.models import profile_enrollment_policy_rule_profile_attribute\
    as profile_enrollment_policy_rule_profile_attribute


class ProfileEnrollmentPolicyRuleAction(
    OktaObject
):
    """
    A class for ProfileEnrollmentPolicyRuleAction objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.access = config["access"]\
                if "access" in config else None
            if "activationRequirements" in config:
                if isinstance(config["activationRequirements"],
                              profile_enrollment_policy_rule_activation_requirement.ProfileEnrollmentPolicyRuleActivationRequirement):
                    self.activation_requirements = config["activationRequirements"]
                elif config["activationRequirements"] is not None:
                    self.activation_requirements = profile_enrollment_policy_rule_activation_requirement.ProfileEnrollmentPolicyRuleActivationRequirement(
                        config["activationRequirements"]
                    )
                else:
                    self.activation_requirements = None
            else:
                self.activation_requirements = None
            self.pre_registration_inline_hooks = OktaCollection.form_list(
                config["preRegistrationInlineHooks"] if "preRegistrationInlineHooks"\
                    in config else [],
                pre_registration_inline_hook.PreRegistrationInlineHook
            )
            self.profile_attributes = OktaCollection.form_list(
                config["profileAttributes"] if "profileAttributes"\
                    in config else [],
                profile_enrollment_policy_rule_profile_attribute.ProfileEnrollmentPolicyRuleProfileAttribute
            )
            self.target_group_ids = OktaCollection.form_list(
                config["targetGroupIds"] if "targetGroupIds"\
                    in config else [],
                str
            )
            self.ui_schema_id = config["uiSchemaId"]\
                if "uiSchemaId" in config else None
            self.unknown_user_action = config["unknownUserAction"]\
                if "unknownUserAction" in config else None
        else:
            self.access = None
            self.activation_requirements = None
            self.pre_registration_inline_hooks = []
            self.profile_attributes = []
            self.target_group_ids = []
            self.ui_schema_id = None
            self.unknown_user_action = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "access": self.access,
            "activationRequirements": self.activation_requirements,
            "preRegistrationInlineHooks": self.pre_registration_inline_hooks,
            "profileAttributes": self.profile_attributes,
            "targetGroupIds": self.target_group_ids,
            "uiSchemaId": self.ui_schema_id,
            "unknownUserAction": self.unknown_user_action
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
