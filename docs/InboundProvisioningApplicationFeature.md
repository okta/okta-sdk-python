# InboundProvisioningApplicationFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**CapabilitiesInboundProvisioningObject**](CapabilitiesInboundProvisioningObject.md) |  | [optional] 

## Example

```python
from okta.models.inbound_provisioning_application_feature import InboundProvisioningApplicationFeature

# TODO update the JSON string below
json = "{}"
# create an instance of InboundProvisioningApplicationFeature from a JSON string
inbound_provisioning_application_feature_instance = InboundProvisioningApplicationFeature.from_json(json)
# print the JSON string representation of the object
print(InboundProvisioningApplicationFeature.to_json())

# convert the object into a dict
inbound_provisioning_application_feature_dict = inbound_provisioning_application_feature_instance.to_dict()
# create an instance of InboundProvisioningApplicationFeature from a dict
inbound_provisioning_application_feature_from_dict = InboundProvisioningApplicationFeature.from_dict(inbound_provisioning_application_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


