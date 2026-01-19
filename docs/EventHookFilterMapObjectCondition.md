# EventHookFilterMapObjectCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | The Okta Expression language statement that filters the event type | [optional] 
**version** | **str** | Internal field | [optional] [readonly] 

## Example

```python
from okta.models.event_hook_filter_map_object_condition import EventHookFilterMapObjectCondition

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookFilterMapObjectCondition from a JSON string
event_hook_filter_map_object_condition_instance = EventHookFilterMapObjectCondition.from_json(json)
# print the JSON string representation of the object
print(EventHookFilterMapObjectCondition.to_json())

# convert the object into a dict
event_hook_filter_map_object_condition_dict = event_hook_filter_map_object_condition_instance.to_dict()
# create an instance of EventHookFilterMapObjectCondition from a dict
event_hook_filter_map_object_condition_from_dict = EventHookFilterMapObjectCondition.from_dict(event_hook_filter_map_object_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


