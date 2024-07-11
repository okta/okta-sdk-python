# CustomHotpUserFactorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.custom_hotp_user_factor_profile import CustomHotpUserFactorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CustomHotpUserFactorProfile from a JSON string
custom_hotp_user_factor_profile_instance = CustomHotpUserFactorProfile.from_json(json)
# print the JSON string representation of the object
print(CustomHotpUserFactorProfile.to_json())

# convert the object into a dict
custom_hotp_user_factor_profile_dict = custom_hotp_user_factor_profile_instance.to_dict()
# create an instance of CustomHotpUserFactorProfile from a dict
custom_hotp_user_factor_profile_from_dict = CustomHotpUserFactorProfile.from_dict(custom_hotp_user_factor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


