# DevicePolicyRuleConditionPlatform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_mdm_frameworks** | [**List[DevicePolicyMDMFramework]**](DevicePolicyMDMFramework.md) |  | [optional] 
**types** | [**List[DevicePolicyPlatformType]**](DevicePolicyPlatformType.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_policy_rule_condition_platform import DevicePolicyRuleConditionPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePolicyRuleConditionPlatform from a JSON string
device_policy_rule_condition_platform_instance = DevicePolicyRuleConditionPlatform.from_json(json)
# print the JSON string representation of the object
print(DevicePolicyRuleConditionPlatform.to_json())

# convert the object into a dict
device_policy_rule_condition_platform_dict = device_policy_rule_condition_platform_instance.to_dict()
# create an instance of DevicePolicyRuleConditionPlatform from a dict
device_policy_rule_condition_platform_from_dict = DevicePolicyRuleConditionPlatform.from_dict(device_policy_rule_condition_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


