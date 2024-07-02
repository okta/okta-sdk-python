# AccessPolicyRuleApplicationSignOn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** |  | [optional] 
**verification_method** | [**VerificationMethod**](VerificationMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.access_policy_rule_application_sign_on import AccessPolicyRuleApplicationSignOn

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyRuleApplicationSignOn from a JSON string
access_policy_rule_application_sign_on_instance = AccessPolicyRuleApplicationSignOn.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyRuleApplicationSignOn.to_json())

# convert the object into a dict
access_policy_rule_application_sign_on_dict = access_policy_rule_application_sign_on_instance.to_dict()
# create an instance of AccessPolicyRuleApplicationSignOn from a dict
access_policy_rule_application_sign_on_from_dict = AccessPolicyRuleApplicationSignOn.from_dict(access_policy_rule_application_sign_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


