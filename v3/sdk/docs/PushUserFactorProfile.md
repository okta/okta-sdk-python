# PushUserFactorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** |  | [optional] 
**device_token** | **str** |  | [optional] 
**device_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from okta.models.push_user_factor_profile import PushUserFactorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PushUserFactorProfile from a JSON string
push_user_factor_profile_instance = PushUserFactorProfile.from_json(json)
# print the JSON string representation of the object
print(PushUserFactorProfile.to_json())

# convert the object into a dict
push_user_factor_profile_dict = push_user_factor_profile_instance.to_dict()
# create an instance of PushUserFactorProfile from a dict
push_user_factor_profile_from_dict = PushUserFactorProfile.from_dict(push_user_factor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


