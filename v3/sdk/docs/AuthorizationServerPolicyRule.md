# AuthorizationServerPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**AuthorizationServerPolicyRuleActions**](AuthorizationServerPolicyRuleActions.md) |  | [optional] 
**conditions** | [**AuthorizationServerPolicyRuleConditions**](AuthorizationServerPolicyRuleConditions.md) |  | [optional] 

## Example

```python
from openapi_client.models.authorization_server_policy_rule import AuthorizationServerPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyRule from a JSON string
authorization_server_policy_rule_instance = AuthorizationServerPolicyRule.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyRule.to_json())

# convert the object into a dict
authorization_server_policy_rule_dict = authorization_server_policy_rule_instance.to_dict()
# create an instance of AuthorizationServerPolicyRule from a dict
authorization_server_policy_rule_from_dict = AuthorizationServerPolicyRule.from_dict(authorization_server_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


