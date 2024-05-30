# InlineHookChannelConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**InlineHookChannelConfigAuthScheme**](InlineHookChannelConfigAuthScheme.md) |  | [optional] 
**headers** | [**List[InlineHookChannelConfigHeaders]**](InlineHookChannelConfigHeaders.md) |  | [optional] 
**method** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inline_hook_channel_config import InlineHookChannelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannelConfig from a JSON string
inline_hook_channel_config_instance = InlineHookChannelConfig.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannelConfig.to_json())

# convert the object into a dict
inline_hook_channel_config_dict = inline_hook_channel_config_instance.to_dict()
# create an instance of InlineHookChannelConfig from a dict
inline_hook_channel_config_form_dict = inline_hook_channel_config.from_dict(inline_hook_channel_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


