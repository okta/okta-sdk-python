# PasswordPolicyRuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**PolicyAccess**](PolicyAccess.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_rule_action import PasswordPolicyRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRuleAction from a JSON string
password_policy_rule_action_instance = PasswordPolicyRuleAction.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRuleAction.to_json())

# convert the object into a dict
password_policy_rule_action_dict = password_policy_rule_action_instance.to_dict()
# create an instance of PasswordPolicyRuleAction from a dict
password_policy_rule_action_from_dict = PasswordPolicyRuleAction.from_dict(password_policy_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


