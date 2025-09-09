# IdentityProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**issuer_mode** | [**IssuerMode**](IssuerMode.md) |  | [optional] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**policy** | [**IdentityProviderPolicy**](IdentityProviderPolicy.md) |  | [optional] 
**properties** | [**IdentityProviderProperties**](IdentityProviderProperties.md) |  | [optional] 
**protocol** | [**Protocol**](Protocol.md) |  | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**IdentityProviderType**](IdentityProviderType.md) |  | [optional] 
**links** | [**IdentityProviderLinks**](IdentityProviderLinks.md) |  | [optional] 

## Example

```python
from okta.models.identity_provider import IdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProvider from a JSON string
identity_provider_instance = IdentityProvider.from_json(json)
# print the JSON string representation of the object
print(IdentityProvider.to_json())

# convert the object into a dict
identity_provider_dict = identity_provider_instance.to_dict()
# create an instance of IdentityProvider from a dict
identity_provider_from_dict = IdentityProvider.from_dict(identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


