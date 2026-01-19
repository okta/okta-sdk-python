# OktaSignOnPolicyRuleSignonActions

Specifies settings for the policy rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | Indicates if a user is allowed to sign in | [optional] 
**factor_lifetime** | **int** | Interval of time that must elapse before the user is challenged for MFA, if the factor prompt mode is set to &#x60;SESSION&#x60;  &gt; **Note:** Required only if &#x60;requireFactor&#x60; is &#x60;true&#x60;.  | [optional] 
**factor_prompt_mode** | [**OktaSignOnPolicyFactorPromptMode**](OktaSignOnPolicyFactorPromptMode.md) |  | [optional] 
**primary_factor** | [**OktaSignOnPolicyRuleSignonPrimaryFactor**](OktaSignOnPolicyRuleSignonPrimaryFactor.md) |  | [optional] 
**remember_device_by_default** | **bool** | Indicates if Okta should automatically remember the device | [optional] [default to False]
**require_factor** | **bool** | Indicates if multifactor authentication is required | [optional] [default to False]
**session** | [**OktaSignOnPolicyRuleSignonSessionActions**](OktaSignOnPolicyRuleSignonSessionActions.md) |  | [optional] 

## Example

```python
from okta.models.okta_sign_on_policy_rule_signon_actions import OktaSignOnPolicyRuleSignonActions

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSignOnPolicyRuleSignonActions from a JSON string
okta_sign_on_policy_rule_signon_actions_instance = OktaSignOnPolicyRuleSignonActions.from_json(json)
# print the JSON string representation of the object
print(OktaSignOnPolicyRuleSignonActions.to_json())

# convert the object into a dict
okta_sign_on_policy_rule_signon_actions_dict = okta_sign_on_policy_rule_signon_actions_instance.to_dict()
# create an instance of OktaSignOnPolicyRuleSignonActions from a dict
okta_sign_on_policy_rule_signon_actions_from_dict = OktaSignOnPolicyRuleSignonActions.from_dict(okta_sign_on_policy_rule_signon_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


