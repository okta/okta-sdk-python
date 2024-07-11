# AuthenticatorLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**activate** | [**HrefObjectActivateLink**](HrefObjectActivateLink.md) |  | [optional] 
**deactivate** | [**HrefObjectDeactivateLink**](HrefObjectDeactivateLink.md) |  | [optional] 
**methods** | [**HrefObject**](HrefObject.md) | Link to Authenticator methods | [optional] 

## Example

```python
from openapi_client.models.authenticator_links import AuthenticatorLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorLinks from a JSON string
authenticator_links_instance = AuthenticatorLinks.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorLinks.to_json())

# convert the object into a dict
authenticator_links_dict = authenticator_links_instance.to_dict()
# create an instance of AuthenticatorLinks from a dict
authenticator_links_from_dict = AuthenticatorLinks.from_dict(authenticator_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


