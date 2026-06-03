# UserFactorSignedNonceProfileKey

JSON Web Key (JWK) for signed nonce verification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Key type | [optional] 
**use** | **str** | Key usage | [optional] 
**kid** | **str** | Key ID | [optional] 
**jwk_type** | **str** | Purpose of the key | [optional] 
**e** | **str** | RSA public exponent (present only for RSA keys) | [optional] 
**n** | **str** | RSA modulus (present only for RSA keys) | [optional] 
**crv** | **str** | EC curve name (present only for EC keys) | [optional] 
**x** | **str** | EC x-coordinate (present only for EC keys) | [optional] 
**y** | **str** | EC y-coordinate (present only for EC keys) | [optional] 
**x5c** | **List[str]** | X.509 certificate chain | [optional] 

## Example

```python
from okta.models.user_factor_signed_nonce_profile_key import UserFactorSignedNonceProfileKey

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorSignedNonceProfileKey from a JSON string
user_factor_signed_nonce_profile_key_instance = UserFactorSignedNonceProfileKey.from_json(json)
# print the JSON string representation of the object
print(UserFactorSignedNonceProfileKey.to_json())

# convert the object into a dict
user_factor_signed_nonce_profile_key_dict = user_factor_signed_nonce_profile_key_instance.to_dict()
# create an instance of UserFactorSignedNonceProfileKey from a dict
user_factor_signed_nonce_profile_key_from_dict = UserFactorSignedNonceProfileKey.from_dict(user_factor_signed_nonce_profile_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


