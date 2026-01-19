# AuthenticatorMethodTotpAllOfSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_interval_in_seconds** | **int** | Time interval for TOTP in seconds | [optional] 
**encoding** | [**OtpTotpEncoding**](OtpTotpEncoding.md) |  | [optional] 
**algorithm** | [**OtpTotpAlgorithm**](OtpTotpAlgorithm.md) |  | [optional] 
**pass_code_length** | **int** | Number of digits in an OTP value | [optional] 

## Example

```python
from okta.models.authenticator_method_totp_all_of_settings import AuthenticatorMethodTotpAllOfSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodTotpAllOfSettings from a JSON string
authenticator_method_totp_all_of_settings_instance = AuthenticatorMethodTotpAllOfSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodTotpAllOfSettings.to_json())

# convert the object into a dict
authenticator_method_totp_all_of_settings_dict = authenticator_method_totp_all_of_settings_instance.to_dict()
# create an instance of AuthenticatorMethodTotpAllOfSettings from a dict
authenticator_method_totp_all_of_settings_from_dict = AuthenticatorMethodTotpAllOfSettings.from_dict(authenticator_method_totp_all_of_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


