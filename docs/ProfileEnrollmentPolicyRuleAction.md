# ProfileEnrollmentPolicyRuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | Indicates if the user profile is granted access  &gt; **Note:** You can&#39;t set the &#x60;access&#x60; property to &#x60;DENY&#x60; after you create the policy | [optional] 
**activation_requirements** | [**ProfileEnrollmentPolicyRuleActivationRequirement**](ProfileEnrollmentPolicyRuleActivationRequirement.md) |  | [optional] 
**allowed_identifiers** | **List[str]** | A list of attributes to identify an end user. Can be used across Okta sign-in, unlock, and recovery flows. | [optional] [default to ["login"]]
**enroll_authenticator_types** | **List[str]** | Additional authenticator fields that can be used on the first page of user registration. Valid values only includes &#x60;&#39;password&#39;&#x60;. | [optional] 
**pre_registration_inline_hooks** | [**List[PreRegistrationInlineHook]**](PreRegistrationInlineHook.md) | (Optional) The &#x60;id&#x60; of at most one registration inline hook | [optional] 
**profile_attributes** | [**List[ProfileEnrollmentPolicyRuleProfileAttribute]**](ProfileEnrollmentPolicyRuleProfileAttribute.md) | A list of attributes to prompt the user for during registration or progressive profiling. Where defined on the user schema, these attributes are persisted in the user profile. You can also add non-schema attributes, which aren&#39;t persisted to the user&#39;s profile, but are included in requests to the registration inline hook. A maximum of 10 profile properties is supported. | [optional] 
**progressive_profiling_action** | **str** | Progressive profile enrollment helps evaluate the user profile policy at every user login. Users can be prompted to provide input for newly required attributes. | [optional] 
**target_group_ids** | **List[str]** | (Optional, max 1 entry) The &#x60;id&#x60; of a group that this user should be added to | [optional] 
**ui_schema_id** | **str** | Value created by the backend. If present, all policy updates must include this attribute/value. | [optional] 
**unknown_user_action** | **str** | Which action should be taken if this user is new | [optional] 

## Example

```python
from okta.models.profile_enrollment_policy_rule_action import ProfileEnrollmentPolicyRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileEnrollmentPolicyRuleAction from a JSON string
profile_enrollment_policy_rule_action_instance = ProfileEnrollmentPolicyRuleAction.from_json(json)
# print the JSON string representation of the object
print(ProfileEnrollmentPolicyRuleAction.to_json())

# convert the object into a dict
profile_enrollment_policy_rule_action_dict = profile_enrollment_policy_rule_action_instance.to_dict()
# create an instance of ProfileEnrollmentPolicyRuleAction from a dict
profile_enrollment_policy_rule_action_from_dict = ProfileEnrollmentPolicyRuleAction.from_dict(profile_enrollment_policy_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


