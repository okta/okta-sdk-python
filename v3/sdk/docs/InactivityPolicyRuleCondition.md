# InactivityPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from okta.models.inactivity_policy_rule_condition import InactivityPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of InactivityPolicyRuleCondition from a JSON string
inactivity_policy_rule_condition_instance = InactivityPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(InactivityPolicyRuleCondition.to_json())

# convert the object into a dict
inactivity_policy_rule_condition_dict = inactivity_policy_rule_condition_instance.to_dict()
# create an instance of InactivityPolicyRuleCondition from a dict
inactivity_policy_rule_condition_from_dict = InactivityPolicyRuleCondition.from_dict(inactivity_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


