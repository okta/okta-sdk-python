# GroupRuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assign_user_to_groups** | [**GroupRuleGroupAssignment**](GroupRuleGroupAssignment.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_rule_action import GroupRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRuleAction from a JSON string
group_rule_action_instance = GroupRuleAction.from_json(json)
# print the JSON string representation of the object
print(GroupRuleAction.to_json())

# convert the object into a dict
group_rule_action_dict = group_rule_action_instance.to_dict()
# create an instance of GroupRuleAction from a dict
group_rule_action_form_dict = group_rule_action.from_dict(group_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


