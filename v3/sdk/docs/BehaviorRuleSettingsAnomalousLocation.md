# BehaviorRuleSettingsAnomalousLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_events_used_for_evaluation** | **int** |  | [optional] [default to 20]
**min_events_needed_for_evaluation** | **int** |  | [optional] [default to 0]
**granularity** | [**LocationGranularity**](LocationGranularity.md) |  | 
**radius_kilometers** | **int** | Required when &#x60;granularity&#x60; is &#x60;LAT_LONG&#x60;. Radius from the provided coordinates in kilometers. | [optional] 

## Example

```python
from openapi_client.models.behavior_rule_settings_anomalous_location import BehaviorRuleSettingsAnomalousLocation

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorRuleSettingsAnomalousLocation from a JSON string
behavior_rule_settings_anomalous_location_instance = BehaviorRuleSettingsAnomalousLocation.from_json(json)
# print the JSON string representation of the object
print(BehaviorRuleSettingsAnomalousLocation.to_json())

# convert the object into a dict
behavior_rule_settings_anomalous_location_dict = behavior_rule_settings_anomalous_location_instance.to_dict()
# create an instance of BehaviorRuleSettingsAnomalousLocation from a dict
behavior_rule_settings_anomalous_location_from_dict = BehaviorRuleSettingsAnomalousLocation.from_dict(behavior_rule_settings_anomalous_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


