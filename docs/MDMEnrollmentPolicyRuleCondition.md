# MDMEnrollmentPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_non_safe_android** | **bool** |  | [optional] 
**enrollment** | [**MDMEnrollmentPolicyEnrollment**](MDMEnrollmentPolicyEnrollment.md) |  | [optional] 

## Example

```python
from okta.models.mdm_enrollment_policy_rule_condition import MDMEnrollmentPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of MDMEnrollmentPolicyRuleCondition from a JSON string
mdm_enrollment_policy_rule_condition_instance = MDMEnrollmentPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(MDMEnrollmentPolicyRuleCondition.to_json())

# convert the object into a dict
mdm_enrollment_policy_rule_condition_dict = mdm_enrollment_policy_rule_condition_instance.to_dict()
# create an instance of MDMEnrollmentPolicyRuleCondition from a dict
mdm_enrollment_policy_rule_condition_from_dict = MDMEnrollmentPolicyRuleCondition.from_dict(mdm_enrollment_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


