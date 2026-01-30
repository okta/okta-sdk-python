# UserFactorToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorTokenProfile**](UserFactorTokenProfile.md) |  | [optional] 
**verify** | [**UserFactorTokenAllOfVerify**](UserFactorTokenAllOfVerify.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_token import UserFactorToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorToken from a JSON string
user_factor_token_instance = UserFactorToken.from_json(json)
# print the JSON string representation of the object
print(UserFactorToken.to_json())

# convert the object into a dict
user_factor_token_dict = user_factor_token_instance.to_dict()
# create an instance of UserFactorToken from a dict
user_factor_token_from_dict = UserFactorToken.from_dict(user_factor_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


