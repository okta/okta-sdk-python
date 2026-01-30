# UserFactorTokenHardware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorTokenProfile**](UserFactorTokenProfile.md) |  | [optional] 
**verify** | [**UserFactorTokenHardwareAllOfVerify**](UserFactorTokenHardwareAllOfVerify.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_token_hardware import UserFactorTokenHardware

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorTokenHardware from a JSON string
user_factor_token_hardware_instance = UserFactorTokenHardware.from_json(json)
# print the JSON string representation of the object
print(UserFactorTokenHardware.to_json())

# convert the object into a dict
user_factor_token_hardware_dict = user_factor_token_hardware_instance.to_dict()
# create an instance of UserFactorTokenHardware from a dict
user_factor_token_hardware_from_dict = UserFactorTokenHardware.from_dict(user_factor_token_hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


