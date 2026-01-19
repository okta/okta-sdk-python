# UserIdentityProviderLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | Unique IdP-specific identifier for a user | [optional] 

## Example

```python
from okta.models.user_identity_provider_link_request import UserIdentityProviderLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentityProviderLinkRequest from a JSON string
user_identity_provider_link_request_instance = UserIdentityProviderLinkRequest.from_json(json)
# print the JSON string representation of the object
print(UserIdentityProviderLinkRequest.to_json())

# convert the object into a dict
user_identity_provider_link_request_dict = user_identity_provider_link_request_instance.to_dict()
# create an instance of UserIdentityProviderLinkRequest from a dict
user_identity_provider_link_request_from_dict = UserIdentityProviderLinkRequest.from_dict(user_identity_provider_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


