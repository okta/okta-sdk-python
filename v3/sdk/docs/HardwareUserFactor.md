# HardwareUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**HardwareUserFactorProfile**](HardwareUserFactorProfile.md) |  | [optional] 

## Example

```python
from okta.models.hardware_user_factor import HardwareUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of HardwareUserFactor from a JSON string
hardware_user_factor_instance = HardwareUserFactor.from_json(json)
# print the JSON string representation of the object
print(HardwareUserFactor.to_json())

# convert the object into a dict
hardware_user_factor_dict = hardware_user_factor_instance.to_dict()
# create an instance of HardwareUserFactor from a dict
hardware_user_factor_from_dict = HardwareUserFactor.from_dict(hardware_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


