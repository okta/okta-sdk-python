# DeviceIntegrationsMetadata

The metadata of the device integration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**service_account_name** | **str** |  | 
**service_account_email** | **str** |  | 
**provider** | **str** |  | 
**enrollment_url** | **str** |  | 
**idp_id** | **str** |  | 

## Example

```python
from okta.models.device_integrations_metadata import DeviceIntegrationsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceIntegrationsMetadata from a JSON string
device_integrations_metadata_instance = DeviceIntegrationsMetadata.from_json(json)
# print the JSON string representation of the object
print(DeviceIntegrationsMetadata.to_json())

# convert the object into a dict
device_integrations_metadata_dict = device_integrations_metadata_instance.to_dict()
# create an instance of DeviceIntegrationsMetadata from a dict
device_integrations_metadata_from_dict = DeviceIntegrationsMetadata.from_dict(device_integrations_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


