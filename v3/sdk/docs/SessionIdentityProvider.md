# SessionIdentityProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identity Provider ID. If the &#x60;type&#x60; is &#x60;OKTA&#x60;, then the &#x60;id&#x60; is the org ID. | [optional] [readonly] 
**type** | [**SessionIdentityProviderType**](SessionIdentityProviderType.md) |  | [optional] 

## Example

```python
from okta.models.session_identity_provider import SessionIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SessionIdentityProvider from a JSON string
session_identity_provider_instance = SessionIdentityProvider.from_json(json)
# print the JSON string representation of the object
print(SessionIdentityProvider.to_json())

# convert the object into a dict
session_identity_provider_dict = session_identity_provider_instance.to_dict()
# create an instance of SessionIdentityProvider from a dict
session_identity_provider_from_dict = SessionIdentityProvider.from_dict(session_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


