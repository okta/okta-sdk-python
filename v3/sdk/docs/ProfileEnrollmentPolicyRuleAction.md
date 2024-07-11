# ProfileEnrollmentPolicyRuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** |  | [optional] 
**activation_requirements** | [**ProfileEnrollmentPolicyRuleActivationRequirement**](ProfileEnrollmentPolicyRuleActivationRequirement.md) |  | [optional] 
**pre_registration_inline_hooks** | [**List[PreRegistrationInlineHook]**](PreRegistrationInlineHook.md) |  | [optional] 
**profile_attributes** | [**List[ProfileEnrollmentPolicyRuleProfileAttribute]**](ProfileEnrollmentPolicyRuleProfileAttribute.md) |  | [optional] 
**target_group_ids** | **List[str]** |  | [optional] 
**unknown_user_action** | **str** |  | [optional] 
**progressive_profiling_action** | **str** |  | [optional] 

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


