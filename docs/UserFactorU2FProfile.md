# UserFactorU2FProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | ID for the factor credential | [optional] 

## Example

```python
from okta.models.user_factor_u2_f_profile import UserFactorU2FProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorU2FProfile from a JSON string
user_factor_u2_f_profile_instance = UserFactorU2FProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorU2FProfile.to_json())

# convert the object into a dict
user_factor_u2_f_profile_dict = user_factor_u2_f_profile_instance.to_dict()
# create an instance of UserFactorU2FProfile from a dict
user_factor_u2_f_profile_from_dict = UserFactorU2FProfile.from_dict(user_factor_u2_f_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


