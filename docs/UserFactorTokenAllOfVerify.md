# UserFactorTokenAllOfVerify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pass_code** | **str** | OTP for the current time window | [optional] 
**next_pass_code** | **int** | OTP for the next time window | [optional] 

## Example

```python
from okta.models.user_factor_token_all_of_verify import UserFactorTokenAllOfVerify

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenAllOfVerify from a JSON string
user_factor_token_all_of_verify_instance = UserFactorTokenAllOfVerify.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenAllOfVerify.to_json())

# convert the object into a dict
user_factor_token_all_of_verify_dict = user_factor_token_all_of_verify_instance.to_dict()
# create an instance of UserFactorTokenAllOfVerify from a dict
user_factor_token_all_of_verify_from_dict = UserFactorTokenAllOfVerify.from_dict(user_factor_token_all_of_verify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


