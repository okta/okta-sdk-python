# AuthServerLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**claims** | [**AuthServerLinksAllOfClaims**](AuthServerLinksAllOfClaims.md) |  | [optional] 
**deactivate** | [**HrefObjectDeactivateLink**](HrefObjectDeactivateLink.md) |  | [optional] 
**metadata** | [**List[HrefObject]**](HrefObject.md) | Link to the authorization server metadata | [optional] 
**policies** | [**AuthServerLinksAllOfPolicies**](AuthServerLinksAllOfPolicies.md) |  | [optional] 
**rotate_key** | [**AuthServerLinksAllOfRotateKey**](AuthServerLinksAllOfRotateKey.md) |  | [optional] 
**scopes** | [**AuthServerLinksAllOfScopes**](AuthServerLinksAllOfScopes.md) |  | [optional] 

## Example

```python
from okta.models.auth_server_links import AuthServerLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AuthServerLinks from a JSON string
auth_server_links_instance = AuthServerLinks.from_json(json)
# print the JSON string representation of the object
print(AuthServerLinks.to_json())

# convert the object into a dict
auth_server_links_dict = auth_server_links_instance.to_dict()
# create an instance of AuthServerLinks from a dict
auth_server_links_from_dict = AuthServerLinks.from_dict(auth_server_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


