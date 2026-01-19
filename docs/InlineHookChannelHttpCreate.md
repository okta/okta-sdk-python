# InlineHookChannelHttpCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**InlineHookHttpConfigCreate**](InlineHookHttpConfigCreate.md) |  | [optional] 

## Example

```python
from okta.models.inline_hook_channel_http_create import InlineHookChannelHttpCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannelHttpCreate from a JSON string
inline_hook_channel_http_create_instance = InlineHookChannelHttpCreate.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannelHttpCreate.to_json())

# convert the object into a dict
inline_hook_channel_http_create_dict = inline_hook_channel_http_create_instance.to_dict()
# create an instance of InlineHookChannelHttpCreate from a dict
inline_hook_channel_http_create_from_dict = InlineHookChannelHttpCreate.from_dict(inline_hook_channel_http_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


