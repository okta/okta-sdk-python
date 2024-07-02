# IdpPolicyRuleActionIdp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[IdpPolicyRuleActionProvider]**](IdpPolicyRuleActionProvider.md) | List of configured Identity Providers that a given Rule can route to. Ability to define multiple providers is a part of the Okta Identity Engine. This allows users to choose a Provider when they sign in. Contact support for information on the Identity Engine. | [optional] 
**idp_selection_type** | [**IdpSelectionType**](IdpSelectionType.md) |  | [optional] 
**match_criteria** | [**List[IdpPolicyRuleActionMatchCriteria]**](IdpPolicyRuleActionMatchCriteria.md) | Required if &#x60;idpSelectionType&#x60; is set to &#x60;DYNAMIC&#x60; | [optional] 

## Example

```python
from openapi_client.models.idp_policy_rule_action_idp import IdpPolicyRuleActionIdp

# TODO update the JSON string below
json = "{}"
# create an instance of IdpPolicyRuleActionIdp from a JSON string
idp_policy_rule_action_idp_instance = IdpPolicyRuleActionIdp.from_json(json)
# print the JSON string representation of the object
print(IdpPolicyRuleActionIdp.to_json())

# convert the object into a dict
idp_policy_rule_action_idp_dict = idp_policy_rule_action_idp_instance.to_dict()
# create an instance of IdpPolicyRuleActionIdp from a dict
idp_policy_rule_action_idp_from_dict = IdpPolicyRuleActionIdp.from_dict(idp_policy_rule_action_idp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


