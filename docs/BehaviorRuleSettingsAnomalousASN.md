# BehaviorRuleSettingsAnomalousASN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_events_used_for_evaluation** | **int** |  | [optional] [default to 20]
**min_events_needed_for_evaluation** | **int** |  | [optional] [default to 0]

## Example

```python
from okta.models.behavior_rule_settings_anomalous_asn import BehaviorRuleSettingsAnomalousASN

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorRuleSettingsAnomalousASN from a JSON string
behavior_rule_settings_anomalous_asn_instance = BehaviorRuleSettingsAnomalousASN.from_json(json)
# print the JSON string representation of the object
print(BehaviorRuleSettingsAnomalousASN.to_json())

# convert the object into a dict
behavior_rule_settings_anomalous_asn_dict = behavior_rule_settings_anomalous_asn_instance.to_dict()
# create an instance of BehaviorRuleSettingsAnomalousASN from a dict
behavior_rule_settings_anomalous_asn_from_dict = BehaviorRuleSettingsAnomalousASN.from_dict(behavior_rule_settings_anomalous_asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


