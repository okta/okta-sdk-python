# IdpPolicyRuleActionProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | IdP types of &#x60;OKTA&#x60;, &#x60;AgentlessDSSO&#x60;, and &#x60;IWA&#x60; don&#39;t require an ID. | [optional] 
**name** | **str** | Provider &#x60;name&#x60; in Okta. Optional. Supported in &#x60;IDENTITY ENGINE&#x60;. | [optional] 
**type** | [**IdentityProviderType**](IdentityProviderType.md) |  | [optional] 

## Example

```python
from openapi_client.models.idp_policy_rule_action_provider import IdpPolicyRuleActionProvider

# TODO update the JSON string below
json = "{}"
# create an instance of IdpPolicyRuleActionProvider from a JSON string
idp_policy_rule_action_provider_instance = IdpPolicyRuleActionProvider.from_json(json)
# print the JSON string representation of the object
print(IdpPolicyRuleActionProvider.to_json())

# convert the object into a dict
idp_policy_rule_action_provider_dict = idp_policy_rule_action_provider_instance.to_dict()
# create an instance of IdpPolicyRuleActionProvider from a dict
idp_policy_rule_action_provider_form_dict = idp_policy_rule_action_provider.from_dict(idp_policy_rule_action_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


