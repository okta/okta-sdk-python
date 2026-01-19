# OAuth2ResourceServerJsonWebKeyRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **str** | RSA key value (exponent) for key binding | [optional] 
**kid** | **str** | Unique identifier of the JSON web key in the custom authorization server&#39;s public JWKS | [optional] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | [optional] 
**n** | **str** | RSA key value (modulus) for key binding | [optional] 
**status** | **str** | Status of the JSON Web Key | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key | [optional] 

## Example

```python
from okta.models.o_auth2_resource_server_json_web_key_request_body import OAuth2ResourceServerJsonWebKeyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ResourceServerJsonWebKeyRequestBody from a JSON string
o_auth2_resource_server_json_web_key_request_body_instance = OAuth2ResourceServerJsonWebKeyRequestBody.from_json(json)
# print the JSON string representation of the object
print(OAuth2ResourceServerJsonWebKeyRequestBody.to_json())

# convert the object into a dict
o_auth2_resource_server_json_web_key_request_body_dict = o_auth2_resource_server_json_web_key_request_body_instance.to_dict()
# create an instance of OAuth2ResourceServerJsonWebKeyRequestBody from a dict
o_auth2_resource_server_json_web_key_request_body_from_dict = OAuth2ResourceServerJsonWebKeyRequestBody.from_dict(o_auth2_resource_server_json_web_key_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


