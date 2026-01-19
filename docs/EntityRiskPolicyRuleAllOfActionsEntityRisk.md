# EntityRiskPolicyRuleAllOfActionsEntityRisk

The object that contains the `actions` array

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[EntityRiskPolicyRuleActionsObject]**](EntityRiskPolicyRuleActionsObject.md) | The &#x60;entityRisk&#x60; object&#39;s &#x60;actions&#x60; array can be empty or contain one of two &#x60;action&#x60; object value pairs. This object determines the specific response to a risk event. | [optional] 

## Example

```python
from okta.models.entity_risk_policy_rule_all_of_actions_entity_risk import EntityRiskPolicyRuleAllOfActionsEntityRisk

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskPolicyRuleAllOfActionsEntityRisk from a JSON string
entity_risk_policy_rule_all_of_actions_entity_risk_instance = EntityRiskPolicyRuleAllOfActionsEntityRisk.from_json(json)
# print the JSON string representation of the object
print(EntityRiskPolicyRuleAllOfActionsEntityRisk.to_json())

# convert the object into a dict
entity_risk_policy_rule_all_of_actions_entity_risk_dict = entity_risk_policy_rule_all_of_actions_entity_risk_instance.to_dict()
# create an instance of EntityRiskPolicyRuleAllOfActionsEntityRisk from a dict
entity_risk_policy_rule_all_of_actions_entity_risk_from_dict = EntityRiskPolicyRuleAllOfActionsEntityRisk.from_dict(entity_risk_policy_rule_all_of_actions_entity_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


