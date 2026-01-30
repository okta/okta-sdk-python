# PasswordPolicyPasswordSettingsAge

Age settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_warn_days** | **int** | Specifies the number of days prior to password expiration when a User is warned to reset their password: &#x60;0&#x60; indicates no warning | [optional] [default to 0]
**history_count** | **int** | Specifies the number of distinct passwords that a User must create before they can reuse a previous password: &#x60;0&#x60; indicates none | [optional] [default to 0]
**max_age_days** | **int** | Specifies how long (in days) a password remains valid before it expires: &#x60;0&#x60; indicates no limit | [optional] [default to 0]
**min_age_minutes** | **int** | Specifies the minimum time interval (in minutes) between password changes: &#x60;0&#x60; indicates no limit | [optional] [default to 0]

## Example

```python
from okta.models.password_policy_password_settings_age import PasswordPolicyPasswordSettingsAge

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyPasswordSettingsAge from a JSON string
password_policy_password_settings_age_instance = PasswordPolicyPasswordSettingsAge.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyPasswordSettingsAge.to_json())

# convert the object into a dict
password_policy_password_settings_age_dict = password_policy_password_settings_age_instance.to_dict()
# create an instance of PasswordPolicyPasswordSettingsAge from a dict
password_policy_password_settings_age_from_dict = PasswordPolicyPasswordSettingsAge.from_dict(password_policy_password_settings_age_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


