# ContextPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrated** | **bool** |  | [optional] 
**platform** | [**DevicePolicyRuleConditionPlatform**](DevicePolicyRuleConditionPlatform.md) |  | [optional] 
**rooted** | **bool** |  | [optional] 
**trust_level** | [**DevicePolicyTrustLevel**](DevicePolicyTrustLevel.md) |  | [optional] 
**expression** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.context_policy_rule_condition import ContextPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ContextPolicyRuleCondition from a JSON string
context_policy_rule_condition_instance = ContextPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(ContextPolicyRuleCondition.to_json())

# convert the object into a dict
context_policy_rule_condition_dict = context_policy_rule_condition_instance.to_dict()
# create an instance of ContextPolicyRuleCondition from a dict
context_policy_rule_condition_form_dict = context_policy_rule_condition.from_dict(context_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


