# WebAuthnCredResponse

Credential response object for enrolled credential details, along with enrollment and key identifiers to associate the credential

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_enrollment_id** | **str** | ID for a WebAuthn preregistration factor in Okta | [optional] 
**cred_response_jwe** | **str** | Encrypted JSON Web Encryption (JWE) of the credential response from the fulfillment provider | [optional] 

## Example

```python
from okta.models.web_authn_cred_response import WebAuthnCredResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnCredResponse from a JSON string
web_authn_cred_response_instance = WebAuthnCredResponse.from_json(json)
# print the JSON string representation of the object
print(WebAuthnCredResponse.to_json())

# convert the object into a dict
web_authn_cred_response_dict = web_authn_cred_response_instance.to_dict()
# create an instance of WebAuthnCredResponse from a dict
web_authn_cred_response_from_dict = WebAuthnCredResponse.from_dict(web_authn_cred_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


