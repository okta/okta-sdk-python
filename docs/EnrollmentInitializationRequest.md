# EnrollmentInitializationRequest

Enrollment initialization request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_rp_ids** | **List[str]** | List of relying party hostnames to register on the YubiKey | [optional] 
**fulfillment_provider** | **str** | Name of the fulfillment provider for the WebAuthn preregistration factor | [optional] 
**user_id** | **str** | ID of an existing Okta user | [optional] 
**yubico_transport_key_jwk** | [**ECKeyJWK**](ECKeyJWK.md) |  | [optional] 

## Example

```python
from okta.models.enrollment_initialization_request import EnrollmentInitializationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentInitializationRequest from a JSON string
enrollment_initialization_request_instance = EnrollmentInitializationRequest.from_json(json)
# print the JSON string representation of the object
print(EnrollmentInitializationRequest.to_json())

# convert the object into a dict
enrollment_initialization_request_dict = enrollment_initialization_request_instance.to_dict()
# create an instance of EnrollmentInitializationRequest from a dict
enrollment_initialization_request_from_dict = EnrollmentInitializationRequest.from_dict(enrollment_initialization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


