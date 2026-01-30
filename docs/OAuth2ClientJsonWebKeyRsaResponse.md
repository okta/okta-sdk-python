# OAuth2ClientJsonWebKeyRsaResponse

An RSA signing key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **str** | RSA key value (exponent) for key binding | 
**n** | **str** | RSA key value (modulus) for key binding | 

## Example

```python
from okta.models.o_auth2_client_json_web_key_rsa_response import OAuth2ClientJsonWebKeyRsaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonWebKeyRsaResponse from a JSON string
o_auth2_client_json_web_key_rsa_response_instance = OAuth2ClientJsonWebKeyRsaResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonWebKeyRsaResponse.to_json())

# convert the object into a dict
o_auth2_client_json_web_key_rsa_response_dict = o_auth2_client_json_web_key_rsa_response_instance.to_dict()
# create an instance of OAuth2ClientJsonWebKeyRsaResponse from a dict
o_auth2_client_json_web_key_rsa_response_from_dict = OAuth2ClientJsonWebKeyRsaResponse.from_dict(o_auth2_client_json_web_key_rsa_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


