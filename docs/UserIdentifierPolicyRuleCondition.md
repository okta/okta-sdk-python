# UserIdentifierPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**patterns** | [**List[UserIdentifierConditionEvaluatorPattern]**](UserIdentifierConditionEvaluatorPattern.md) |  | [optional] 
**type** | [**UserIdentifierType**](UserIdentifierType.md) |  | [optional] 

## Example

```python
from okta.models.user_identifier_policy_rule_condition import UserIdentifierPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentifierPolicyRuleCondition from a JSON string
user_identifier_policy_rule_condition_instance = UserIdentifierPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(UserIdentifierPolicyRuleCondition.to_json())

# convert the object into a dict
user_identifier_policy_rule_condition_dict = user_identifier_policy_rule_condition_instance.to_dict()
# create an instance of UserIdentifierPolicyRuleCondition from a dict
user_identifier_policy_rule_condition_from_dict = UserIdentifierPolicyRuleCondition.from_dict(user_identifier_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


