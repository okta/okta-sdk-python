# AuthenticatorEnrollmentPolicyConditionsAllOfPeople

Identifies users and groups that are used together

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups**](AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_conditions_all_of_people import AuthenticatorEnrollmentPolicyConditionsAllOfPeople

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyConditionsAllOfPeople from a JSON string
authenticator_enrollment_policy_conditions_all_of_people_instance = AuthenticatorEnrollmentPolicyConditionsAllOfPeople.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyConditionsAllOfPeople.to_json())

# convert the object into a dict
authenticator_enrollment_policy_conditions_all_of_people_dict = authenticator_enrollment_policy_conditions_all_of_people_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyConditionsAllOfPeople from a dict
authenticator_enrollment_policy_conditions_all_of_people_from_dict = AuthenticatorEnrollmentPolicyConditionsAllOfPeople.from_dict(authenticator_enrollment_policy_conditions_all_of_people_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


