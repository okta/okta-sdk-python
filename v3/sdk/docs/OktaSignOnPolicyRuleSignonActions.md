# OktaSignOnPolicyRuleSignonActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**PolicyAccess**](PolicyAccess.md) |  | [optional] 
**factor_lifetime** | **int** |  | [optional] 
**factor_prompt_mode** | [**OktaSignOnPolicyFactorPromptMode**](OktaSignOnPolicyFactorPromptMode.md) |  | [optional] 
**remember_device_by_default** | **bool** |  | [optional] [default to False]
**require_factor** | **bool** |  | [optional] [default to False]
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


