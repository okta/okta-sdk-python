# IdpDiscoveryPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**IdpPolicyRuleAction**](IdpPolicyRuleAction.md) |  | [optional] 
**conditions** | [**IdpDiscoveryPolicyRuleCondition**](IdpDiscoveryPolicyRuleCondition.md) |  | [optional] 

## Example

```python
from openapi_client.models.idp_discovery_policy_rule import IdpDiscoveryPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of IdpDiscoveryPolicyRule from a JSON string
idp_discovery_policy_rule_instance = IdpDiscoveryPolicyRule.from_json(json)
# print the JSON string representation of the object
print(IdpDiscoveryPolicyRule.to_json())

# convert the object into a dict
idp_discovery_policy_rule_dict = idp_discovery_policy_rule_instance.to_dict()
# create an instance of IdpDiscoveryPolicyRule from a dict
idp_discovery_policy_rule_from_dict = IdpDiscoveryPolicyRule.from_dict(idp_discovery_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


