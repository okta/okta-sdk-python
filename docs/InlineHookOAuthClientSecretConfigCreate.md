# InlineHookOAuthClientSecretConfigCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** | A private value provided by the service used to authenticate the identity of the app to the service | [optional] 
**method** | **str** | The method of the Okta inline hook request. Only accepts &#x60;POST&#x60;. | [optional] 
**auth_type** | **str** |  | [optional] 
**client_id** | **str** | A publicly exposed string provided by the service that&#39;s used to identify the OAuth app and build authorization URLs | [optional] 
**scope** | **str** | Include the scopes that allow you to perform the actions on the hook endpoint that you want to access | [optional] 
**token_url** | **str** | The URI where inline hooks can exchange an authorization code for access and refresh tokens | [optional] 
**headers** | [**List[InlineHookChannelConfigHeaders]**](InlineHookChannelConfigHeaders.md) | An optional list of key/value pairs for headers that you can send with the request to the external service | [optional] 
**uri** | **str** | The external service endpoint that executes the inline hook handler. It must begin with &#x60;https://&#x60; and be reachable by Okta. No white space is allowed in the URI. | [optional] 

## Example

```python
from okta.models.inline_hook_o_auth_client_secret_config_create import InlineHookOAuthClientSecretConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookOAuthClientSecretConfigCreate from a JSON string
inline_hook_o_auth_client_secret_config_create_instance = InlineHookOAuthClientSecretConfigCreate.from_json(json)
# print the JSON string representation of the object
print(InlineHookOAuthClientSecretConfigCreate.to_json())

# convert the object into a dict
inline_hook_o_auth_client_secret_config_create_dict = inline_hook_o_auth_client_secret_config_create_instance.to_dict()
# create an instance of InlineHookOAuthClientSecretConfigCreate from a dict
inline_hook_o_auth_client_secret_config_create_from_dict = InlineHookOAuthClientSecretConfigCreate.from_dict(inline_hook_o_auth_client_secret_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


