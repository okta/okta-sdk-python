# DeviceSignalCollectionPolicyRuleActions

<x-lifecycle-container><x-lifecycle class=\"ea\"></x-lifecycle></x-lifecycle-container>Specifies actions to be taken, or operations that may be allowed, if the rule conditions are satisfied

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_signal_collection** | [**DeviceSignalCollectionPolicyRuleDeviceSignalCollection**](DeviceSignalCollectionPolicyRuleDeviceSignalCollection.md) |  | [optional] 

## Example

```python
from okta.models.device_signal_collection_policy_rule_actions import DeviceSignalCollectionPolicyRuleActions

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSignalCollectionPolicyRuleActions from a JSON string
device_signal_collection_policy_rule_actions_instance = DeviceSignalCollectionPolicyRuleActions.from_json(json)
# print the JSON string representation of the object
print(DeviceSignalCollectionPolicyRuleActions.to_json())

# convert the object into a dict
device_signal_collection_policy_rule_actions_dict = device_signal_collection_policy_rule_actions_instance.to_dict()
# create an instance of DeviceSignalCollectionPolicyRuleActions from a dict
device_signal_collection_policy_rule_actions_from_dict = DeviceSignalCollectionPolicyRuleActions.from_dict(device_signal_collection_policy_rule_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


