# UserFactorCallProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_extension** | **str** | Extension of the associated &#x60;phoneNumber&#x60; | [optional] 
**phone_number** | **str** | Phone number of the factor. Format phone numbers to use the [E.164 standard](https://www.itu.int/rec/T-REC-E.164/). | [optional] 

## Example

```python
from okta.models.user_factor_call_profile import UserFactorCallProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorCallProfile from a JSON string
user_factor_call_profile_instance = UserFactorCallProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorCallProfile.to_json())

# convert the object into a dict
user_factor_call_profile_dict = user_factor_call_profile_instance.to_dict()
# create an instance of UserFactorCallProfile from a dict
user_factor_call_profile_from_dict = UserFactorCallProfile.from_dict(user_factor_call_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


