# UserFactorTokenSoftwareTOTP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorTokenProfile**](UserFactorTokenProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_token_software_totp import UserFactorTokenSoftwareTOTP

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenSoftwareTOTP from a JSON string
user_factor_token_software_totp_instance = UserFactorTokenSoftwareTOTP.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenSoftwareTOTP.to_json())

# convert the object into a dict
user_factor_token_software_totp_dict = user_factor_token_software_totp_instance.to_dict()
# create an instance of UserFactorTokenSoftwareTOTP from a dict
user_factor_token_software_totp_from_dict = UserFactorTokenSoftwareTOTP.from_dict(user_factor_token_software_totp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


