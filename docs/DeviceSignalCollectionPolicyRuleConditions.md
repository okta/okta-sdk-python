# DeviceSignalCollectionPolicyRuleConditions

<x-lifecycle-container><x-lifecycle class=\"ea\"></x-lifecycle></x-lifecycle-container>Specifies conditions that must be met during policy evaluation to apply the rule. All policy conditions, as well as conditions for at least one rule must be met to apply the settings specified in the policy and the associated rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**PolicyNetworkCondition**](PolicyNetworkCondition.md) |  | [optional] 
**platform** | [**PlatformPolicyRuleCondition**](PlatformPolicyRuleCondition.md) |  | [optional] 

## Example

```python
from okta.models.device_signal_collection_policy_rule_conditions import DeviceSignalCollectionPolicyRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSignalCollectionPolicyRuleConditions from a JSON string
device_signal_collection_policy_rule_conditions_instance = DeviceSignalCollectionPolicyRuleConditions.from_json(json)
# print the JSON string representation of the object
print(DeviceSignalCollectionPolicyRuleConditions.to_json())

# convert the object into a dict
device_signal_collection_policy_rule_conditions_dict = device_signal_collection_policy_rule_conditions_instance.to_dict()
# create an instance of DeviceSignalCollectionPolicyRuleConditions from a dict
device_signal_collection_policy_rule_conditions_from_dict = DeviceSignalCollectionPolicyRuleConditions.from_dict(device_signal_collection_policy_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


