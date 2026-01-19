# AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers

Specifies a set of users to be included or excluded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Users to be excluded | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_rule_conditions_people_users import AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers from a JSON string
authenticator_enrollment_policy_rule_conditions_people_users_instance = AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers.to_json())

# convert the object into a dict
authenticator_enrollment_policy_rule_conditions_people_users_dict = authenticator_enrollment_policy_rule_conditions_people_users_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers from a dict
authenticator_enrollment_policy_rule_conditions_people_users_from_dict = AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers.from_dict(authenticator_enrollment_policy_rule_conditions_people_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


