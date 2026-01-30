# PasswordPolicyConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_provider** | [**PasswordPolicyAuthenticationProviderCondition**](PasswordPolicyAuthenticationProviderCondition.md) |  | [optional] 
**people** | [**AuthenticatorEnrollmentPolicyConditionsAllOfPeople**](AuthenticatorEnrollmentPolicyConditionsAllOfPeople.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_conditions import PasswordPolicyConditions

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyConditions from a JSON string
password_policy_conditions_instance = PasswordPolicyConditions.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyConditions.to_json())

# convert the object into a dict
password_policy_conditions_dict = password_policy_conditions_instance.to_dict()
# create an instance of PasswordPolicyConditions from a dict
password_policy_conditions_from_dict = PasswordPolicyConditions.from_dict(password_policy_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


