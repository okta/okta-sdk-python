# EntityRiskPolicyRuleActionRunWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**workflow** | [**EntityRiskPolicyRuleActionRunWorkflowWorkflow**](EntityRiskPolicyRuleActionRunWorkflowWorkflow.md) |  | [optional] 

## Example

```python
from okta.models.entity_risk_policy_rule_action_run_workflow import EntityRiskPolicyRuleActionRunWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskPolicyRuleActionRunWorkflow from a JSON string
entity_risk_policy_rule_action_run_workflow_instance = EntityRiskPolicyRuleActionRunWorkflow.from_json(json)
# print the JSON string representation of the object
print(EntityRiskPolicyRuleActionRunWorkflow.to_json())

# convert the object into a dict
entity_risk_policy_rule_action_run_workflow_dict = entity_risk_policy_rule_action_run_workflow_instance.to_dict()
# create an instance of EntityRiskPolicyRuleActionRunWorkflow from a dict
entity_risk_policy_rule_action_run_workflow_from_dict = EntityRiskPolicyRuleActionRunWorkflow.from_dict(entity_risk_policy_rule_action_run_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


