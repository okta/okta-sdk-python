# EventHookChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**EventHookChannelConfig**](EventHookChannelConfig.md) |  | 
**type** | [**EventHookChannelType**](EventHookChannelType.md) |  | 
**version** | **str** | Version of the channel. Currently the only supported version is &#x60;1.0.0&#x60;. | 

## Example

```python
from okta.models.event_hook_channel import EventHookChannel

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookChannel from a JSON string
event_hook_channel_instance = EventHookChannel.from_json(json)
# print the JSON string representation of the object
print(EventHookChannel.to_json())

# convert the object into a dict
event_hook_channel_dict = event_hook_channel_instance.to_dict()
# create an instance of EventHookChannel from a dict
event_hook_channel_from_dict = EventHookChannel.from_dict(event_hook_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


