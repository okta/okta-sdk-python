# PostAuthSessionPolicyRuleAllOfActionsPostAuthSession

This object contains a `failureActions` array that defines the specific action to take when the session protection policy detects a failure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_actions** | [**List[PostAuthSessionFailureActionsObject]**](PostAuthSessionFailureActionsObject.md) | An array of objects that define the action. It can be empty or contain two &#x60;action&#x60; value pairs. | [optional] 

## Example

```python
from okta.models.post_auth_session_policy_rule_all_of_actions_post_auth_session import PostAuthSessionPolicyRuleAllOfActionsPostAuthSession

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthSessionPolicyRuleAllOfActionsPostAuthSession from a JSON string
post_auth_session_policy_rule_all_of_actions_post_auth_session_instance = PostAuthSessionPolicyRuleAllOfActionsPostAuthSession.from_json(json)
# print the JSON string representation of the object
print(PostAuthSessionPolicyRuleAllOfActionsPostAuthSession.to_json())

# convert the object into a dict
post_auth_session_policy_rule_all_of_actions_post_auth_session_dict = post_auth_session_policy_rule_all_of_actions_post_auth_session_instance.to_dict()
# create an instance of PostAuthSessionPolicyRuleAllOfActionsPostAuthSession from a dict
post_auth_session_policy_rule_all_of_actions_post_auth_session_from_dict = PostAuthSessionPolicyRuleAllOfActionsPostAuthSession.from_dict(post_auth_session_policy_rule_all_of_actions_post_auth_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


