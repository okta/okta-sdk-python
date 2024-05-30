# AccessPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**AccessPolicyRuleActions**](AccessPolicyRuleActions.md) |  | [optional] 
**conditions** | [**AccessPolicyRuleConditions**](AccessPolicyRuleConditions.md) |  | [optional] 

## Example

```python
from openapi_client.models.access_policy_rule import AccessPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyRule from a JSON string
access_policy_rule_instance = AccessPolicyRule.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyRule.to_json())

# convert the object into a dict
access_policy_rule_dict = access_policy_rule_instance.to_dict()
# create an instance of AccessPolicyRule from a dict
access_policy_rule_form_dict = access_policy_rule.from_dict(access_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


