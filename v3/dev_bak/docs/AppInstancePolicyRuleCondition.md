# AppInstancePolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** |  | [optional] 
**include** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.app_instance_policy_rule_condition import AppInstancePolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstancePolicyRuleCondition from a JSON string
app_instance_policy_rule_condition_instance = AppInstancePolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(AppInstancePolicyRuleCondition.to_json())

# convert the object into a dict
app_instance_policy_rule_condition_dict = app_instance_policy_rule_condition_instance.to_dict()
# create an instance of AppInstancePolicyRuleCondition from a dict
app_instance_policy_rule_condition_from_dict = AppInstancePolicyRuleCondition.from_dict(app_instance_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


