# InlineHookChannelCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InlineHookChannelType**](InlineHookChannelType.md) |  | [optional] 
**version** | **str** | Version of the inline hook type. The currently supported version is &#x60;1.0.0&#x60;. | [optional] 

## Example

```python
from okta.models.inline_hook_channel_create import InlineHookChannelCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannelCreate from a JSON string
inline_hook_channel_create_instance = InlineHookChannelCreate.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannelCreate.to_json())

# convert the object into a dict
inline_hook_channel_create_dict = inline_hook_channel_create_instance.to_dict()
# create an instance of InlineHookChannelCreate from a dict
inline_hook_channel_create_from_dict = InlineHookChannelCreate.from_dict(inline_hook_channel_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


