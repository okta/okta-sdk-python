# UserFactorTokenHOTPProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_secret** | **str** | Unique secret key used to generate the OTP | [optional] 

## Example

```python
from okta.models.user_factor_token_hotp_profile import UserFactorTokenHOTPProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenHOTPProfile from a JSON string
user_factor_token_hotp_profile_instance = UserFactorTokenHOTPProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenHOTPProfile.to_json())

# convert the object into a dict
user_factor_token_hotp_profile_dict = user_factor_token_hotp_profile_instance.to_dict()
# create an instance of UserFactorTokenHOTPProfile from a dict
user_factor_token_hotp_profile_from_dict = UserFactorTokenHOTPProfile.from_dict(user_factor_token_hotp_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


