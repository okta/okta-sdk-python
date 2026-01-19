# TacAuthenticatorEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the authenticator enrollment was created | [optional] 
**id** | **str** | A unique identifier of the authenticator enrollment | [optional] 
**key** | **str** | A human-readable string that identifies the authenticator | [optional] 
**last_updated** | **datetime** | Timestamp when the authenticator enrollment was last updated | [optional] 
**name** | **str** | The authenticator display name | [optional] 
**nickname** | **str** | A user-friendly name for the authenticator enrollment | [optional] 
**profile** | [**AuthenticatorProfileTacResponsePost**](AuthenticatorProfileTacResponsePost.md) |  | [optional] 
**status** | **str** | Status of the enrollment | [optional] 
**type** | [**AuthenticatorType**](AuthenticatorType.md) |  | [optional] 
**links** | [**AuthenticatorEnrollmentLinks**](AuthenticatorEnrollmentLinks.md) |  | [optional] 

## Example

```python
from okta.models.tac_authenticator_enrollment import TacAuthenticatorEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of TacAuthenticatorEnrollment from a JSON string
tac_authenticator_enrollment_instance = TacAuthenticatorEnrollment.from_json(json)
# print the JSON string representation of the object
print(TacAuthenticatorEnrollment.to_json())

# convert the object into a dict
tac_authenticator_enrollment_dict = tac_authenticator_enrollment_instance.to_dict()
# create an instance of TacAuthenticatorEnrollment from a dict
tac_authenticator_enrollment_from_dict = TacAuthenticatorEnrollment.from_dict(tac_authenticator_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


