# EventHookChannelConfigHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from okta.models.event_hook_channel_config_header import EventHookChannelConfigHeader

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookChannelConfigHeader from a JSON string
event_hook_channel_config_header_instance = EventHookChannelConfigHeader.from_json(json)
# print the JSON string representation of the object
print(EventHookChannelConfigHeader.to_json())

# convert the object into a dict
event_hook_channel_config_header_dict = event_hook_channel_config_header_instance.to_dict()
# create an instance of EventHookChannelConfigHeader from a dict
event_hook_channel_config_header_from_dict = EventHookChannelConfigHeader.from_dict(event_hook_channel_config_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


