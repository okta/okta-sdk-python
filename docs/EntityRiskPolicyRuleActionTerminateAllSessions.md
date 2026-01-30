# EntityRiskPolicyRuleActionTerminateAllSessions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | This action revokes or terminates all of the user&#39;s active sessions. | [optional] 

## Example

```python
from okta.models.entity_risk_policy_rule_action_terminate_all_sessions import EntityRiskPolicyRuleActionTerminateAllSessions

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskPolicyRuleActionTerminateAllSessions from a JSON string
entity_risk_policy_rule_action_terminate_all_sessions_instance = EntityRiskPolicyRuleActionTerminateAllSessions.from_json(json)
# print the JSON string representation of the object
print(EntityRiskPolicyRuleActionTerminateAllSessions.to_json())

# convert the object into a dict
entity_risk_policy_rule_action_terminate_all_sessions_dict = entity_risk_policy_rule_action_terminate_all_sessions_instance.to_dict()
# create an instance of EntityRiskPolicyRuleActionTerminateAllSessions from a dict
entity_risk_policy_rule_action_terminate_all_sessions_from_dict = EntityRiskPolicyRuleActionTerminateAllSessions.from_dict(entity_risk_policy_rule_action_terminate_all_sessions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


