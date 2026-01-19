# UserFactorTokenVerifyRSA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pass_code** | **str** | OTP for the current time window | [optional] 

## Example

```python
from okta.models.user_factor_token_verify_rsa import UserFactorTokenVerifyRSA

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenVerifyRSA from a JSON string
user_factor_token_verify_rsa_instance = UserFactorTokenVerifyRSA.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenVerifyRSA.to_json())

# convert the object into a dict
user_factor_token_verify_rsa_dict = user_factor_token_verify_rsa_instance.to_dict()
# create an instance of UserFactorTokenVerifyRSA from a dict
user_factor_token_verify_rsa_from_dict = UserFactorTokenVerifyRSA.from_dict(user_factor_token_verify_rsa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


