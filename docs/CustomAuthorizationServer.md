# CustomAuthorizationServer

Custom authorization server for the managed connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_url** | **str** | Issuer URL for the authorization server | 
**logo** | **str** | Image URL for the authorization server | [optional] 
**name** | **str** | Display name of the authorization server | 
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the authorization server | 
**links** | [**CustomAuthorizationServerLinks**](CustomAuthorizationServerLinks.md) |  | 

## Example

```python
from okta.models.custom_authorization_server import CustomAuthorizationServer

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAuthorizationServer from a JSON string
custom_authorization_server_instance = CustomAuthorizationServer.from_json(json)
# print the JSON string representation of the object
print(CustomAuthorizationServer.to_json())

# convert the object into a dict
custom_authorization_server_dict = custom_authorization_server_instance.to_dict()
# create an instance of CustomAuthorizationServer from a dict
custom_authorization_server_from_dict = CustomAuthorizationServer.from_dict(custom_authorization_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


