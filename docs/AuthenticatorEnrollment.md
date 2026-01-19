# AuthenticatorEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the authenticator enrollment was created | [optional] 
**id** | **str** | The unique identifier of the authenticator enrollment | [optional] 
**key** | **str** | A human-readable string that identifies the authenticator | [optional] 
**last_updated** | **datetime** | Timestamp when the authenticator enrollment was last updated | [optional] 
**name** | **str** | The authenticator display name | [optional] 
**profile** | [**AuthenticatorProfile**](AuthenticatorProfile.md) |  | [optional] 
**status** | **str** | Status of the enrollment | [optional] 
**type** | [**AuthenticatorType**](AuthenticatorType.md) |  | [optional] 
**links** | [**AuthenticatorEnrollmentLinks**](AuthenticatorEnrollmentLinks.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment import AuthenticatorEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollment from a JSON string
authenticator_enrollment_instance = AuthenticatorEnrollment.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollment.to_json())

# convert the object into a dict
authenticator_enrollment_dict = authenticator_enrollment_instance.to_dict()
# create an instance of AuthenticatorEnrollment from a dict
authenticator_enrollment_from_dict = AuthenticatorEnrollment.from_dict(authenticator_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


