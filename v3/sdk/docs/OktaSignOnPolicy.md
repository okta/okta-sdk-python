# OktaSignOnPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**OktaSignOnPolicyConditions**](OktaSignOnPolicyConditions.md) |  | [optional] 

## Example

```python
from okta.models.okta_sign_on_policy import OktaSignOnPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSignOnPolicy from a JSON string
okta_sign_on_policy_instance = OktaSignOnPolicy.from_json(json)
# print the JSON string representation of the object
print(OktaSignOnPolicy.to_json())

# convert the object into a dict
okta_sign_on_policy_dict = okta_sign_on_policy_instance.to_dict()
# create an instance of OktaSignOnPolicy from a dict
okta_sign_on_policy_from_dict = OktaSignOnPolicy.from_dict(okta_sign_on_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


