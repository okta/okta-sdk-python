# SmsUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**SmsUserFactorProfile**](SmsUserFactorProfile.md) |  | [optional] 

## Example

```python
from okta.models.sms_user_factor import SmsUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of SmsUserFactor from a JSON string
sms_user_factor_instance = SmsUserFactor.from_json(json)
# print the JSON string representation of the object
print(SmsUserFactor.to_json())

# convert the object into a dict
sms_user_factor_dict = sms_user_factor_instance.to_dict()
# create an instance of SmsUserFactor from a dict
sms_user_factor_from_dict = SmsUserFactor.from_dict(sms_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


