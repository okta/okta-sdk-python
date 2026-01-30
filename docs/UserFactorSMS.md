# UserFactorSMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorSMSProfile**](UserFactorSMSProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_sms import UserFactorSMS

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorSMS from a JSON string
user_factor_sms_instance = UserFactorSMS.from_json(json)
# print the JSON string representation of the object
print(UserFactorSMS.to_json())

# convert the object into a dict
user_factor_sms_dict = user_factor_sms_instance.to_dict()
# create an instance of UserFactorSMS from a dict
user_factor_sms_from_dict = UserFactorSMS.from_dict(user_factor_sms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


