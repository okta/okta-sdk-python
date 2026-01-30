# EnrollmentActivationResponse

Enrollment initialization response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_enrollment_ids** | **List[str]** | List of IDs for preregistered WebAuthn factors in Okta | [optional] 
**fulfillment_provider** | **str** | Name of the fulfillment provider for the WebAuthn preregistration factor | [optional] 
**user_id** | **str** | ID of an existing Okta user | [optional] 

## Example

```python
from okta.models.enrollment_activation_response import EnrollmentActivationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentActivationResponse from a JSON string
enrollment_activation_response_instance = EnrollmentActivationResponse.from_json(json)
# print the JSON string representation of the object
print(EnrollmentActivationResponse.to_json())

# convert the object into a dict
enrollment_activation_response_dict = enrollment_activation_response_instance.to_dict()
# create an instance of EnrollmentActivationResponse from a dict
enrollment_activation_response_from_dict = EnrollmentActivationResponse.from_dict(enrollment_activation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


