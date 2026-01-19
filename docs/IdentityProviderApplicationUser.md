# IdentityProviderApplicationUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**external_id** | **str** | Unique IdP-specific identifier for the user | [optional] [readonly] 
**id** | **str** | Unique key of the user | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**profile** | **Dict[str, object]** | IdP-specific profile for the user.  IdP user profiles are IdP-specific but may be customized by the Profile Editor in the Admin Console.  &gt; **Note:** Okta variable names have reserved characters that may conflict with the name of an IdP assertion attribute. You can use the **External name** to define the attribute name as defined in an IdP assertion such as a SAML attribute name. | [optional] 
**embedded** | **Dict[str, object]** | Embedded resources related to the IdP user | [optional] [readonly] 
**links** | [**IdentityProviderApplicationUserLinks**](IdentityProviderApplicationUserLinks.md) |  | [optional] 

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


