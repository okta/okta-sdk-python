# AuthenticatorProfile

Defines the authenticator specific parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | The phone number for a &#x60;call&#x60; or &#x60;sms&#x60; authenticator enrollment. | 

## Example

```python
from okta.models.authenticator_profile import AuthenticatorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorProfile from a JSON string
authenticator_profile_instance = AuthenticatorProfile.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorProfile.to_json())

# convert the object into a dict
authenticator_profile_dict = authenticator_profile_instance.to_dict()
# create an instance of AuthenticatorProfile from a dict
authenticator_profile_from_dict = AuthenticatorProfile.from_dict(authenticator_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


