# AuthenticatorEnrollmentPolicyConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**people** | [**AuthenticatorEnrollmentPolicyConditionsAllOfPeople**](AuthenticatorEnrollmentPolicyConditionsAllOfPeople.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_conditions import AuthenticatorEnrollmentPolicyConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyConditions from a JSON string
authenticator_enrollment_policy_conditions_instance = AuthenticatorEnrollmentPolicyConditions.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyConditions.to_json())

# convert the object into a dict
authenticator_enrollment_policy_conditions_dict = authenticator_enrollment_policy_conditions_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyConditions from a dict
authenticator_enrollment_policy_conditions_from_dict = AuthenticatorEnrollmentPolicyConditions.from_dict(authenticator_enrollment_policy_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


