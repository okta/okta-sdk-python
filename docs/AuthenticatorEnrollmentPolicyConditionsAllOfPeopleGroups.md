# AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups

Specifies a set of groups whose users are to be included or excluded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Groups to be included | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_conditions_all_of_people_groups import AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups from a JSON string
authenticator_enrollment_policy_conditions_all_of_people_groups_instance = AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups.to_json())

# convert the object into a dict
authenticator_enrollment_policy_conditions_all_of_people_groups_dict = authenticator_enrollment_policy_conditions_all_of_people_groups_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups from a dict
authenticator_enrollment_policy_conditions_all_of_people_groups_from_dict = AuthenticatorEnrollmentPolicyConditionsAllOfPeopleGroups.from_dict(authenticator_enrollment_policy_conditions_all_of_people_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


