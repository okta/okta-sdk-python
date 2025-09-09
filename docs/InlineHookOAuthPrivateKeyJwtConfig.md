# InlineHookOAuthPrivateKeyJwtConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook_key_id** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**token_url** | **str** |  | [optional] 
**auth_scheme** | [**InlineHookChannelConfigAuthScheme**](InlineHookChannelConfigAuthScheme.md) |  | [optional] 
**headers** | [**List[InlineHookChannelConfigHeaders]**](InlineHookChannelConfigHeaders.md) |  | [optional] 
**method** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

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


