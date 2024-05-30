# GroupRuleConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**GroupRuleExpression**](GroupRuleExpression.md) |  | [optional] 
**people** | [**GroupRulePeopleCondition**](GroupRulePeopleCondition.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_rule_conditions import GroupRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRuleConditions from a JSON string
group_rule_conditions_instance = GroupRuleConditions.from_json(json)
# print the JSON string representation of the object
print(GroupRuleConditions.to_json())

# convert the object into a dict
group_rule_conditions_dict = group_rule_conditions_instance.to_dict()
# create an instance of GroupRuleConditions from a dict
group_rule_conditions_form_dict = group_rule_conditions.from_dict(group_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


