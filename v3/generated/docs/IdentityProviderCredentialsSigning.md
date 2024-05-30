# IdentityProviderCredentialsSigning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.identity_provider_credentials_signing import IdentityProviderCredentialsSigning

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderCredentialsSigning from a JSON string
identity_provider_credentials_signing_instance = IdentityProviderCredentialsSigning.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderCredentialsSigning.to_json())

# convert the object into a dict
identity_provider_credentials_signing_dict = identity_provider_credentials_signing_instance.to_dict()
# create an instance of IdentityProviderCredentialsSigning from a dict
identity_provider_credentials_signing_form_dict = identity_provider_credentials_signing.from_dict(identity_provider_credentials_signing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


