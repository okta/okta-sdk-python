# InlineHookOAuthClientSecretConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** |  | [optional] 
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
from okta.models.inline_hook_o_auth_client_secret_config import InlineHookOAuthClientSecretConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookOAuthClientSecretConfig from a JSON string
inline_hook_o_auth_client_secret_config_instance = InlineHookOAuthClientSecretConfig.from_json(json)
# print the JSON string representation of the object
print(InlineHookOAuthClientSecretConfig.to_json())

# convert the object into a dict
inline_hook_o_auth_client_secret_config_dict = inline_hook_o_auth_client_secret_config_instance.to_dict()
# create an instance of InlineHookOAuthClientSecretConfig from a dict
inline_hook_o_auth_client_secret_config_from_dict = InlineHookOAuthClientSecretConfig.from_dict(inline_hook_o_auth_client_secret_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


