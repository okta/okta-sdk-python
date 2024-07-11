# IdentityProviderApplicationUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **str** |  | [optional] 
**profile** | **Dict[str, object]** |  | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.identity_provider_application_user import IdentityProviderApplicationUser

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderApplicationUser from a JSON string
identity_provider_application_user_instance = IdentityProviderApplicationUser.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderApplicationUser.to_json())

# convert the object into a dict
identity_provider_application_user_dict = identity_provider_application_user_instance.to_dict()
# create an instance of IdentityProviderApplicationUser from a dict
identity_provider_application_user_from_dict = IdentityProviderApplicationUser.from_dict(identity_provider_application_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


