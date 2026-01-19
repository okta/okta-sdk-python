# AuthenticatorMethodOtp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptable_adjacent_intervals** | **int** | The number of acceptable adjacent intervals, also known as the clock drift interval. This setting allows you to build in tolerance for any time difference between the token and the server. For example, with a &#x60;timeIntervalInSeconds&#x60; of 60 seconds and an &#x60;acceptableAdjacentIntervals&#x60; value of 5, Okta accepts passcodes within 300 seconds (60 * 5) before or after the end user enters their code. | [optional] 
**algorithm** | [**OtpTotpAlgorithm**](OtpTotpAlgorithm.md) |  | [optional] 
**encoding** | [**OtpTotpEncoding**](OtpTotpEncoding.md) |  | [optional] 
**factor_profile_id** | **str** | The &#x60;id&#x60; value of the factor profile | [optional] 
**pass_code_length** | **int** | Number of digits in an OTP value | [optional] 
**protocol** | [**OtpProtocol**](OtpProtocol.md) |  | [optional] 
**time_interval_in_seconds** | **int** | Time interval for TOTP in seconds | [optional] 

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


