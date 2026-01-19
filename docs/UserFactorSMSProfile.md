# UserFactorSMSProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number of the factor. You should format phone numbers to use the [E.164 standard](https://www.itu.int/rec/T-REC-E.164/). | [optional] 

## Example

```python
from okta.models.user_factor_sms_profile import UserFactorSMSProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorSMSProfile from a JSON string
user_factor_sms_profile_instance = UserFactorSMSProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorSMSProfile.to_json())

# convert the object into a dict
user_factor_sms_profile_dict = user_factor_sms_profile_instance.to_dict()
# create an instance of UserFactorSMSProfile from a dict
user_factor_sms_profile_from_dict = UserFactorSMSProfile.from_dict(user_factor_sms_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


