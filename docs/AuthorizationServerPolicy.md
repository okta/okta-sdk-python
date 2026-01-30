# AuthorizationServerPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Policy | [optional] 
**type** | **str** | Indicates that the Policy is an authorization server Policy | [optional] 
**name** | **str** | Name of the Policy | [optional] 
**conditions** | [**AuthorizationServerPolicyConditions**](AuthorizationServerPolicyConditions.md) |  | [optional] 
**description** | **str** | Description of the Policy | [optional] 
**priority** | **int** | Specifies the order in which this Policy is evaluated in relation to the other Policies in a custom authorization server | [optional] 
**status** | **str** | Specifies whether requests have access to this Policy | [optional] 
**system** | **bool** | Specifies whether Okta created this Policy | [optional] 
**created** | **datetime** | Timestamp when the Policy was created | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the Policy was last updated | [optional] [readonly] 
**links** | [**AuthorizationServerPolicyAllOfLinks**](AuthorizationServerPolicyAllOfLinks.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server_policy import AuthorizationServerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicy from a JSON string
authorization_server_policy_instance = AuthorizationServerPolicy.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicy.to_json())

# convert the object into a dict
authorization_server_policy_dict = authorization_server_policy_instance.to_dict()
# create an instance of AuthorizationServerPolicy from a dict
authorization_server_policy_from_dict = AuthorizationServerPolicy.from_dict(authorization_server_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


