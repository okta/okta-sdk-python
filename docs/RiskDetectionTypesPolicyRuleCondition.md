# RiskDetectionTypesPolicyRuleCondition

<x-lifecycle class=\"oie\"></x-lifecycle> An object that references detected risk events. This object can have an `include` parameter or an `exclude` parameter, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | [**List[DetectedRiskEvents]**](DetectedRiskEvents.md) | An array of detected risk events to exclude in the entity policy rule | 
**include** | [**List[DetectedRiskEvents]**](DetectedRiskEvents.md) | An array of detected risk events to include in the entity policy rule | 

## Example

```python
from okta.models.risk_detection_types_policy_rule_condition import RiskDetectionTypesPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RiskDetectionTypesPolicyRuleCondition from a JSON string
risk_detection_types_policy_rule_condition_instance = RiskDetectionTypesPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(RiskDetectionTypesPolicyRuleCondition.to_json())

# convert the object into a dict
risk_detection_types_policy_rule_condition_dict = risk_detection_types_policy_rule_condition_instance.to_dict()
# create an instance of RiskDetectionTypesPolicyRuleCondition from a dict
risk_detection_types_policy_rule_condition_from_dict = RiskDetectionTypesPolicyRuleCondition.from_dict(risk_detection_types_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


