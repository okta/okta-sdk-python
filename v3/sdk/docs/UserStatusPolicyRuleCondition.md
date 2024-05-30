# UserStatusPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**PolicyUserStatus**](PolicyUserStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_status_policy_rule_condition import UserStatusPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of UserStatusPolicyRuleCondition from a JSON string
user_status_policy_rule_condition_instance = UserStatusPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(UserStatusPolicyRuleCondition.to_json())

# convert the object into a dict
user_status_policy_rule_condition_dict = user_status_policy_rule_condition_instance.to_dict()
# create an instance of UserStatusPolicyRuleCondition from a dict
user_status_policy_rule_condition_form_dict = user_status_policy_rule_condition.from_dict(user_status_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


