# PostAuthSessionPolicyRuleRunWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**workflow** | [**EntityRiskPolicyRuleActionRunWorkflowWorkflow**](EntityRiskPolicyRuleActionRunWorkflowWorkflow.md) |  | [optional] 

## Example

```python
from okta.models.post_auth_session_policy_rule_run_workflow import PostAuthSessionPolicyRuleRunWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthSessionPolicyRuleRunWorkflow from a JSON string
post_auth_session_policy_rule_run_workflow_instance = PostAuthSessionPolicyRuleRunWorkflow.from_json(json)
# print the JSON string representation of the object
print(PostAuthSessionPolicyRuleRunWorkflow.to_json())

# convert the object into a dict
post_auth_session_policy_rule_run_workflow_dict = post_auth_session_policy_rule_run_workflow_instance.to_dict()
# create an instance of PostAuthSessionPolicyRuleRunWorkflow from a dict
post_auth_session_policy_rule_run_workflow_from_dict = PostAuthSessionPolicyRuleRunWorkflow.from_dict(post_auth_session_policy_rule_run_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


