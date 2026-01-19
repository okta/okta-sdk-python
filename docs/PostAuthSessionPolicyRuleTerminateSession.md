# PostAuthSessionPolicyRuleTerminateSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to take when the session protection policy detects a failure. | [optional] 

## Example

```python
from okta.models.post_auth_session_policy_rule_terminate_session import PostAuthSessionPolicyRuleTerminateSession

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthSessionPolicyRuleTerminateSession from a JSON string
post_auth_session_policy_rule_terminate_session_instance = PostAuthSessionPolicyRuleTerminateSession.from_json(json)
# print the JSON string representation of the object
print(PostAuthSessionPolicyRuleTerminateSession.to_json())

# convert the object into a dict
post_auth_session_policy_rule_terminate_session_dict = post_auth_session_policy_rule_terminate_session_instance.to_dict()
# create an instance of PostAuthSessionPolicyRuleTerminateSession from a dict
post_auth_session_policy_rule_terminate_session_from_dict = PostAuthSessionPolicyRuleTerminateSession.from_dict(post_auth_session_policy_rule_terminate_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


