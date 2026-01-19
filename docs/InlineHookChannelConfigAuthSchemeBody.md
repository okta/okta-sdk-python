# InlineHookChannelConfigAuthSchemeBody

The authentication scheme to use for this request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The header name for the authorization server | [optional] 
**type** | **str** | The authentication scheme type. Supported type&amp;mdash;&#x60;HEADER&#x60;. | [optional] 
**value** | **str** | The header value. This secret value is passed to your external service endpoint. Your external service can check it as a security measure. | [optional] 

## Example

```python
from okta.models.inline_hook_channel_config_auth_scheme_body import InlineHookChannelConfigAuthSchemeBody

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookChannelConfigAuthSchemeBody from a JSON string
inline_hook_channel_config_auth_scheme_body_instance = InlineHookChannelConfigAuthSchemeBody.from_json(json)
# print the JSON string representation of the object
print(InlineHookChannelConfigAuthSchemeBody.to_json())

# convert the object into a dict
inline_hook_channel_config_auth_scheme_body_dict = inline_hook_channel_config_auth_scheme_body_instance.to_dict()
# create an instance of InlineHookChannelConfigAuthSchemeBody from a dict
inline_hook_channel_config_auth_scheme_body_from_dict = InlineHookChannelConfigAuthSchemeBody.from_dict(inline_hook_channel_config_auth_scheme_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


