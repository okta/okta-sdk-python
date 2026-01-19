# AuthorizationServerPolicyConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**ClientPolicyCondition**](ClientPolicyCondition.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server_policy_conditions import AuthorizationServerPolicyConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyConditions from a JSON string
authorization_server_policy_conditions_instance = AuthorizationServerPolicyConditions.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyConditions.to_json())

# convert the object into a dict
authorization_server_policy_conditions_dict = authorization_server_policy_conditions_instance.to_dict()
# create an instance of AuthorizationServerPolicyConditions from a dict
authorization_server_policy_conditions_from_dict = AuthorizationServerPolicyConditions.from_dict(authorization_server_policy_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


