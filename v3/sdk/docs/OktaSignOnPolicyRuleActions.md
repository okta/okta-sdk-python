# OktaSignOnPolicyRuleActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signon** | [**OktaSignOnPolicyRuleSignonActions**](OktaSignOnPolicyRuleSignonActions.md) |  | [optional] 

## Example

```python
from okta.models.okta_sign_on_policy_rule_actions import OktaSignOnPolicyRuleActions

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSignOnPolicyRuleActions from a JSON string
okta_sign_on_policy_rule_actions_instance = OktaSignOnPolicyRuleActions.from_json(json)
# print the JSON string representation of the object
print(OktaSignOnPolicyRuleActions.to_json())

# convert the object into a dict
okta_sign_on_policy_rule_actions_dict = okta_sign_on_policy_rule_actions_instance.to_dict()
# create an instance of OktaSignOnPolicyRuleActions from a dict
okta_sign_on_policy_rule_actions_from_dict = OktaSignOnPolicyRuleActions.from_dict(okta_sign_on_policy_rule_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


