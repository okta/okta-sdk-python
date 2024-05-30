# DevicePolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrated** | **bool** |  | [optional] 
**platform** | [**DevicePolicyRuleConditionPlatform**](DevicePolicyRuleConditionPlatform.md) |  | [optional] 
**rooted** | **bool** |  | [optional] 
**trust_level** | [**DevicePolicyTrustLevel**](DevicePolicyTrustLevel.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_policy_rule_condition import DevicePolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePolicyRuleCondition from a JSON string
device_policy_rule_condition_instance = DevicePolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(DevicePolicyRuleCondition.to_json())

# convert the object into a dict
device_policy_rule_condition_dict = device_policy_rule_condition_instance.to_dict()
# create an instance of DevicePolicyRuleCondition from a dict
device_policy_rule_condition_form_dict = device_policy_rule_condition.from_dict(device_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


