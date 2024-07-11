# RiskPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behaviors** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.risk_policy_rule_condition import RiskPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RiskPolicyRuleCondition from a JSON string
risk_policy_rule_condition_instance = RiskPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(RiskPolicyRuleCondition.to_json())

# convert the object into a dict
risk_policy_rule_condition_dict = risk_policy_rule_condition_instance.to_dict()
# create an instance of RiskPolicyRuleCondition from a dict
risk_policy_rule_condition_from_dict = RiskPolicyRuleCondition.from_dict(risk_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


