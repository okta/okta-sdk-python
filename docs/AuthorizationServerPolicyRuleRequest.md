# AuthorizationServerPolicyRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**AuthorizationServerPolicyRuleActions**](AuthorizationServerPolicyRuleActions.md) |  | [optional] 
**conditions** | [**AuthorizationServerPolicyRuleConditions**](AuthorizationServerPolicyRuleConditions.md) |  | 
**created** | **datetime** | Timestamp when the rule was created | [optional] [readonly] 
**id** | **str** | Identifier of the rule | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the rule was last modified | [optional] [readonly] 
**name** | **str** | Name of the rule | 
**priority** | **int** | Priority of the rule | [optional] 
**status** | **str** | Status of the rule | [optional] 
**system** | **bool** | Set to &#x60;true&#x60; for system rules. You can&#39;t delete system rules. | [optional] 
**type** | **str** | Rule type | 
**links** | [**LinksSelfAndLifecycle**](LinksSelfAndLifecycle.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server_policy_rule_request import AuthorizationServerPolicyRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyRuleRequest from a JSON string
authorization_server_policy_rule_request_instance = AuthorizationServerPolicyRuleRequest.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyRuleRequest.to_json())

# convert the object into a dict
authorization_server_policy_rule_request_dict = authorization_server_policy_rule_request_instance.to_dict()
# create an instance of AuthorizationServerPolicyRuleRequest from a dict
authorization_server_policy_rule_request_from_dict = AuthorizationServerPolicyRuleRequest.from_dict(authorization_server_policy_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


