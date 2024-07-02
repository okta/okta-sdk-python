# AuthenticationProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**AuthenticationProviderType**](AuthenticationProviderType.md) |  | [optional] 

## Example

```python
from openapi_client.models.authentication_provider import AuthenticationProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProvider from a JSON string
authentication_provider_instance = AuthenticationProvider.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProvider.to_json())

# convert the object into a dict
authentication_provider_dict = authentication_provider_instance.to_dict()
# create an instance of AuthenticationProvider from a dict
authentication_provider_from_dict = AuthenticationProvider.from_dict(authentication_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


