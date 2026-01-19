# OktaSignOnPolicyRuleConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_context** | [**PolicyRuleAuthContextCondition**](PolicyRuleAuthContextCondition.md) |  | [optional] 
**identity_provider** | [**IdentityProviderPolicyRuleCondition**](IdentityProviderPolicyRuleCondition.md) |  | [optional] 
**network** | [**PolicyNetworkCondition**](PolicyNetworkCondition.md) |  | [optional] 
**people** | [**PolicyPeopleCondition**](PolicyPeopleCondition.md) |  | [optional] 

## Example

```python
from okta.models.okta_sign_on_policy_rule_conditions import OktaSignOnPolicyRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSignOnPolicyRuleConditions from a JSON string
okta_sign_on_policy_rule_conditions_instance = OktaSignOnPolicyRuleConditions.from_json(json)
# print the JSON string representation of the object
print(OktaSignOnPolicyRuleConditions.to_json())

# convert the object into a dict
okta_sign_on_policy_rule_conditions_dict = okta_sign_on_policy_rule_conditions_instance.to_dict()
# create an instance of OktaSignOnPolicyRuleConditions from a dict
okta_sign_on_policy_rule_conditions_from_dict = OktaSignOnPolicyRuleConditions.from_dict(okta_sign_on_policy_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


