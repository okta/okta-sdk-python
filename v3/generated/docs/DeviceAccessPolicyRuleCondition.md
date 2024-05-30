# DeviceAccessPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrated** | **bool** |  | [optional] 
**platform** | [**DevicePolicyRuleConditionPlatform**](DevicePolicyRuleConditionPlatform.md) |  | [optional] 
**rooted** | **bool** |  | [optional] 
**trust_level** | [**DevicePolicyTrustLevel**](DevicePolicyTrustLevel.md) |  | [optional] 
**managed** | **bool** |  | [optional] 
**registered** | **bool** |  | [optional] 
**assurance** | [**DevicePolicyRuleConditionAssurance**](DevicePolicyRuleConditionAssurance.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_access_policy_rule_condition import DeviceAccessPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAccessPolicyRuleCondition from a JSON string
device_access_policy_rule_condition_instance = DeviceAccessPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(DeviceAccessPolicyRuleCondition.to_json())

# convert the object into a dict
device_access_policy_rule_condition_dict = device_access_policy_rule_condition_instance.to_dict()
# create an instance of DeviceAccessPolicyRuleCondition from a dict
device_access_policy_rule_condition_form_dict = device_access_policy_rule_condition.from_dict(device_access_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


