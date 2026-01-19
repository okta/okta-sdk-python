# CapabilitiesInboundProvisioningObject

Defines the configuration for the INBOUND_PROVISIONING feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_rules** | [**CapabilitiesImportRulesObject**](CapabilitiesImportRulesObject.md) |  | 
**import_settings** | [**CapabilitiesImportSettingsObject**](CapabilitiesImportSettingsObject.md) |  | 

## Example

```python
from okta.models.capabilities_inbound_provisioning_object import CapabilitiesInboundProvisioningObject

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesInboundProvisioningObject from a JSON string
capabilities_inbound_provisioning_object_instance = CapabilitiesInboundProvisioningObject.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesInboundProvisioningObject.to_json())

# convert the object into a dict
capabilities_inbound_provisioning_object_dict = capabilities_inbound_provisioning_object_instance.to_dict()
# create an instance of CapabilitiesInboundProvisioningObject from a dict
capabilities_inbound_provisioning_object_from_dict = CapabilitiesInboundProvisioningObject.from_dict(capabilities_inbound_provisioning_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


