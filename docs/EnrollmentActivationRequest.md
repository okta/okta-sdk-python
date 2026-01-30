# EnrollmentActivationRequest

Enrollment Initialization Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cred_responses** | [**List[WebAuthnCredResponse]**](WebAuthnCredResponse.md) | List of credential responses from the fulfillment provider | [optional] 
**fulfillment_provider** | **str** | Name of the fulfillment provider for the WebAuthn preregistration factor | [optional] 
**pin_response_jwe** | **str** | Encrypted JWE of the PIN response from the fulfillment provider | [optional] 
**serial** | **str** | Serial number of the YubiKey | [optional] 
**user_id** | **str** | ID of an existing Okta user | [optional] 
**version** | **str** | Firmware version of the YubiKey | [optional] 
**yubico_signing_jwks** | [**List[ECKeyJWK]**](ECKeyJWK.md) | List of usable signing keys from Yubico (in JSON Web Key Sets (JWKS) format). The signing keys are used to verify the JSON Web Signature (JWS) inside the JWE. | [optional] 

## Example

```python
from okta.models.enrollment_activation_request import EnrollmentActivationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentActivationRequest from a JSON string
enrollment_activation_request_instance = EnrollmentActivationRequest.from_json(json)
# print the JSON string representation of the object
print(EnrollmentActivationRequest.to_json())

# convert the object into a dict
enrollment_activation_request_dict = enrollment_activation_request_instance.to_dict()
# create an instance of EnrollmentActivationRequest from a dict
enrollment_activation_request_from_dict = EnrollmentActivationRequest.from_dict(enrollment_activation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


