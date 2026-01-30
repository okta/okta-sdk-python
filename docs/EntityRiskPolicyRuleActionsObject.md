# EntityRiskPolicyRuleActionsObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 

## Example

```python
from okta.models.entity_risk_policy_rule_actions_object import EntityRiskPolicyRuleActionsObject

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskPolicyRuleActionsObject from a JSON string
entity_risk_policy_rule_actions_object_instance = EntityRiskPolicyRuleActionsObject.from_json(json)
# print the JSON string representation of the object
print(EntityRiskPolicyRuleActionsObject.to_json())

# convert the object into a dict
entity_risk_policy_rule_actions_object_dict = entity_risk_policy_rule_actions_object_instance.to_dict()
# create an instance of EntityRiskPolicyRuleActionsObject from a dict
entity_risk_policy_rule_actions_object_from_dict = EntityRiskPolicyRuleActionsObject.from_dict(entity_risk_policy_rule_actions_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


