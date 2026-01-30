# GroupRulePeopleCondition

Defines conditions for `people` in a group rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**GroupRuleGroupCondition**](GroupRuleGroupCondition.md) |  | [optional] 
**users** | [**GroupRuleUserCondition**](GroupRuleUserCondition.md) |  | [optional] 

## Example

```python
from okta.models.group_rule_people_condition import GroupRulePeopleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRulePeopleCondition from a JSON string
group_rule_people_condition_instance = GroupRulePeopleCondition.from_json(json)
# print the JSON string representation of the object
print(GroupRulePeopleCondition.to_json())

# convert the object into a dict
group_rule_people_condition_dict = group_rule_people_condition_instance.to_dict()
# create an instance of GroupRulePeopleCondition from a dict
group_rule_people_condition_from_dict = GroupRulePeopleCondition.from_dict(group_rule_people_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


