# OAuth2ClientJsonWebKeyECResponse

An EC signing key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **str** | The public x coordinate for the elliptic curve point | 
**y** | **str** | The public y coordinate for the elliptic curve point | 
**crv** | **str** | The cryptographic curve used with the key | 

## Example

```python
from okta.models.o_auth2_client_json_web_key_ec_response import OAuth2ClientJsonWebKeyECResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonWebKeyECResponse from a JSON string
o_auth2_client_json_web_key_ec_response_instance = OAuth2ClientJsonWebKeyECResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonWebKeyECResponse.to_json())

# convert the object into a dict
o_auth2_client_json_web_key_ec_response_dict = o_auth2_client_json_web_key_ec_response_instance.to_dict()
# create an instance of OAuth2ClientJsonWebKeyECResponse from a dict
o_auth2_client_json_web_key_ec_response_from_dict = OAuth2ClientJsonWebKeyECResponse.from_dict(o_auth2_client_json_web_key_ec_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


