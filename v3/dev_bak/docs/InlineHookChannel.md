# InlineHookChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InlineHookChannelType**](InlineHookChannelType.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inline_hook_channel import InlineHookChannel

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannel from a JSON string
inline_hook_channel_instance = InlineHookChannel.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannel.to_json())

# convert the object into a dict
inline_hook_channel_dict = inline_hook_channel_instance.to_dict()
# create an instance of InlineHookChannel from a dict
inline_hook_channel_from_dict = InlineHookChannel.from_dict(inline_hook_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


