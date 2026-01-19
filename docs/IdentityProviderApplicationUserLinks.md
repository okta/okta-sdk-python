# IdentityProviderApplicationUserLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**next** | [**HrefObjectNextLink**](HrefObjectNextLink.md) |  | [optional] 
**idp** | [**HrefObject**](HrefObject.md) | The IdP instance | [optional] 
**user** | [**HrefObject**](HrefObject.md) | The linked Okta user | [optional] 

## Example

```python
from okta.models.identity_provider_application_user_links import IdentityProviderApplicationUserLinks

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderApplicationUserLinks from a JSON string
identity_provider_application_user_links_instance = IdentityProviderApplicationUserLinks.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderApplicationUserLinks.to_json())

# convert the object into a dict
identity_provider_application_user_links_dict = identity_provider_application_user_links_instance.to_dict()
# create an instance of IdentityProviderApplicationUserLinks from a dict
identity_provider_application_user_links_from_dict = IdentityProviderApplicationUserLinks.from_dict(identity_provider_application_user_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


