# EntityRiskPolicyRuleAllOfActions

The action to take based on the risk event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_risk** | [**EntityRiskPolicyRuleAllOfActionsEntityRisk**](EntityRiskPolicyRuleAllOfActionsEntityRisk.md) |  | [optional] 

## Example

```python
from okta.models.entity_risk_policy_rule_all_of_actions import EntityRiskPolicyRuleAllOfActions

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskPolicyRuleAllOfActions from a JSON string
entity_risk_policy_rule_all_of_actions_instance = EntityRiskPolicyRuleAllOfActions.from_json(json)
# print the JSON string representation of the object
print(EntityRiskPolicyRuleAllOfActions.to_json())

# convert the object into a dict
entity_risk_policy_rule_all_of_actions_dict = entity_risk_policy_rule_all_of_actions_instance.to_dict()
# create an instance of EntityRiskPolicyRuleAllOfActions from a dict
entity_risk_policy_rule_all_of_actions_from_dict = EntityRiskPolicyRuleAllOfActions.from_dict(entity_risk_policy_rule_all_of_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


