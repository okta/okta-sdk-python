# AuthorizationServerPolicyRuleConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_types** | [**GrantTypePolicyRuleCondition**](GrantTypePolicyRuleCondition.md) |  | [optional] 
**people** | [**AuthorizationServerPolicyPeopleCondition**](AuthorizationServerPolicyPeopleCondition.md) |  | [optional] 
**scopes** | [**OAuth2ScopesMediationPolicyRuleCondition**](OAuth2ScopesMediationPolicyRuleCondition.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server_policy_rule_conditions import AuthorizationServerPolicyRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyRuleConditions from a JSON string
authorization_server_policy_rule_conditions_instance = AuthorizationServerPolicyRuleConditions.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyRuleConditions.to_json())

# convert the object into a dict
authorization_server_policy_rule_conditions_dict = authorization_server_policy_rule_conditions_instance.to_dict()
# create an instance of AuthorizationServerPolicyRuleConditions from a dict
authorization_server_policy_rule_conditions_from_dict = AuthorizationServerPolicyRuleConditions.from_dict(authorization_server_policy_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


