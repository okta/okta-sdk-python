# EventHookFilterMapObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**EventHookFilterMapObjectCondition**](EventHookFilterMapObjectCondition.md) |  | [optional] 
**event** | **str** | The filtered event type | [optional] 

## Example

```python
from okta.models.event_hook_filter_map_object import EventHookFilterMapObject

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookFilterMapObject from a JSON string
event_hook_filter_map_object_instance = EventHookFilterMapObject.from_json(json)
# print the JSON string representation of the object
print(EventHookFilterMapObject.to_json())

# convert the object into a dict
event_hook_filter_map_object_dict = event_hook_filter_map_object_instance.to_dict()
# create an instance of EventHookFilterMapObject from a dict
event_hook_filter_map_object_from_dict = EventHookFilterMapObject.from_dict(event_hook_filter_map_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


