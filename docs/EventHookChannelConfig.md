# EventHookChannelConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**EventHookChannelConfigAuthScheme**](EventHookChannelConfigAuthScheme.md) |  | [optional] 
**headers** | [**List[EventHookChannelConfigHeader]**](EventHookChannelConfigHeader.md) | Optional list of key/value pairs for headers that can be sent with the request to the external service. For example, &#x60;X-Other-Header&#x60; is an example of an optional header, with a value of &#x60;my-header-value&#x60;, that you want Okta to pass to your external service. | [optional] 
**method** | **str** | The method of the Okta event hook request | [optional] [readonly] 
**uri** | **str** | The external service endpoint called to execute the event hook handler | 

## Example

```python
from okta.models.event_hook_channel_config import EventHookChannelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookChannelConfig from a JSON string
event_hook_channel_config_instance = EventHookChannelConfig.from_json(json)
# print the JSON string representation of the object
print(EventHookChannelConfig.to_json())

# convert the object into a dict
event_hook_channel_config_dict = event_hook_channel_config_instance.to_dict()
# create an instance of EventHookChannelConfig from a dict
event_hook_channel_config_from_dict = EventHookChannelConfig.from_dict(event_hook_channel_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


