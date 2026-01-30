# EntityRiskScorePolicyRuleCondition

<x-lifecycle class=\"oie\"></x-lifecycle> The risk score level of the entity risk policy rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | 

## Example

```python
from okta.models.entity_risk_score_policy_rule_condition import EntityRiskScorePolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskScorePolicyRuleCondition from a JSON string
entity_risk_score_policy_rule_condition_instance = EntityRiskScorePolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(EntityRiskScorePolicyRuleCondition.to_json())

# convert the object into a dict
entity_risk_score_policy_rule_condition_dict = entity_risk_score_policy_rule_condition_instance.to_dict()
# create an instance of EntityRiskScorePolicyRuleCondition from a dict
entity_risk_score_policy_rule_condition_from_dict = EntityRiskScorePolicyRuleCondition.from_dict(entity_risk_score_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


