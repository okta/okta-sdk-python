# OktaSignOnPolicyRuleSignonSessionActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_session_idle_minutes** | **int** |  | [optional] 
**max_session_lifetime_minutes** | **int** |  | [optional] 
**use_persistent_cookie** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.okta_sign_on_policy_rule_signon_session_actions import OktaSignOnPolicyRuleSignonSessionActions

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSignOnPolicyRuleSignonSessionActions from a JSON string
okta_sign_on_policy_rule_signon_session_actions_instance = OktaSignOnPolicyRuleSignonSessionActions.from_json(json)
# print the JSON string representation of the object
print(OktaSignOnPolicyRuleSignonSessionActions.to_json())

# convert the object into a dict
okta_sign_on_policy_rule_signon_session_actions_dict = okta_sign_on_policy_rule_signon_session_actions_instance.to_dict()
# create an instance of OktaSignOnPolicyRuleSignonSessionActions from a dict
okta_sign_on_policy_rule_signon_session_actions_form_dict = okta_sign_on_policy_rule_signon_session_actions.from_dict(okta_sign_on_policy_rule_signon_session_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


