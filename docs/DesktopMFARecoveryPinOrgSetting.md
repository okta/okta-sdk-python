# DesktopMFARecoveryPinOrgSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desktop_mfa_recovery_pin_enabled** | **bool** | Indicates whether or not the Desktop MFA Recovery PIN feature is enabled | [optional] [default to False]

## Example

```python
from okta.models.desktop_mfa_recovery_pin_org_setting import DesktopMFARecoveryPinOrgSetting

# TODO update the JSON string below
json = "{}"
# create an instance of DesktopMFARecoveryPinOrgSetting from a JSON string
desktop_mfa_recovery_pin_org_setting_instance = DesktopMFARecoveryPinOrgSetting.from_json(json)
# print the JSON string representation of the object
print(DesktopMFARecoveryPinOrgSetting.to_json())

# convert the object into a dict
desktop_mfa_recovery_pin_org_setting_dict = desktop_mfa_recovery_pin_org_setting_instance.to_dict()
# create an instance of DesktopMFARecoveryPinOrgSetting from a dict
desktop_mfa_recovery_pin_org_setting_from_dict = DesktopMFARecoveryPinOrgSetting.from_dict(desktop_mfa_recovery_pin_org_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


