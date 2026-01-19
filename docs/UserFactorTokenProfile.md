# UserFactorTokenProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | ID for the factor credential | [optional] 

## Example

```python
from okta.models.user_factor_token_profile import UserFactorTokenProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenProfile from a JSON string
user_factor_token_profile_instance = UserFactorTokenProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenProfile.to_json())

# convert the object into a dict
user_factor_token_profile_dict = user_factor_token_profile_instance.to_dict()
# create an instance of UserFactorTokenProfile from a dict
user_factor_token_profile_from_dict = UserFactorTokenProfile.from_dict(user_factor_token_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


