# TokenAuthorizationServerPolicyRuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_lifetime_minutes** | **int** |  | [optional] 
**inline_hook** | [**TokenAuthorizationServerPolicyRuleActionInlineHook**](TokenAuthorizationServerPolicyRuleActionInlineHook.md) |  | [optional] 
**refresh_token_lifetime_minutes** | **int** |  | [optional] 
**refresh_token_window_minutes** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.token_authorization_server_policy_rule_action import TokenAuthorizationServerPolicyRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of TokenAuthorizationServerPolicyRuleAction from a JSON string
token_authorization_server_policy_rule_action_instance = TokenAuthorizationServerPolicyRuleAction.from_json(json)
# print the JSON string representation of the object
print(TokenAuthorizationServerPolicyRuleAction.to_json())

# convert the object into a dict
token_authorization_server_policy_rule_action_dict = token_authorization_server_policy_rule_action_instance.to_dict()
# create an instance of TokenAuthorizationServerPolicyRuleAction from a dict
token_authorization_server_policy_rule_action_from_dict = TokenAuthorizationServerPolicyRuleAction.from_dict(token_authorization_server_policy_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


