# AuthenticatorMethodOtp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptable_adjacent_intervals** | **int** |  | [optional] 
**algorithm** | [**OtpTotpAlgorithm**](OtpTotpAlgorithm.md) |  | [optional] 
**encoding** | [**OtpTotpEncoding**](OtpTotpEncoding.md) |  | [optional] 
**factor_profile_id** | **str** |  | [optional] 
**pass_code_length** | **int** |  | [optional] 
**protocol** | [**OtpProtocol**](OtpProtocol.md) |  | [optional] 
**time_interval_in_seconds** | **int** |  | [optional] 

## Example

```python
from okta.models.authenticator_method_otp import AuthenticatorMethodOtp

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodOtp from a JSON string
authenticator_method_otp_instance = AuthenticatorMethodOtp.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodOtp.to_json())

# convert the object into a dict
authenticator_method_otp_dict = authenticator_method_otp_instance.to_dict()
# create an instance of AuthenticatorMethodOtp from a dict
authenticator_method_otp_from_dict = AuthenticatorMethodOtp.from_dict(authenticator_method_otp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


