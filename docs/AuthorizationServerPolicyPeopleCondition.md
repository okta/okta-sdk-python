# AuthorizationServerPolicyPeopleCondition

Identifies Users and Groups that are used together

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**AuthorizationServerPolicyRuleGroupCondition**](AuthorizationServerPolicyRuleGroupCondition.md) |  | [optional] 
**users** | [**AuthorizationServerPolicyRuleUserCondition**](AuthorizationServerPolicyRuleUserCondition.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server_policy_people_condition import AuthorizationServerPolicyPeopleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyPeopleCondition from a JSON string
authorization_server_policy_people_condition_instance = AuthorizationServerPolicyPeopleCondition.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyPeopleCondition.to_json())

# convert the object into a dict
authorization_server_policy_people_condition_dict = authorization_server_policy_people_condition_instance.to_dict()
# create an instance of AuthorizationServerPolicyPeopleCondition from a dict
authorization_server_policy_people_condition_from_dict = AuthorizationServerPolicyPeopleCondition.from_dict(authorization_server_policy_people_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


