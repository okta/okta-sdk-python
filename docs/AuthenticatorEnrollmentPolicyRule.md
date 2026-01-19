# AuthenticatorEnrollmentPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**AuthenticatorEnrollmentPolicyRuleActions**](AuthenticatorEnrollmentPolicyRuleActions.md) |  | [optional] 
**conditions** | [**AuthenticatorEnrollmentPolicyRuleConditions**](AuthenticatorEnrollmentPolicyRuleConditions.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_rule import AuthenticatorEnrollmentPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyRule from a JSON string
authenticator_enrollment_policy_rule_instance = AuthenticatorEnrollmentPolicyRule.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyRule.to_json())

# convert the object into a dict
authenticator_enrollment_policy_rule_dict = authenticator_enrollment_policy_rule_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyRule from a dict
authenticator_enrollment_policy_rule_from_dict = AuthenticatorEnrollmentPolicyRule.from_dict(authenticator_enrollment_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


