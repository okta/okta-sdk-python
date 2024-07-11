# BehaviorRuleSettingsAnomalousDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_events_used_for_evaluation** | **int** |  | [optional] [default to 20]
**min_events_needed_for_evaluation** | **int** |  | [optional] [default to 0]

## Example

```python
from okta.models.behavior_rule_settings_anomalous_device import BehaviorRuleSettingsAnomalousDevice

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorRuleSettingsAnomalousDevice from a JSON string
behavior_rule_settings_anomalous_device_instance = BehaviorRuleSettingsAnomalousDevice.from_json(json)
# print the JSON string representation of the object
print(BehaviorRuleSettingsAnomalousDevice.to_json())

# convert the object into a dict
behavior_rule_settings_anomalous_device_dict = behavior_rule_settings_anomalous_device_instance.to_dict()
# create an instance of BehaviorRuleSettingsAnomalousDevice from a dict
behavior_rule_settings_anomalous_device_from_dict = BehaviorRuleSettingsAnomalousDevice.from_dict(behavior_rule_settings_anomalous_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


