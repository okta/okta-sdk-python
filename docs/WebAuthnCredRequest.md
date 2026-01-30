# WebAuthnCredRequest

Credential request object for the initialized credential, along with the enrollment and key identifiers to associate with the credential

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_enrollment_id** | **str** | ID for a WebAuthn preregistration factor in Okta | [optional] 
**cred_request_jwe** | **str** | Encrypted JWE of credential request for the fulfillment provider | [optional] 
**key_id** | **str** | ID for the Okta response key-pair used to encrypt and decrypt credential requests and responses | [optional] 

## Example

```python
from okta.models.web_authn_cred_request import WebAuthnCredRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnCredRequest from a JSON string
web_authn_cred_request_instance = WebAuthnCredRequest.from_json(json)
# print the JSON string representation of the object
print(WebAuthnCredRequest.to_json())

# convert the object into a dict
web_authn_cred_request_dict = web_authn_cred_request_instance.to_dict()
# create an instance of WebAuthnCredRequest from a dict
web_authn_cred_request_from_dict = WebAuthnCredRequest.from_dict(web_authn_cred_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


