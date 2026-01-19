# OktaSignOnPolicyConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**people** | [**AuthenticatorEnrollmentPolicyConditionsAllOfPeople**](AuthenticatorEnrollmentPolicyConditionsAllOfPeople.md) |  | [optional] 

## Example

```python
from okta.models.okta_sign_on_policy_conditions import OktaSignOnPolicyConditions

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSignOnPolicyConditions from a JSON string
okta_sign_on_policy_conditions_instance = OktaSignOnPolicyConditions.from_json(json)
# print the JSON string representation of the object
print(OktaSignOnPolicyConditions.to_json())

# convert the object into a dict
okta_sign_on_policy_conditions_dict = okta_sign_on_policy_conditions_instance.to_dict()
# create an instance of OktaSignOnPolicyConditions from a dict
okta_sign_on_policy_conditions_from_dict = OktaSignOnPolicyConditions.from_dict(okta_sign_on_policy_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


