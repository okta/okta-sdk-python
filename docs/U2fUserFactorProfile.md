# U2fUserFactorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** |  | [optional] 

## Example

```python
from okta.models.u2f_user_factor_profile import U2fUserFactorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of U2fUserFactorProfile from a JSON string
u2f_user_factor_profile_instance = U2fUserFactorProfile.from_json(json)
# print the JSON string representation of the object
print(U2fUserFactorProfile.to_json())

# convert the object into a dict
u2f_user_factor_profile_dict = u2f_user_factor_profile_instance.to_dict()
# create an instance of U2fUserFactorProfile from a dict
u2f_user_factor_profile_from_dict = U2fUserFactorProfile.from_dict(u2f_user_factor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


