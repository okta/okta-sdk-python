# InlineHookChannelConfigAuthSchemeResponse

The authentication scheme to use for this request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The header name for the authorization server | [optional] 
**type** | **str** | The authentication scheme type. Supported type&amp;mdash;&#x60;HEADER&#x60; | [optional] 

## Example

```python
from okta.models.inline_hook_channel_config_auth_scheme_response import InlineHookChannelConfigAuthSchemeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannelConfigAuthSchemeResponse from a JSON string
inline_hook_channel_config_auth_scheme_response_instance = InlineHookChannelConfigAuthSchemeResponse.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannelConfigAuthSchemeResponse.to_json())

# convert the object into a dict
inline_hook_channel_config_auth_scheme_response_dict = inline_hook_channel_config_auth_scheme_response_instance.to_dict()
# create an instance of InlineHookChannelConfigAuthSchemeResponse from a dict
inline_hook_channel_config_auth_scheme_response_from_dict = InlineHookChannelConfigAuthSchemeResponse.from_dict(inline_hook_channel_config_auth_scheme_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


