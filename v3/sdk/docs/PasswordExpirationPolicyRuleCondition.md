# PasswordExpirationPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.password_expiration_policy_rule_condition import PasswordExpirationPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordExpirationPolicyRuleCondition from a JSON string
password_expiration_policy_rule_condition_instance = PasswordExpirationPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(PasswordExpirationPolicyRuleCondition.to_json())

# convert the object into a dict
password_expiration_policy_rule_condition_dict = password_expiration_policy_rule_condition_instance.to_dict()
# create an instance of PasswordExpirationPolicyRuleCondition from a dict
password_expiration_policy_rule_condition_from_dict = PasswordExpirationPolicyRuleCondition.from_dict(password_expiration_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


