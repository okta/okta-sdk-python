# AuthenticatorEnrollmentPolicyRuleConditionsPeople

Identifies users and groups that are used together

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers**](AuthenticatorEnrollmentPolicyRuleConditionsPeopleUsers.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_rule_conditions_people import AuthenticatorEnrollmentPolicyRuleConditionsPeople

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyRuleConditionsPeople from a JSON string
authenticator_enrollment_policy_rule_conditions_people_instance = AuthenticatorEnrollmentPolicyRuleConditionsPeople.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyRuleConditionsPeople.to_json())

# convert the object into a dict
authenticator_enrollment_policy_rule_conditions_people_dict = authenticator_enrollment_policy_rule_conditions_people_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyRuleConditionsPeople from a dict
authenticator_enrollment_policy_rule_conditions_people_from_dict = AuthenticatorEnrollmentPolicyRuleConditionsPeople.from_dict(authenticator_enrollment_policy_rule_conditions_people_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


