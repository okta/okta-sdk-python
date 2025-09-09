# PolicyRuleActionsEnroll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**PolicyRuleActionsEnrollSelf**](PolicyRuleActionsEnrollSelf.md) |  | [optional] 

## Example

```python
from okta.models.policy_rule_actions_enroll import PolicyRuleActionsEnroll

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleActionsEnroll from a JSON string
policy_rule_actions_enroll_instance = PolicyRuleActionsEnroll.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleActionsEnroll.to_json())

# convert the object into a dict
policy_rule_actions_enroll_dict = policy_rule_actions_enroll_instance.to_dict()
# create an instance of PolicyRuleActionsEnroll from a dict
policy_rule_actions_enroll_from_dict = PolicyRuleActionsEnroll.from_dict(policy_rule_actions_enroll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


