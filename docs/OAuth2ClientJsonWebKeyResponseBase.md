# OAuth2ClientJsonWebKeyResponseBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Timestamp when the OAuth 2.0 client JSON Web Key was created | [optional] [readonly] 
**id** | **str** | The unique ID of the OAuth Client JSON Web Key | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the OAuth 2.0 client JSON Web Key was updated | [optional] [readonly] 
**links** | [**OAuthClientSecretLinks**](OAuthClientSecretLinks.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_client_json_web_key_response_base import OAuth2ClientJsonWebKeyResponseBase

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonWebKeyResponseBase from a JSON string
o_auth2_client_json_web_key_response_base_instance = OAuth2ClientJsonWebKeyResponseBase.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonWebKeyResponseBase.to_json())

# convert the object into a dict
o_auth2_client_json_web_key_response_base_dict = o_auth2_client_json_web_key_response_base_instance.to_dict()
# create an instance of OAuth2ClientJsonWebKeyResponseBase from a dict
o_auth2_client_json_web_key_response_base_from_dict = OAuth2ClientJsonWebKeyResponseBase.from_dict(o_auth2_client_json_web_key_response_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


