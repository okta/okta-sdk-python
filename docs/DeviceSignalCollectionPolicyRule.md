# DeviceSignalCollectionPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**DeviceSignalCollectionPolicyRuleActions**](DeviceSignalCollectionPolicyRuleActions.md) |  | [optional] 
**conditions** | [**DeviceSignalCollectionPolicyRuleConditions**](DeviceSignalCollectionPolicyRuleConditions.md) |  | [optional] 

## Example

```python
from okta.models.device_signal_collection_policy_rule import DeviceSignalCollectionPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSignalCollectionPolicyRule from a JSON string
device_signal_collection_policy_rule_instance = DeviceSignalCollectionPolicyRule.from_json(json)
# print the JSON string representation of the object
print(DeviceSignalCollectionPolicyRule.to_json())

# convert the object into a dict
device_signal_collection_policy_rule_dict = device_signal_collection_policy_rule_instance.to_dict()
# create an instance of DeviceSignalCollectionPolicyRule from a dict
device_signal_collection_policy_rule_from_dict = DeviceSignalCollectionPolicyRule.from_dict(device_signal_collection_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


