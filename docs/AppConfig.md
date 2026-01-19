# AppConfig

Additional app configuration for group push mappings. Currently only required for Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AppConfigType**](AppConfigType.md) |  | [optional] 

## Example

```python
from okta.models.app_config import AppConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AppConfig from a JSON string
app_config_instance = AppConfig.from_json(json)
# print the JSON string representation of the object
print(AppConfig.to_json())

# convert the object into a dict
app_config_dict = app_config_instance.to_dict()
# create an instance of AppConfig from a dict
app_config_from_dict = AppConfig.from_dict(app_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


