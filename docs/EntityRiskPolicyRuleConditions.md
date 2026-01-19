# EntityRiskPolicyRuleConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_risk** | [**EntityRiskScorePolicyRuleCondition**](EntityRiskScorePolicyRuleCondition.md) |  | [optional] 
**people** | [**PolicyPeopleCondition**](PolicyPeopleCondition.md) |  | [optional] 
**risk_detection_types** | [**RiskDetectionTypesPolicyRuleCondition**](RiskDetectionTypesPolicyRuleCondition.md) |  | [optional] 

## Example

```python
from okta.models.entity_risk_policy_rule_conditions import EntityRiskPolicyRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskPolicyRuleConditions from a JSON string
entity_risk_policy_rule_conditions_instance = EntityRiskPolicyRuleConditions.from_json(json)
# print the JSON string representation of the object
print(EntityRiskPolicyRuleConditions.to_json())

# convert the object into a dict
entity_risk_policy_rule_conditions_dict = entity_risk_policy_rule_conditions_instance.to_dict()
# create an instance of EntityRiskPolicyRuleConditions from a dict
entity_risk_policy_rule_conditions_from_dict = EntityRiskPolicyRuleConditions.from_dict(entity_risk_policy_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


