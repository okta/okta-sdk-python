# CustomAuthSettings

Set of AIPs used for authType `CUSTOM`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_properties** | [**List[AppInstanceProperty]**](AppInstanceProperty.md) |  | [optional] 

## Example

```python
from okta.models.custom_auth_settings import CustomAuthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAuthSettings from a JSON string
custom_auth_settings_instance = CustomAuthSettings.from_json(json)
# print the JSON string representation of the object
print(CustomAuthSettings.to_json())

# convert the object into a dict
custom_auth_settings_dict = custom_auth_settings_instance.to_dict()
# create an instance of CustomAuthSettings from a dict
custom_auth_settings_from_dict = CustomAuthSettings.from_dict(custom_auth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


