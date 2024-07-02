# EventHookChannelConfigAuthScheme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**type** | [**EventHookChannelConfigAuthSchemeType**](EventHookChannelConfigAuthSchemeType.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.event_hook_channel_config_auth_scheme import EventHookChannelConfigAuthScheme

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookChannelConfigAuthScheme from a JSON string
event_hook_channel_config_auth_scheme_instance = EventHookChannelConfigAuthScheme.from_json(json)
# print the JSON string representation of the object
print(EventHookChannelConfigAuthScheme.to_json())

# convert the object into a dict
event_hook_channel_config_auth_scheme_dict = event_hook_channel_config_auth_scheme_instance.to_dict()
# create an instance of EventHookChannelConfigAuthScheme from a dict
event_hook_channel_config_auth_scheme_from_dict = EventHookChannelConfigAuthScheme.from_dict(event_hook_channel_config_auth_scheme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


