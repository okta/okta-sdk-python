# DeviceAccessPolicyRuleCondition

<x-lifecycle class=\"oie\"></x-lifecycle> Specifies the device condition to match on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assurance** | [**DevicePolicyRuleConditionAssurance**](DevicePolicyRuleConditionAssurance.md) |  | [optional] 
**managed** | **bool** | Indicates if the device is managed. A device is considered managed if it&#39;s part of a device management system. | [optional] 
**registered** | **bool** | Indicates if the device is registered. A device is registered if the User enrolls with Okta Verify that&#39;s installed on the device. When the &#x60;managed&#x60; property is passed, you must also include the &#x60;registered&#x60; property and set it to &#x60;true&#x60;.  | [optional] 

## Example

```python
from okta.models.device_access_policy_rule_condition import DeviceAccessPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAccessPolicyRuleCondition from a JSON string
device_access_policy_rule_condition_instance = DeviceAccessPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(DeviceAccessPolicyRuleCondition.to_json())

# convert the object into a dict
device_access_policy_rule_condition_dict = device_access_policy_rule_condition_instance.to_dict()
# create an instance of DeviceAccessPolicyRuleCondition from a dict
device_access_policy_rule_condition_from_dict = DeviceAccessPolicyRuleCondition.from_dict(device_access_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


