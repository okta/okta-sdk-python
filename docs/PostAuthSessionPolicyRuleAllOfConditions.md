# PostAuthSessionPolicyRuleAllOfConditions

Specifies conditions that must be met during policy evaluation to apply the rule. All policy conditions and conditions for at least one rule must be met to apply the settings specified in the policy and the associated rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**people** | [**PolicyPeopleCondition**](PolicyPeopleCondition.md) |  | [optional] 

## Example

```python
from okta.models.post_auth_session_policy_rule_all_of_conditions import PostAuthSessionPolicyRuleAllOfConditions

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthSessionPolicyRuleAllOfConditions from a JSON string
post_auth_session_policy_rule_all_of_conditions_instance = PostAuthSessionPolicyRuleAllOfConditions.from_json(json)
# print the JSON string representation of the object
print(PostAuthSessionPolicyRuleAllOfConditions.to_json())

# convert the object into a dict
post_auth_session_policy_rule_all_of_conditions_dict = post_auth_session_policy_rule_all_of_conditions_instance.to_dict()
# create an instance of PostAuthSessionPolicyRuleAllOfConditions from a dict
post_auth_session_policy_rule_all_of_conditions_from_dict = PostAuthSessionPolicyRuleAllOfConditions.from_dict(post_auth_session_policy_rule_all_of_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


