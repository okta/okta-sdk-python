# InlineHookOAuthChannelConfigCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | The authentication method for the token endpoint | [optional] 

## Example

```python
from okta.models.inline_hook_o_auth_channel_config_create import InlineHookOAuthChannelConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookOAuthChannelConfigCreate from a JSON string
inline_hook_o_auth_channel_config_create_instance = InlineHookOAuthChannelConfigCreate.from_json(json)
# print the JSON string representation of the object
print(InlineHookOAuthChannelConfigCreate.to_json())

# convert the object into a dict
inline_hook_o_auth_channel_config_create_dict = inline_hook_o_auth_channel_config_create_instance.to_dict()
# create an instance of InlineHookOAuthChannelConfigCreate from a dict
inline_hook_o_auth_channel_config_create_from_dict = InlineHookOAuthChannelConfigCreate.from_dict(inline_hook_o_auth_channel_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


