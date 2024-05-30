# EventHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**EventHookChannel**](EventHookChannel.md) |  | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**created_by** | **str** |  | [optional] 
**events** | [**EventSubscriptions**](EventSubscriptions.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**verification_status** | [**EventHookVerificationStatus**](EventHookVerificationStatus.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.event_hook import EventHook

# TODO update the JSON string below
json = "{}"
# create an instance of EventHook from a JSON string
event_hook_instance = EventHook.from_json(json)
# print the JSON string representation of the object
print(EventHook.to_json())

# convert the object into a dict
event_hook_dict = event_hook_instance.to_dict()
# create an instance of EventHook from a dict
event_hook_form_dict = event_hook.from_dict(event_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


