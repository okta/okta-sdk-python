# TenantSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_properties** | [**List[AppInstanceProperty]**](AppInstanceProperty.md) |  | [optional] 

## Example

```python
from okta.models.tenant_settings import TenantSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantSettings from a JSON string
tenant_settings_instance = TenantSettings.from_json(json)
# print the JSON string representation of the object
print(TenantSettings.to_json())

# convert the object into a dict
tenant_settings_dict = tenant_settings_instance.to_dict()
# create an instance of TenantSettings from a dict
tenant_settings_from_dict = TenantSettings.from_dict(tenant_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


