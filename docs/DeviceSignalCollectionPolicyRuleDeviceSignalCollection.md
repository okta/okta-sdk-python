# DeviceSignalCollectionPolicyRuleDeviceSignalCollection

Specifies how device context is collected when a user attempts to sign in

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_context_providers** | [**List[DeviceContextProvider]**](DeviceContextProvider.md) | Contains the device context provider configuration | [optional] 

## Example

```python
from okta.models.device_signal_collection_policy_rule_device_signal_collection import DeviceSignalCollectionPolicyRuleDeviceSignalCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSignalCollectionPolicyRuleDeviceSignalCollection from a JSON string
device_signal_collection_policy_rule_device_signal_collection_instance = DeviceSignalCollectionPolicyRuleDeviceSignalCollection.from_json(json)
# print the JSON string representation of the object
print(DeviceSignalCollectionPolicyRuleDeviceSignalCollection.to_json())

# convert the object into a dict
device_signal_collection_policy_rule_device_signal_collection_dict = device_signal_collection_policy_rule_device_signal_collection_instance.to_dict()
# create an instance of DeviceSignalCollectionPolicyRuleDeviceSignalCollection from a dict
device_signal_collection_policy_rule_device_signal_collection_from_dict = DeviceSignalCollectionPolicyRuleDeviceSignalCollection.from_dict(device_signal_collection_policy_rule_device_signal_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


