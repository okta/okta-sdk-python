# CustomHotpUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_profile_id** | **str** |  | [optional] 
**profile** | [**CustomHotpUserFactorProfile**](CustomHotpUserFactorProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.custom_hotp_user_factor import CustomHotpUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of CustomHotpUserFactor from a JSON string
custom_hotp_user_factor_instance = CustomHotpUserFactor.from_json(json)
# print the JSON string representation of the object
print(CustomHotpUserFactor.to_json())

# convert the object into a dict
custom_hotp_user_factor_dict = custom_hotp_user_factor_instance.to_dict()
# create an instance of CustomHotpUserFactor from a dict
custom_hotp_user_factor_from_dict = CustomHotpUserFactor.from_dict(custom_hotp_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


