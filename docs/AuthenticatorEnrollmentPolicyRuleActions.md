# AuthenticatorEnrollmentPolicyRuleActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enroll** | [**AuthenticatorEnrollmentPolicyRuleActionEnroll**](AuthenticatorEnrollmentPolicyRuleActionEnroll.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_rule_actions import AuthenticatorEnrollmentPolicyRuleActions

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyRuleActions from a JSON string
authenticator_enrollment_policy_rule_actions_instance = AuthenticatorEnrollmentPolicyRuleActions.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyRuleActions.to_json())

# convert the object into a dict
authenticator_enrollment_policy_rule_actions_dict = authenticator_enrollment_policy_rule_actions_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyRuleActions from a dict
authenticator_enrollment_policy_rule_actions_from_dict = AuthenticatorEnrollmentPolicyRuleActions.from_dict(authenticator_enrollment_policy_rule_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


