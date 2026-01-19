# EventHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**EventHookChannel**](EventHookChannel.md) |  | 
**created** | **datetime** | Timestamp of the event hook creation | [optional] [readonly] 
**created_by** | **str** | The ID of the user who created the event hook | [optional] [readonly] 
**description** | **str** | Description of the event hook | [optional] 
**events** | [**EventSubscriptions**](EventSubscriptions.md) |  | 
**id** | **str** | Unique key for the event hook | [optional] [readonly] 
**last_updated** | **datetime** | Date of the last event hook update | [optional] [readonly] 
**name** | **str** | Display name for the event hook | 
**status** | **str** | Status of the event hook | [optional] [readonly] 
**verification_status** | [**EventHookVerificationStatus**](EventHookVerificationStatus.md) |  | [optional] 
**links** | [**EventHookLinks**](EventHookLinks.md) |  | [optional] 

## Example

```python
from okta.models.event_hook import EventHook

# TODO update the JSON string below
json = "{}"
# create an instance of EventHook from a JSON string
event_hook_instance = EventHook.from_json(json)
# print the JSON string representation of the object
print(EventHook.to_json())

# convert the object into a dict
event_hook_dict = event_hook_instance.to_dict()
# create an instance of EventHook from a dict
event_hook_from_dict = EventHook.from_dict(event_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


