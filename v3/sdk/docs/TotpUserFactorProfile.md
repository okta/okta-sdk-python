# TotpUserFactorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.totp_user_factor_profile import TotpUserFactorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TotpUserFactorProfile from a JSON string
totp_user_factor_profile_instance = TotpUserFactorProfile.from_json(json)
# print the JSON string representation of the object
print(TotpUserFactorProfile.to_json())

# convert the object into a dict
totp_user_factor_profile_dict = totp_user_factor_profile_instance.to_dict()
# create an instance of TotpUserFactorProfile from a dict
totp_user_factor_profile_from_dict = TotpUserFactorProfile.from_dict(totp_user_factor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


