# AccessPolicyRuleCustomCondition

Specifies [Okta Expression Language](https://developer.okta.com/docs/reference/okta-expression-language-in-identity-engine/) expressions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | expression to match | 

## Example

```python
from okta.models.access_policy_rule_custom_condition import AccessPolicyRuleCustomCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyRuleCustomCondition from a JSON string
access_policy_rule_custom_condition_instance = AccessPolicyRuleCustomCondition.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyRuleCustomCondition.to_json())

# convert the object into a dict
access_policy_rule_custom_condition_dict = access_policy_rule_custom_condition_instance.to_dict()
# create an instance of AccessPolicyRuleCustomCondition from a dict
access_policy_rule_custom_condition_from_dict = AccessPolicyRuleCustomCondition.from_dict(access_policy_rule_custom_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


