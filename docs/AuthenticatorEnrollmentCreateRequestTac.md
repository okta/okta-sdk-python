# AuthenticatorEnrollmentCreateRequestTac


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_id** | **str** | Unique identifier of the TAC authenticator | 
**profile** | [**AuthenticatorProfileTacRequest**](AuthenticatorProfileTacRequest.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_create_request_tac import AuthenticatorEnrollmentCreateRequestTac

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentCreateRequestTac from a JSON string
authenticator_enrollment_create_request_tac_instance = AuthenticatorEnrollmentCreateRequestTac.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentCreateRequestTac.to_json())

# convert the object into a dict
authenticator_enrollment_create_request_tac_dict = authenticator_enrollment_create_request_tac_instance.to_dict()
# create an instance of AuthenticatorEnrollmentCreateRequestTac from a dict
authenticator_enrollment_create_request_tac_from_dict = AuthenticatorEnrollmentCreateRequestTac.from_dict(authenticator_enrollment_create_request_tac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


