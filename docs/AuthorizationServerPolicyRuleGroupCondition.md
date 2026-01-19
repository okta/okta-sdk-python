# AuthorizationServerPolicyRuleGroupCondition

Specifies a set of Groups whose Users are to be included

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Groups to be included | [optional] 

## Example

```python
from okta.models.authorization_server_policy_rule_group_condition import AuthorizationServerPolicyRuleGroupCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyRuleGroupCondition from a JSON string
authorization_server_policy_rule_group_condition_instance = AuthorizationServerPolicyRuleGroupCondition.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyRuleGroupCondition.to_json())

# convert the object into a dict
authorization_server_policy_rule_group_condition_dict = authorization_server_policy_rule_group_condition_instance.to_dict()
# create an instance of AuthorizationServerPolicyRuleGroupCondition from a dict
authorization_server_policy_rule_group_condition_from_dict = AuthorizationServerPolicyRuleGroupCondition.from_dict(authorization_server_policy_rule_group_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


