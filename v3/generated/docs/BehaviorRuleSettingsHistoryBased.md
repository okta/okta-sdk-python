# BehaviorRuleSettingsHistoryBased


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_events_used_for_evaluation** | **int** |  | [optional] [default to 20]
**min_events_needed_for_evaluation** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.behavior_rule_settings_history_based import BehaviorRuleSettingsHistoryBased

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorRuleSettingsHistoryBased from a JSON string
behavior_rule_settings_history_based_instance = BehaviorRuleSettingsHistoryBased.from_json(json)
# print the JSON string representation of the object
print(BehaviorRuleSettingsHistoryBased.to_json())

# convert the object into a dict
behavior_rule_settings_history_based_dict = behavior_rule_settings_history_based_instance.to_dict()
# create an instance of BehaviorRuleSettingsHistoryBased from a dict
behavior_rule_settings_history_based_form_dict = behavior_rule_settings_history_based.from_dict(behavior_rule_settings_history_based_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


