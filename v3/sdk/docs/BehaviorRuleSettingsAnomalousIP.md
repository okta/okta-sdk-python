# BehaviorRuleSettingsAnomalousIP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_events_used_for_evaluation** | **int** |  | [optional] [default to 50]
**min_events_needed_for_evaluation** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.behavior_rule_settings_anomalous_ip import BehaviorRuleSettingsAnomalousIP

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorRuleSettingsAnomalousIP from a JSON string
behavior_rule_settings_anomalous_ip_instance = BehaviorRuleSettingsAnomalousIP.from_json(json)
# print the JSON string representation of the object
print(BehaviorRuleSettingsAnomalousIP.to_json())

# convert the object into a dict
behavior_rule_settings_anomalous_ip_dict = behavior_rule_settings_anomalous_ip_instance.to_dict()
# create an instance of BehaviorRuleSettingsAnomalousIP from a dict
behavior_rule_settings_anomalous_ip_from_dict = BehaviorRuleSettingsAnomalousIP.from_dict(behavior_rule_settings_anomalous_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


