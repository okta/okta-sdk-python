# PasswordPolicyPasswordSettingsBreachedProtection

Breached Protection settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegated_workflow_id** | **str** | The &#x60;id&#x60; of the workflow that runs when a breached password is found during a sign-in attempt. | [optional] 
**expire_after_days** | **int** | Specifies the number of days after a breached password is found during a sign-in attempt that the user&#39;s password should expire. Valid values: 0 through 10. If set to 0, it happens immediately. | [optional] 
**logout_enabled** | **bool** | (Optional, default is false) If true, you must also specify a value for &#x60;expireAfterDays&#x60;. When enabled, the user&#39;s session(s) are terminated immediately the first time the user&#39;s credentials are detected as part of a breach. | [optional] [default to False]

## Example

```python
from okta.models.password_policy_password_settings_breached_protection import PasswordPolicyPasswordSettingsBreachedProtection

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyPasswordSettingsBreachedProtection from a JSON string
password_policy_password_settings_breached_protection_instance = PasswordPolicyPasswordSettingsBreachedProtection.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyPasswordSettingsBreachedProtection.to_json())

# convert the object into a dict
password_policy_password_settings_breached_protection_dict = password_policy_password_settings_breached_protection_instance.to_dict()
# create an instance of PasswordPolicyPasswordSettingsBreachedProtection from a dict
password_policy_password_settings_breached_protection_from_dict = PasswordPolicyPasswordSettingsBreachedProtection.from_dict(password_policy_password_settings_breached_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


