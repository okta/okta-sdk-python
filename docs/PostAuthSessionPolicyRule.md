# PostAuthSessionPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**PostAuthSessionPolicyRuleAllOfActions**](PostAuthSessionPolicyRuleAllOfActions.md) |  | [optional] 
**conditions** | [**PostAuthSessionPolicyRuleAllOfConditions**](PostAuthSessionPolicyRuleAllOfConditions.md) |  | [optional] 

## Example

```python
from okta.models.post_auth_session_policy_rule import PostAuthSessionPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthSessionPolicyRule from a JSON string
post_auth_session_policy_rule_instance = PostAuthSessionPolicyRule.from_json(json)
# print the JSON string representation of the object
print(PostAuthSessionPolicyRule.to_json())

# convert the object into a dict
post_auth_session_policy_rule_dict = post_auth_session_policy_rule_instance.to_dict()
# create an instance of PostAuthSessionPolicyRule from a dict
post_auth_session_policy_rule_from_dict = PostAuthSessionPolicyRule.from_dict(post_auth_session_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


