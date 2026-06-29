# UserFactorSignedNonceProfile

Profile for the Okta FastPass (signed nonce) factor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | ID for the factor credential | [optional] 
**device_type** | **str** | Type of device | [optional] 
**name** | **str** | Name of the device | [optional] 
**platform** | **str** | OS platform of the associated device | [optional] 
**version** | **str** | OS version of the associated device | [optional] 
**keys** | [**List[UserFactorSignedNonceProfileKey]**](UserFactorSignedNonceProfileKey.md) | Cryptographic keys associated with the signed nonce factor | [optional] 

## Example

```python
from okta.models.user_factor_signed_nonce_profile import UserFactorSignedNonceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorSignedNonceProfile from a JSON string
user_factor_signed_nonce_profile_instance = UserFactorSignedNonceProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorSignedNonceProfile.to_json())

# convert the object into a dict
user_factor_signed_nonce_profile_dict = user_factor_signed_nonce_profile_instance.to_dict()
# create an instance of UserFactorSignedNonceProfile from a dict
user_factor_signed_nonce_profile_from_dict = UserFactorSignedNonceProfile.from_dict(user_factor_signed_nonce_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


