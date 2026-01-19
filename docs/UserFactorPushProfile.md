# UserFactorPushProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | ID for the factor credential | [optional] 
**device_token** | **str** | Token used to identify the device | [optional] 
**device_type** | **str** | Type of device | [optional] 
**name** | **str** | Name of the device | [optional] 
**platform** | **str** | OS version of the associated device | [optional] 
**version** | **str** | Installed version of Okta Verify | [optional] 

## Example

```python
from okta.models.user_factor_push_profile import UserFactorPushProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorPushProfile from a JSON string
user_factor_push_profile_instance = UserFactorPushProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorPushProfile.to_json())

# convert the object into a dict
user_factor_push_profile_dict = user_factor_push_profile_instance.to_dict()
# create an instance of UserFactorPushProfile from a dict
user_factor_push_profile_from_dict = UserFactorPushProfile.from_dict(user_factor_push_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


