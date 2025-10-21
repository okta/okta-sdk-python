# BehaviorRuleAnomalousDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**BehaviorRuleSettingsAnomalousDevice**](BehaviorRuleSettingsAnomalousDevice.md) |  | [optional] 

## Example

```python
from okta.models.behavior_rule_anomalous_device import BehaviorRuleAnomalousDevice

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorRuleAnomalousDevice from a JSON string
behavior_rule_anomalous_device_instance = BehaviorRuleAnomalousDevice.from_json(json)
# print the JSON string representation of the object
print(BehaviorRuleAnomalousDevice.to_json())

# convert the object into a dict
behavior_rule_anomalous_device_dict = behavior_rule_anomalous_device_instance.to_dict()
# create an instance of BehaviorRuleAnomalousDevice from a dict
behavior_rule_anomalous_device_from_dict = BehaviorRuleAnomalousDevice.from_dict(behavior_rule_anomalous_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


