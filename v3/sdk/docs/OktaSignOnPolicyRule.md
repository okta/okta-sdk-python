# OktaSignOnPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**OktaSignOnPolicyRuleActions**](OktaSignOnPolicyRuleActions.md) |  | [optional] 
**conditions** | [**OktaSignOnPolicyRuleConditions**](OktaSignOnPolicyRuleConditions.md) |  | [optional] 

## Example

```python
from okta.models.okta_sign_on_policy_rule import OktaSignOnPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSignOnPolicyRule from a JSON string
okta_sign_on_policy_rule_instance = OktaSignOnPolicyRule.from_json(json)
# print the JSON string representation of the object
print(OktaSignOnPolicyRule.to_json())

# convert the object into a dict
okta_sign_on_policy_rule_dict = okta_sign_on_policy_rule_instance.to_dict()
# create an instance of OktaSignOnPolicyRule from a dict
okta_sign_on_policy_rule_from_dict = OktaSignOnPolicyRule.from_dict(okta_sign_on_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


