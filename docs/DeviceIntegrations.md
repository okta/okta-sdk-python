# DeviceIntegrations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the device integration | [optional] 
**id** | **str** | The ID of the device integration | [optional] [readonly] 
**metadata** | [**DeviceIntegrationsMetadata**](DeviceIntegrationsMetadata.md) |  | [optional] 
**name** | [**DeviceIntegrationsName**](DeviceIntegrationsName.md) |  | [optional] 
**platform** | [**DeviceIntegrationsPlatform**](DeviceIntegrationsPlatform.md) |  | [optional] 
**status** | [**DeviceIntegrationsStatus**](DeviceIntegrationsStatus.md) |  | [optional] 
**links** | [**LinksSelfAndLifecycle**](LinksSelfAndLifecycle.md) |  | [optional] 

## Example

```python
from okta.models.device_integrations import DeviceIntegrations

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceIntegrations from a JSON string
device_integrations_instance = DeviceIntegrations.from_json(json)
# print the JSON string representation of the object
print(DeviceIntegrations.to_json())

# convert the object into a dict
device_integrations_dict = device_integrations_instance.to_dict()
# create an instance of DeviceIntegrations from a dict
device_integrations_from_dict = DeviceIntegrations.from_dict(device_integrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


