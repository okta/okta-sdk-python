# IdentityProviderCredentialsTrust


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**kid** | **str** |  | [optional] 
**revocation** | [**IdentityProviderCredentialsTrustRevocation**](IdentityProviderCredentialsTrustRevocation.md) |  | [optional] 
**revocation_cache_lifetime** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.identity_provider_credentials_trust import IdentityProviderCredentialsTrust

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderCredentialsTrust from a JSON string
identity_provider_credentials_trust_instance = IdentityProviderCredentialsTrust.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderCredentialsTrust.to_json())

# convert the object into a dict
identity_provider_credentials_trust_dict = identity_provider_credentials_trust_instance.to_dict()
# create an instance of IdentityProviderCredentialsTrust from a dict
identity_provider_credentials_trust_form_dict = identity_provider_credentials_trust.from_dict(identity_provider_credentials_trust_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


