# GroupRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**GroupRuleAction**](GroupRuleAction.md) |  | [optional] 
**conditions** | [**GroupRuleConditions**](GroupRuleConditions.md) |  | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**status** | [**GroupRuleStatus**](GroupRuleStatus.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from okta.models.group_rule import GroupRule

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRule from a JSON string
group_rule_instance = GroupRule.from_json(json)
# print the JSON string representation of the object
print(GroupRule.to_json())

# convert the object into a dict
group_rule_dict = group_rule_instance.to_dict()
# create an instance of GroupRule from a dict
group_rule_from_dict = GroupRule.from_dict(group_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


