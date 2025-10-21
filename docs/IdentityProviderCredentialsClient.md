# IdentityProviderCredentialsClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from okta.models.identity_provider_credentials_client import IdentityProviderCredentialsClient

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderCredentialsClient from a JSON string
identity_provider_credentials_client_instance = IdentityProviderCredentialsClient.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderCredentialsClient.to_json())

# convert the object into a dict
identity_provider_credentials_client_dict = identity_provider_credentials_client_instance.to_dict()
# create an instance of IdentityProviderCredentialsClient from a dict
identity_provider_credentials_client_from_dict = IdentityProviderCredentialsClient.from_dict(identity_provider_credentials_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


