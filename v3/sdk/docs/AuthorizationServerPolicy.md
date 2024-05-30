# AuthorizationServerPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**PolicyRuleConditions**](PolicyRuleConditions.md) |  | [optional] 

## Example

```python
from openapi_client.models.authorization_server_policy import AuthorizationServerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicy from a JSON string
authorization_server_policy_instance = AuthorizationServerPolicy.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicy.to_json())

# convert the object into a dict
authorization_server_policy_dict = authorization_server_policy_instance.to_dict()
# create an instance of AuthorizationServerPolicy from a dict
authorization_server_policy_form_dict = authorization_server_policy.from_dict(authorization_server_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


