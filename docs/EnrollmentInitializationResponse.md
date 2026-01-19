# EnrollmentInitializationResponse

Yubico transport key in the form of a JSON Web Token (JWK), used to encrypt our fulfillment request to Yubico. The currently agreed protocol uses P-384.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cred_requests** | [**List[WebAuthnCredRequest]**](WebAuthnCredRequest.md) | List of credential requests for the fulfillment provider | [optional] 
**fulfillment_provider** | **str** | Name of the fulfillment provider for the WebAuthn preregistration factor | [optional] 
**pin_request_jwe** | **str** | Encrypted JWE of PIN request for the fulfillment provider | [optional] 
**user_id** | **str** | ID of an existing Okta user | [optional] 

## Example

```python
from okta.models.enrollment_initialization_response import EnrollmentInitializationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentInitializationResponse from a JSON string
enrollment_initialization_response_instance = EnrollmentInitializationResponse.from_json(json)
# print the JSON string representation of the object
print(EnrollmentInitializationResponse.to_json())

# convert the object into a dict
enrollment_initialization_response_dict = enrollment_initialization_response_instance.to_dict()
# create an instance of EnrollmentInitializationResponse from a dict
enrollment_initialization_response_from_dict = EnrollmentInitializationResponse.from_dict(enrollment_initialization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


