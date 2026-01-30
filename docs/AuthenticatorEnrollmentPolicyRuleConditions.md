# AuthenticatorEnrollmentPolicyRuleConditions

Specifies conditions that must be met during policy evaluation to apply the rule. All policy conditions and conditions for at least one rule must be met to apply the settings specified in the policy and the associated rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**PolicyNetworkCondition**](PolicyNetworkCondition.md) |  | [optional] 
**people** | [**AuthenticatorEnrollmentPolicyRuleConditionsPeople**](AuthenticatorEnrollmentPolicyRuleConditionsPeople.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_rule_conditions import AuthenticatorEnrollmentPolicyRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyRuleConditions from a JSON string
authenticator_enrollment_policy_rule_conditions_instance = AuthenticatorEnrollmentPolicyRuleConditions.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyRuleConditions.to_json())

# convert the object into a dict
authenticator_enrollment_policy_rule_conditions_dict = authenticator_enrollment_policy_rule_conditions_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyRuleConditions from a dict
authenticator_enrollment_policy_rule_conditions_from_dict = AuthenticatorEnrollmentPolicyRuleConditions.from_dict(authenticator_enrollment_policy_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


