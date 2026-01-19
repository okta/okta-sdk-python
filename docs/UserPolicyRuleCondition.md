# UserPolicyRuleCondition

Specifies a set of Users to be included or excluded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Users to be excluded | [optional] 
**inactivity** | [**InactivityPolicyRuleCondition**](InactivityPolicyRuleCondition.md) |  | [optional] 
**include** | **List[str]** | Users to be included | [optional] 
**lifecycle_expiration** | [**LifecycleExpirationPolicyRuleCondition**](LifecycleExpirationPolicyRuleCondition.md) |  | [optional] 
**password_expiration** | [**PasswordExpirationPolicyRuleCondition**](PasswordExpirationPolicyRuleCondition.md) |  | [optional] 
**user_lifecycle_attribute** | [**UserLifecycleAttributePolicyRuleCondition**](UserLifecycleAttributePolicyRuleCondition.md) |  | [optional] 

## Example

```python
from okta.models.user_policy_rule_condition import UserPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of UserPolicyRuleCondition from a JSON string
user_policy_rule_condition_instance = UserPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(UserPolicyRuleCondition.to_json())

# convert the object into a dict
user_policy_rule_condition_dict = user_policy_rule_condition_instance.to_dict()
# create an instance of UserPolicyRuleCondition from a dict
user_policy_rule_condition_from_dict = UserPolicyRuleCondition.from_dict(user_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


