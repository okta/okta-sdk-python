# UserFactorWebProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | ID for the factor credential | [optional] 

## Example

```python
from okta.models.user_factor_web_profile import UserFactorWebProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorWebProfile from a JSON string
user_factor_web_profile_instance = UserFactorWebProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorWebProfile.to_json())

# convert the object into a dict
user_factor_web_profile_dict = user_factor_web_profile_instance.to_dict()
# create an instance of UserFactorWebProfile from a dict
user_factor_web_profile_from_dict = UserFactorWebProfile.from_dict(user_factor_web_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


