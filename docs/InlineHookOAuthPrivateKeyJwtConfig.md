# InlineHookOAuthPrivateKeyJwtConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | **str** | Not applicable. Must be &#x60;null&#x60;. | [optional] 
**hook_key_id** | **str** | An ID value of the hook key pair generated from the [Hook Keys API](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/HookKey/#tag/HookKey) | [optional] 
**method** | **str** | The method of the Okta inline hook request. Only accepts &#x60;POST&#x60;. | [optional] 
**auth_type** | **str** |  | [optional] 
**client_id** | **str** | A publicly exposed string provided by the service that&#39;s used to identify the OAuth app and build authorization URLs | [optional] 
**scope** | **str** | Include the scopes that allow you to perform the actions on the hook endpoint that you want to access | [optional] 
**token_url** | **str** | The URI where inline hooks can exchange an authorization code for access and refresh tokens | [optional] 
**headers** | [**List[InlineHookChannelConfigHeaders]**](InlineHookChannelConfigHeaders.md) | An optional list of key/value pairs for headers that you can send with the request to the external service | [optional] 
**uri** | **str** | The external service endpoint that executes the inline hook handler. It must begin with &#x60;https://&#x60; and be reachable by Okta. No white space is allowed in the URI. | [optional] 

## Example

```python
from okta.models.inline_hook_o_auth_private_key_jwt_config import InlineHookOAuthPrivateKeyJwtConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookOAuthPrivateKeyJwtConfig from a JSON string
inline_hook_o_auth_private_key_jwt_config_instance = InlineHookOAuthPrivateKeyJwtConfig.from_json(json)
# print the JSON string representation of the object
print(InlineHookOAuthPrivateKeyJwtConfig.to_json())

# convert the object into a dict
inline_hook_o_auth_private_key_jwt_config_dict = inline_hook_o_auth_private_key_jwt_config_instance.to_dict()
# create an instance of InlineHookOAuthPrivateKeyJwtConfig from a dict
inline_hook_o_auth_private_key_jwt_config_from_dict = InlineHookOAuthPrivateKeyJwtConfig.from_dict(inline_hook_o_auth_private_key_jwt_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


