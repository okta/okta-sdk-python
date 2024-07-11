# PasswordPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**PasswordPolicyRuleActions**](PasswordPolicyRuleActions.md) |  | [optional] 
**conditions** | [**PasswordPolicyRuleConditions**](PasswordPolicyRuleConditions.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_rule import PasswordPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRule from a JSON string
password_policy_rule_instance = PasswordPolicyRule.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRule.to_json())

# convert the object into a dict
password_policy_rule_dict = password_policy_rule_instance.to_dict()
# create an instance of PasswordPolicyRule from a dict
password_policy_rule_from_dict = PasswordPolicyRule.from_dict(password_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


