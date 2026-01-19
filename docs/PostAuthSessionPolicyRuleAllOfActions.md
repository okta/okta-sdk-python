# PostAuthSessionPolicyRuleAllOfActions

The action to take in response to a failure of the reevaluated global session policy or authentication polices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_auth_session** | [**PostAuthSessionPolicyRuleAllOfActionsPostAuthSession**](PostAuthSessionPolicyRuleAllOfActionsPostAuthSession.md) |  | [optional] 

## Example

```python
from okta.models.post_auth_session_policy_rule_all_of_actions import PostAuthSessionPolicyRuleAllOfActions

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthSessionPolicyRuleAllOfActions from a JSON string
post_auth_session_policy_rule_all_of_actions_instance = PostAuthSessionPolicyRuleAllOfActions.from_json(json)
# print the JSON string representation of the object
print(PostAuthSessionPolicyRuleAllOfActions.to_json())

# convert the object into a dict
post_auth_session_policy_rule_all_of_actions_dict = post_auth_session_policy_rule_all_of_actions_instance.to_dict()
# create an instance of PostAuthSessionPolicyRuleAllOfActions from a dict
post_auth_session_policy_rule_all_of_actions_from_dict = PostAuthSessionPolicyRuleAllOfActions.from_dict(post_auth_session_policy_rule_all_of_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


