# AuthenticatorProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**AuthenticatorProviderConfiguration**](AuthenticatorProviderConfiguration.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_provider import AuthenticatorProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorProvider from a JSON string
authenticator_provider_instance = AuthenticatorProvider.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorProvider.to_json())

# convert the object into a dict
authenticator_provider_dict = authenticator_provider_instance.to_dict()
# create an instance of AuthenticatorProvider from a dict
authenticator_provider_from_dict = AuthenticatorProvider.from_dict(authenticator_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


