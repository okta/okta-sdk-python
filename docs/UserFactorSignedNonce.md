# UserFactorSignedNonce

`signed_nonce` is the factor type for [Okta FastPass](https://help.okta.com/oie/en-us/content/topics/identity-engine/devices/fp/fp-main.htm). You can't use the Factors API to enroll or activate Okta FastPass (`signed_nonce`) for a user. Use the [Okta Verify](https://help.okta.com/en-us/content/topics/mobile/okta-verify-overview.htm) authenticator enrollment flow instead.  You can use the Factors API to list and delete `signed_nonce` factors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_type** | **object** |  | [optional] 
**profile** | [**UserFactorSignedNonceProfile**](UserFactorSignedNonceProfile.md) |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from okta.models.user_factor_signed_nonce import UserFactorSignedNonce

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorSignedNonce from a JSON string
user_factor_signed_nonce_instance = UserFactorSignedNonce.from_json(json)
# print the JSON string representation of the object
print(UserFactorSignedNonce.to_json())

# convert the object into a dict
user_factor_signed_nonce_dict = user_factor_signed_nonce_instance.to_dict()
# create an instance of UserFactorSignedNonce from a dict
user_factor_signed_nonce_from_dict = UserFactorSignedNonce.from_dict(user_factor_signed_nonce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


