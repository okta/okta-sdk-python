# PasswordPolicyPasswordSettingsComplexity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dictionary** | [**PasswordDictionary**](PasswordDictionary.md) |  | [optional] 
**exclude_attributes** | **List[str]** |  | [optional] 
**exclude_username** | **bool** |  | [optional] [default to True]
**min_length** | **int** |  | [optional] 
**min_lower_case** | **int** |  | [optional] 
**min_number** | **int** |  | [optional] 
**min_symbol** | **int** |  | [optional] 
**min_upper_case** | **int** |  | [optional] 

## Example

```python
from okta.models.password_policy_password_settings_complexity import PasswordPolicyPasswordSettingsComplexity

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyPasswordSettingsComplexity from a JSON string
password_policy_password_settings_complexity_instance = PasswordPolicyPasswordSettingsComplexity.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyPasswordSettingsComplexity.to_json())

# convert the object into a dict
password_policy_password_settings_complexity_dict = password_policy_password_settings_complexity_instance.to_dict()
# create an instance of PasswordPolicyPasswordSettingsComplexity from a dict
password_policy_password_settings_complexity_from_dict = PasswordPolicyPasswordSettingsComplexity.from_dict(password_policy_password_settings_complexity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


