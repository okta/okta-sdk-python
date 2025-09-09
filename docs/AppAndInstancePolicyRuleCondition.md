# AppAndInstancePolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | [**List[AppAndInstanceConditionEvaluatorAppOrInstance]**](AppAndInstanceConditionEvaluatorAppOrInstance.md) |  | [optional] 
**include** | [**List[AppAndInstanceConditionEvaluatorAppOrInstance]**](AppAndInstanceConditionEvaluatorAppOrInstance.md) |  | [optional] 

## Example

```python
from okta.models.app_and_instance_policy_rule_condition import AppAndInstancePolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AppAndInstancePolicyRuleCondition from a JSON string
app_and_instance_policy_rule_condition_instance = AppAndInstancePolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(AppAndInstancePolicyRuleCondition.to_json())

# convert the object into a dict
app_and_instance_policy_rule_condition_dict = app_and_instance_policy_rule_condition_instance.to_dict()
# create an instance of AppAndInstancePolicyRuleCondition from a dict
app_and_instance_policy_rule_condition_from_dict = AppAndInstancePolicyRuleCondition.from_dict(app_and_instance_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


