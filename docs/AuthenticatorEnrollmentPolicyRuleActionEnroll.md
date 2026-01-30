# AuthenticatorEnrollmentPolicyRuleActionEnroll

Specifies whether the user is to be enrolled the first time they `LOGIN`, the next time they are in the `CHALLENGE` process, or `NEVER`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_rule_action_enroll import AuthenticatorEnrollmentPolicyRuleActionEnroll

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyRuleActionEnroll from a JSON string
authenticator_enrollment_policy_rule_action_enroll_instance = AuthenticatorEnrollmentPolicyRuleActionEnroll.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyRuleActionEnroll.to_json())

# convert the object into a dict
authenticator_enrollment_policy_rule_action_enroll_dict = authenticator_enrollment_policy_rule_action_enroll_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyRuleActionEnroll from a dict
authenticator_enrollment_policy_rule_action_enroll_from_dict = AuthenticatorEnrollmentPolicyRuleActionEnroll.from_dict(authenticator_enrollment_policy_rule_action_enroll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


