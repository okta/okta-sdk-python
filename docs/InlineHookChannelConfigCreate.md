# InlineHookChannelConfigCreate

Properties of the communications channel that are used to contact your external service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**List[InlineHookChannelConfigHeaders]**](InlineHookChannelConfigHeaders.md) | An optional list of key/value pairs for headers that you can send with the request to the external service. | [optional] 
**method** | **str** | The method of the Okta inline hook request | [optional] 
**uri** | **str** | The external service endpoint that executes the inline hook handler. It must begin with &#x60;https://&#x60; and be reachable by Okta. No white space is allowed in the URI. | [optional] 

## Example

```python
from okta.models.inline_hook_channel_config_create import InlineHookChannelConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannelConfigCreate from a JSON string
inline_hook_channel_config_create_instance = InlineHookChannelConfigCreate.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannelConfigCreate.to_json())

# convert the object into a dict
inline_hook_channel_config_create_dict = inline_hook_channel_config_create_instance.to_dict()
# create an instance of InlineHookChannelConfigCreate from a dict
inline_hook_channel_config_create_from_dict = InlineHookChannelConfigCreate.from_dict(inline_hook_channel_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


