# InlineHookChannelConfigHeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The optional field or header name | [optional] 
**value** | **str** | The value for the key | [optional] 

## Example

```python
from okta.models.inline_hook_channel_config_headers import InlineHookChannelConfigHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannelConfigHeaders from a JSON string
inline_hook_channel_config_headers_instance = InlineHookChannelConfigHeaders.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannelConfigHeaders.to_json())

# convert the object into a dict
inline_hook_channel_config_headers_dict = inline_hook_channel_config_headers_instance.to_dict()
# create an instance of InlineHookChannelConfigHeaders from a dict
inline_hook_channel_config_headers_from_dict = InlineHookChannelConfigHeaders.from_dict(inline_hook_channel_config_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


