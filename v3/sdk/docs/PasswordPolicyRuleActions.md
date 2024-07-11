# PasswordPolicyRuleActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_change** | [**PasswordPolicyRuleAction**](PasswordPolicyRuleAction.md) |  | [optional] 
**self_service_password_reset** | [**SelfServicePasswordResetAction**](SelfServicePasswordResetAction.md) |  | [optional] 
**self_service_unlock** | [**PasswordPolicyRuleAction**](PasswordPolicyRuleAction.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_rule_actions import PasswordPolicyRuleActions

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRuleActions from a JSON string
password_policy_rule_actions_instance = PasswordPolicyRuleActions.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRuleActions.to_json())

# convert the object into a dict
password_policy_rule_actions_dict = password_policy_rule_actions_instance.to_dict()
# create an instance of PasswordPolicyRuleActions from a dict
password_policy_rule_actions_from_dict = PasswordPolicyRuleActions.from_dict(password_policy_rule_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


