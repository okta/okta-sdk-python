# PlatformPolicyRuleCondition

Specifies a particular platform or device to match on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | [**List[PlatformConditionEvaluatorPlatform]**](PlatformConditionEvaluatorPlatform.md) |  | [optional] 
**include** | [**List[PlatformConditionEvaluatorPlatform]**](PlatformConditionEvaluatorPlatform.md) |  | [optional] 

## Example

```python
from okta.models.platform_policy_rule_condition import PlatformPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformPolicyRuleCondition from a JSON string
platform_policy_rule_condition_instance = PlatformPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(PlatformPolicyRuleCondition.to_json())

# convert the object into a dict
platform_policy_rule_condition_dict = platform_policy_rule_condition_instance.to_dict()
# create an instance of PlatformPolicyRuleCondition from a dict
platform_policy_rule_condition_from_dict = PlatformPolicyRuleCondition.from_dict(platform_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


