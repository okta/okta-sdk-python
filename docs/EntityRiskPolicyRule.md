# EntityRiskPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**EntityRiskPolicyRuleAllOfActions**](EntityRiskPolicyRuleAllOfActions.md) |  | [optional] 
**conditions** | [**EntityRiskPolicyRuleConditions**](EntityRiskPolicyRuleConditions.md) |  | [optional] 

## Example

```python
from okta.models.entity_risk_policy_rule import EntityRiskPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskPolicyRule from a JSON string
entity_risk_policy_rule_instance = EntityRiskPolicyRule.from_json(json)
# print the JSON string representation of the object
print(EntityRiskPolicyRule.to_json())

# convert the object into a dict
entity_risk_policy_rule_dict = entity_risk_policy_rule_instance.to_dict()
# create an instance of EntityRiskPolicyRule from a dict
entity_risk_policy_rule_from_dict = EntityRiskPolicyRule.from_dict(entity_risk_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


