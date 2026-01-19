# UserFactorTokenVerifySymantec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_pass_code** | **int** | OTP for the next time window | [optional] 
**pass_code** | **str** | OTP for the current time window | [optional] 

## Example

```python
from okta.models.user_factor_token_verify_symantec import UserFactorTokenVerifySymantec

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenVerifySymantec from a JSON string
user_factor_token_verify_symantec_instance = UserFactorTokenVerifySymantec.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenVerifySymantec.to_json())

# convert the object into a dict
user_factor_token_verify_symantec_dict = user_factor_token_verify_symantec_instance.to_dict()
# create an instance of UserFactorTokenVerifySymantec from a dict
user_factor_token_verify_symantec_from_dict = UserFactorTokenVerifySymantec.from_dict(user_factor_token_verify_symantec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


