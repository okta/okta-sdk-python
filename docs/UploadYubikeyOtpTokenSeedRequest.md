# UploadYubikeyOtpTokenSeedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_number** | **str** | The unique identifier assigned to each YubiKey device | [optional] 
**public_id** | **str** | The YubiKey&#39;s public ID | [optional] 
**private_id** | **str** | The YubiKey&#39;s private ID | [optional] 
**aes_key** | **str** | The cryptographic key used in the AES (Advanced Encryption Standard) algorithm to encrypt and decrypt the YubiKey OTP | [optional] 

## Example

```python
from okta.models.upload_yubikey_otp_token_seed_request import UploadYubikeyOtpTokenSeedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadYubikeyOtpTokenSeedRequest from a JSON string
upload_yubikey_otp_token_seed_request_instance = UploadYubikeyOtpTokenSeedRequest.from_json(json)
# print the JSON string representation of the object
print(UploadYubikeyOtpTokenSeedRequest.to_json())

# convert the object into a dict
upload_yubikey_otp_token_seed_request_dict = upload_yubikey_otp_token_seed_request_instance.to_dict()
# create an instance of UploadYubikeyOtpTokenSeedRequest from a dict
upload_yubikey_otp_token_seed_request_from_dict = UploadYubikeyOtpTokenSeedRequest.from_dict(upload_yubikey_otp_token_seed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


