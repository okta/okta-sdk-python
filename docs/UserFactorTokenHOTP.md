# UserFactorTokenHOTP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_profile_id** | **str** | ID of an existing Custom TOTP factor profile. To create this, see [Custom TOTP factor](https://help.okta.com/okta_help.htm?id&#x3D;ext-mfa-totp). | [optional] 
**profile** | [**UserFactorTokenHOTPProfile**](UserFactorTokenHOTPProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_token_hotp import UserFactorTokenHOTP

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenHOTP from a JSON string
user_factor_token_hotp_instance = UserFactorTokenHOTP.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenHOTP.to_json())

# convert the object into a dict
user_factor_token_hotp_dict = user_factor_token_hotp_instance.to_dict()
# create an instance of UserFactorTokenHOTP from a dict
user_factor_token_hotp_from_dict = UserFactorTokenHOTP.from_dict(user_factor_token_hotp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


