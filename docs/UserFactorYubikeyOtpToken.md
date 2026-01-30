# UserFactorYubikeyOtpToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the token was created | [optional] [readonly] 
**id** | **str** | ID of the token | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the token was last updated | [optional] [readonly] 
**last_verified** | **datetime** | Timestamp when the token was last verified | [optional] [readonly] 
**profile** | **Dict[str, object]** | Specified profile information for token | [optional] 
**status** | **str** | Token status | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] 
**links** | [**UserFactorLinks**](UserFactorLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_yubikey_otp_token import UserFactorYubikeyOtpToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorYubikeyOtpToken from a JSON string
user_factor_yubikey_otp_token_instance = UserFactorYubikeyOtpToken.from_json(json)
# print the JSON string representation of the object
print(UserFactorYubikeyOtpToken.to_json())

# convert the object into a dict
user_factor_yubikey_otp_token_dict = user_factor_yubikey_otp_token_instance.to_dict()
# create an instance of UserFactorYubikeyOtpToken from a dict
user_factor_yubikey_otp_token_from_dict = UserFactorYubikeyOtpToken.from_dict(user_factor_yubikey_otp_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


