# AccessPolicyRuleConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**DeviceAccessPolicyRuleCondition**](DeviceAccessPolicyRuleCondition.md) |  | [optional] 
**el_condition** | [**AccessPolicyRuleCustomCondition**](AccessPolicyRuleCustomCondition.md) |  | [optional] 
**network** | [**PolicyNetworkCondition**](PolicyNetworkCondition.md) |  | [optional] 
**people** | [**PolicyPeopleCondition**](PolicyPeopleCondition.md) |  | [optional] 
**platform** | [**PlatformPolicyRuleCondition**](PlatformPolicyRuleCondition.md) |  | [optional] 
**risk_score** | [**RiskScorePolicyRuleCondition**](RiskScorePolicyRuleCondition.md) |  | [optional] 
**user_type** | [**UserTypeCondition**](UserTypeCondition.md) |  | [optional] 

## Example

```python
from okta.models.access_policy_rule_conditions import AccessPolicyRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyRuleConditions from a JSON string
access_policy_rule_conditions_instance = AccessPolicyRuleConditions.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyRuleConditions.to_json())

# convert the object into a dict
access_policy_rule_conditions_dict = access_policy_rule_conditions_instance.to_dict()
# create an instance of AccessPolicyRuleConditions from a dict
access_policy_rule_conditions_from_dict = AccessPolicyRuleConditions.from_dict(access_policy_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


