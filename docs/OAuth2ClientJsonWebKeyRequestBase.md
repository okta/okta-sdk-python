# OAuth2ClientJsonWebKeyRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | Unique identifier of the JSON Web Key in the OAUth 2.0 client&#39;s JWKS | [optional] 
**status** | **str** | Status of the OAuth 2.0 client JSON Web Key | [optional] [default to 'ACTIVE']

## Example

```python
from okta.models.o_auth2_client_json_web_key_request_base import OAuth2ClientJsonWebKeyRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonWebKeyRequestBase from a JSON string
o_auth2_client_json_web_key_request_base_instance = OAuth2ClientJsonWebKeyRequestBase.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonWebKeyRequestBase.to_json())

# convert the object into a dict
o_auth2_client_json_web_key_request_base_dict = o_auth2_client_json_web_key_request_base_instance.to_dict()
# create an instance of OAuth2ClientJsonWebKeyRequestBase from a dict
o_auth2_client_json_web_key_request_base_from_dict = OAuth2ClientJsonWebKeyRequestBase.from_dict(o_auth2_client_json_web_key_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


