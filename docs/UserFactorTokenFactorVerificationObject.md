# UserFactorTokenFactorVerificationObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_pass_code** | **str** | OTP for the next time window | [optional] 
**pass_code** | **str** | OTP for the current time window | [optional] 

## Example

```python
from okta.models.user_factor_token_factor_verification_object import UserFactorTokenFactorVerificationObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenFactorVerificationObject from a JSON string
user_factor_token_factor_verification_object_instance = UserFactorTokenFactorVerificationObject.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenFactorVerificationObject.to_json())

# convert the object into a dict
user_factor_token_factor_verification_object_dict = user_factor_token_factor_verification_object_instance.to_dict()
# create an instance of UserFactorTokenFactorVerificationObject from a dict
user_factor_token_factor_verification_object_from_dict = UserFactorTokenFactorVerificationObject.from_dict(user_factor_token_factor_verification_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


