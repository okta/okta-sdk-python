# OktaSignOnPolicyRuleSignonSessionActions

Properties governing the user's session lifetime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_session_idle_minutes** | **int** | Maximum number of minutes that a user session can be idle before the session is ended | [optional] [default to 120]
**max_session_lifetime_minutes** | **int** | Maximum number of minutes (from when the user signs in) that a user&#39;s session is active. Set this to force users to sign in again after the number of specified minutes. Disable by setting to &#x60;0&#x60;. | [optional] [default to 0]
**use_persistent_cookie** | **bool** | If set to &#x60;false&#x60;, user session cookies only last the length of a browser session. If set to &#x60;true&#x60;, user session cookies last across browser sessions. This setting doesn&#39;t impact administrators who can never have persistent session cookies. This property is read-only for the default rule of the default global session policy. | [optional] [default to False]

## Example

```python
from okta.models.okta_sign_on_policy_rule_signon_session_actions import OktaSignOnPolicyRuleSignonSessionActions

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSignOnPolicyRuleSignonSessionActions from a JSON string
okta_sign_on_policy_rule_signon_session_actions_instance = OktaSignOnPolicyRuleSignonSessionActions.from_json(json)
# print the JSON string representation of the object
print(OktaSignOnPolicyRuleSignonSessionActions.to_json())

# convert the object into a dict
okta_sign_on_policy_rule_signon_session_actions_dict = okta_sign_on_policy_rule_signon_session_actions_instance.to_dict()
# create an instance of OktaSignOnPolicyRuleSignonSessionActions from a dict
okta_sign_on_policy_rule_signon_session_actions_from_dict = OktaSignOnPolicyRuleSignonSessionActions.from_dict(okta_sign_on_policy_rule_signon_session_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


