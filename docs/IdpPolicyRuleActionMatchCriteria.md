# IdpPolicyRuleActionMatchCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | The IdP property that the evaluated string should match to | [optional] 
**provider_expression** | **str** | You can provide an Okta Expression Language expression with the Login Context that&#39;s evaluated with the IdP. For example, the value &#x60;login.identifier&#x60; refers to the user&#39;s username. If the user is signing in with the username &#x60;john.doe@mycompany.com&#x60;, the expression &#x60;login.identifier.substringAfter(@))&#x60; is evaluated to the domain name of the user, for example: &#x60;mycompany.com&#x60;.  | [optional] 

## Example

```python
from okta.models.idp_policy_rule_action_match_criteria import IdpPolicyRuleActionMatchCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of IdpPolicyRuleActionMatchCriteria from a JSON string
idp_policy_rule_action_match_criteria_instance = IdpPolicyRuleActionMatchCriteria.from_json(json)
# print the JSON string representation of the object
print(IdpPolicyRuleActionMatchCriteria.to_json())

# convert the object into a dict
idp_policy_rule_action_match_criteria_dict = idp_policy_rule_action_match_criteria_instance.to_dict()
# create an instance of IdpPolicyRuleActionMatchCriteria from a dict
idp_policy_rule_action_match_criteria_from_dict = IdpPolicyRuleActionMatchCriteria.from_dict(idp_policy_rule_action_match_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


