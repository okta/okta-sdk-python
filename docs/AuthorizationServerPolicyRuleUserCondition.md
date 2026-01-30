# AuthorizationServerPolicyRuleUserCondition

Specifies a set of Users to be included

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Users to be included | [optional] 

## Example

```python
from okta.models.authorization_server_policy_rule_user_condition import AuthorizationServerPolicyRuleUserCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyRuleUserCondition from a JSON string
authorization_server_policy_rule_user_condition_instance = AuthorizationServerPolicyRuleUserCondition.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyRuleUserCondition.to_json())

# convert the object into a dict
authorization_server_policy_rule_user_condition_dict = authorization_server_policy_rule_user_condition_instance.to_dict()
# create an instance of AuthorizationServerPolicyRuleUserCondition from a dict
authorization_server_policy_rule_user_condition_from_dict = AuthorizationServerPolicyRuleUserCondition.from_dict(authorization_server_policy_rule_user_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


