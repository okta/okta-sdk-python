# GroupRuleGroupAssignment

Contains the `groupIds` array

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_ids** | **List[str]** | Array of &#x60;groupIds&#x60; to which users are added | [optional] 

## Example

```python
from okta.models.group_rule_group_assignment import GroupRuleGroupAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRuleGroupAssignment from a JSON string
group_rule_group_assignment_instance = GroupRuleGroupAssignment.from_json(json)
# print the JSON string representation of the object
print(GroupRuleGroupAssignment.to_json())

# convert the object into a dict
group_rule_group_assignment_dict = group_rule_group_assignment_instance.to_dict()
# create an instance of GroupRuleGroupAssignment from a dict
group_rule_group_assignment_from_dict = GroupRuleGroupAssignment.from_dict(group_rule_group_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


