# GroupRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**GroupRuleAction**](GroupRuleAction.md) |  | [optional] 
**conditions** | [**GroupRuleConditions**](GroupRuleConditions.md) |  | [optional] 
**created** | **datetime** | Creation date for group rule | [optional] [readonly] 
**id** | **str** | ID of the group rule | [optional] [readonly] 
**last_updated** | **datetime** | Date group rule was last updated | [optional] [readonly] 
**name** | **str** | Name of the group rule | [optional] 
**status** | [**GroupRuleStatus**](GroupRuleStatus.md) |  | [optional] 
**type** | **str** | Type to indicate a group rule operation. Only &#x60;group_rule&#x60; is allowed. | [optional] 

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


