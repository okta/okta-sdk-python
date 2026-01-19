# DeviceIntegrationsMetadataOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**service_account_name** | **str** |  | 
**service_account_email** | **str** |  | 

## Example

```python
from okta.models.device_integrations_metadata_one_of import DeviceIntegrationsMetadataOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceIntegrationsMetadataOneOf from a JSON string
device_integrations_metadata_one_of_instance = DeviceIntegrationsMetadataOneOf.from_json(json)
# print the JSON string representation of the object
print(DeviceIntegrationsMetadataOneOf.to_json())

# convert the object into a dict
device_integrations_metadata_one_of_dict = device_integrations_metadata_one_of_instance.to_dict()
# create an instance of DeviceIntegrationsMetadataOneOf from a dict
device_integrations_metadata_one_of_from_dict = DeviceIntegrationsMetadataOneOf.from_dict(device_integrations_metadata_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


