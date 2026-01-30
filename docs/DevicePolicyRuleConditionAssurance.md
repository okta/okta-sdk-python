# DevicePolicyRuleConditionAssurance

Specifies [device assurance policies](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/DeviceAssurance/) in the policy rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Specifies the device assurance policy ID | [optional] 

## Example

```python
from okta.models.device_policy_rule_condition_assurance import DevicePolicyRuleConditionAssurance

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePolicyRuleConditionAssurance from a JSON string
device_policy_rule_condition_assurance_instance = DevicePolicyRuleConditionAssurance.from_json(json)
# print the JSON string representation of the object
print(DevicePolicyRuleConditionAssurance.to_json())

# convert the object into a dict
device_policy_rule_condition_assurance_dict = device_policy_rule_condition_assurance_instance.to_dict()
# create an instance of DevicePolicyRuleConditionAssurance from a dict
device_policy_rule_condition_assurance_from_dict = DevicePolicyRuleConditionAssurance.from_dict(device_policy_rule_condition_assurance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


