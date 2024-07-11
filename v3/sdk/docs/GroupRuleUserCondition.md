# GroupRuleUserCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** |  | [optional] 
**include** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.group_rule_user_condition import GroupRuleUserCondition

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRuleUserCondition from a JSON string
group_rule_user_condition_instance = GroupRuleUserCondition.from_json(json)
# print the JSON string representation of the object
print(GroupRuleUserCondition.to_json())

# convert the object into a dict
group_rule_user_condition_dict = group_rule_user_condition_instance.to_dict()
# create an instance of GroupRuleUserCondition from a dict
group_rule_user_condition_from_dict = GroupRuleUserCondition.from_dict(group_rule_user_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


