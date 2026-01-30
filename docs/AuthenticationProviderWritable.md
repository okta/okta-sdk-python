# AuthenticationProviderWritable

Specifies the authentication provider that validates the user password credential. The user's current provider is managed by the **Delegated Authentication** settings in your org. See [Create user with authentication provider](/openapi/okta-management/management/tag/User/#create-user-with-authentication-provider).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the authentication provider | [optional] 
**type** | [**AuthenticationProviderTypeWritable**](AuthenticationProviderTypeWritable.md) |  | [optional] 

## Example

```python
from okta.models.authentication_provider_writable import AuthenticationProviderWritable

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProviderWritable from a JSON string
authentication_provider_writable_instance = AuthenticationProviderWritable.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProviderWritable.to_json())

# convert the object into a dict
authentication_provider_writable_dict = authentication_provider_writable_instance.to_dict()
# create an instance of AuthenticationProviderWritable from a dict
authentication_provider_writable_from_dict = AuthenticationProviderWritable.from_dict(authentication_provider_writable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


