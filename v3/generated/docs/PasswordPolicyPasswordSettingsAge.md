# PasswordPolicyPasswordSettingsAge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_warn_days** | **int** |  | [optional] 
**history_count** | **int** |  | [optional] 
**max_age_days** | **int** |  | [optional] 
**min_age_minutes** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_password_settings_age import PasswordPolicyPasswordSettingsAge

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyPasswordSettingsAge from a JSON string
password_policy_password_settings_age_instance = PasswordPolicyPasswordSettingsAge.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyPasswordSettingsAge.to_json())

# convert the object into a dict
password_policy_password_settings_age_dict = password_policy_password_settings_age_instance.to_dict()
# create an instance of PasswordPolicyPasswordSettingsAge from a dict
password_policy_password_settings_age_form_dict = password_policy_password_settings_age.from_dict(password_policy_password_settings_age_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


