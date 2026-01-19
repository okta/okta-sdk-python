# GroupRuleExpression

Defines Okta specific [group-rules expression](https://developer.okta.com/docs/reference/okta-expression-language/#expressions-in-group-rules)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Expression type. Only valid value is &#39;&#x60;urn:okta:expression:1.0&#x60;&#39;. | [optional] 
**value** | **str** | Okta expression that would result in a Boolean value | [optional] 

## Example

```python
from okta.models.group_rule_expression import GroupRuleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRuleExpression from a JSON string
group_rule_expression_instance = GroupRuleExpression.from_json(json)
# print the JSON string representation of the object
print(GroupRuleExpression.to_json())

# convert the object into a dict
group_rule_expression_dict = group_rule_expression_instance.to_dict()
# create an instance of GroupRuleExpression from a dict
group_rule_expression_from_dict = GroupRuleExpression.from_dict(group_rule_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


