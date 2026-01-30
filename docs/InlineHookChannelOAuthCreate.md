# InlineHookChannelOAuthCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**InlineHookOAuthChannelConfigCreate**](InlineHookOAuthChannelConfigCreate.md) |  | [optional] 

## Example

```python
from okta.models.inline_hook_channel_o_auth_create import InlineHookChannelOAuthCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannelOAuthCreate from a JSON string
inline_hook_channel_o_auth_create_instance = InlineHookChannelOAuthCreate.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannelOAuthCreate.to_json())

# convert the object into a dict
inline_hook_channel_o_auth_create_dict = inline_hook_channel_o_auth_create_instance.to_dict()
# create an instance of InlineHookChannelOAuthCreate from a dict
inline_hook_channel_o_auth_create_from_dict = InlineHookChannelOAuthCreate.from_dict(inline_hook_channel_o_auth_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


