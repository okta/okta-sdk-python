# IdpDiscoveryPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**AppAndInstancePolicyRuleCondition**](AppAndInstancePolicyRuleCondition.md) |  | [optional] 
**network** | [**PolicyNetworkCondition**](PolicyNetworkCondition.md) |  | [optional] 
**user_identifier** | [**UserIdentifierPolicyRuleCondition**](UserIdentifierPolicyRuleCondition.md) |  | [optional] 
**platform** | [**PlatformPolicyRuleCondition**](PlatformPolicyRuleCondition.md) |  | [optional] 

## Example

```python
from openapi_client.models.idp_discovery_policy_rule_condition import IdpDiscoveryPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of IdpDiscoveryPolicyRuleCondition from a JSON string
idp_discovery_policy_rule_condition_instance = IdpDiscoveryPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(IdpDiscoveryPolicyRuleCondition.to_json())

# convert the object into a dict
idp_discovery_policy_rule_condition_dict = idp_discovery_policy_rule_condition_instance.to_dict()
# create an instance of IdpDiscoveryPolicyRuleCondition from a dict
idp_discovery_policy_rule_condition_from_dict = IdpDiscoveryPolicyRuleCondition.from_dict(idp_discovery_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


