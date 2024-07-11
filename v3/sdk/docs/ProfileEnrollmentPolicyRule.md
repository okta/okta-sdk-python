# ProfileEnrollmentPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**ProfileEnrollmentPolicyRuleActions**](ProfileEnrollmentPolicyRuleActions.md) |  | [optional] 
**conditions** | [**PolicyRuleConditions**](PolicyRuleConditions.md) |  | [optional] 

## Example

```python
from okta.models.profile_enrollment_policy_rule import ProfileEnrollmentPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileEnrollmentPolicyRule from a JSON string
profile_enrollment_policy_rule_instance = ProfileEnrollmentPolicyRule.from_json(json)
# print the JSON string representation of the object
print(ProfileEnrollmentPolicyRule.to_json())

# convert the object into a dict
profile_enrollment_policy_rule_dict = profile_enrollment_policy_rule_instance.to_dict()
# create an instance of ProfileEnrollmentPolicyRule from a dict
profile_enrollment_policy_rule_from_dict = ProfileEnrollmentPolicyRule.from_dict(profile_enrollment_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


