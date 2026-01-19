# AuthenticatorEnrollmentCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_id** | **str** | Unique identifier of the &#x60;phone&#x60; authenticator | 
**profile** | [**AuthenticatorProfile**](AuthenticatorProfile.md) |  | 

## Example

```python
from okta.models.authenticator_enrollment_create_request import AuthenticatorEnrollmentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentCreateRequest from a JSON string
authenticator_enrollment_create_request_instance = AuthenticatorEnrollmentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentCreateRequest.to_json())

# convert the object into a dict
authenticator_enrollment_create_request_dict = authenticator_enrollment_create_request_instance.to_dict()
# create an instance of AuthenticatorEnrollmentCreateRequest from a dict
authenticator_enrollment_create_request_from_dict = AuthenticatorEnrollmentCreateRequest.from_dict(authenticator_enrollment_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


