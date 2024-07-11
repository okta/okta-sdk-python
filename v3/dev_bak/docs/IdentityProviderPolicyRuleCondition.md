# IdentityProviderPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp_ids** | **List[str]** |  | [optional] 
**provider** | [**IdentityProviderPolicyProvider**](IdentityProviderPolicyProvider.md) |  | [optional] 

## Example

```python
from openapi_client.models.identity_provider_policy_rule_condition import IdentityProviderPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderPolicyRuleCondition from a JSON string
identity_provider_policy_rule_condition_instance = IdentityProviderPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderPolicyRuleCondition.to_json())

# convert the object into a dict
identity_provider_policy_rule_condition_dict = identity_provider_policy_rule_condition_instance.to_dict()
# create an instance of IdentityProviderPolicyRuleCondition from a dict
identity_provider_policy_rule_condition_from_dict = IdentityProviderPolicyRuleCondition.from_dict(identity_provider_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


