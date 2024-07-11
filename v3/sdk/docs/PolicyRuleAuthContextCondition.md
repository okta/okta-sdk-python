# PolicyRuleAuthContextCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**PolicyRuleAuthContextType**](PolicyRuleAuthContextType.md) |  | [optional] 

## Example

```python
from okta.models.policy_rule_auth_context_condition import PolicyRuleAuthContextCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleAuthContextCondition from a JSON string
policy_rule_auth_context_condition_instance = PolicyRuleAuthContextCondition.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleAuthContextCondition.to_json())

# convert the object into a dict
policy_rule_auth_context_condition_dict = policy_rule_auth_context_condition_instance.to_dict()
# create an instance of PolicyRuleAuthContextCondition from a dict
policy_rule_auth_context_condition_from_dict = PolicyRuleAuthContextCondition.from_dict(policy_rule_auth_context_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


