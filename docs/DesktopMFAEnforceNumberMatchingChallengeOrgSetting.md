# DesktopMFAEnforceNumberMatchingChallengeOrgSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desktop_mfa_enforce_number_matching_challenge_enabled** | **bool** | Indicates whether or not the Desktop MFA Enforce Number Matching Challenge push notifications feature is enabled | [optional] [default to False]

## Example

```python
from okta.models.desktop_mfa_enforce_number_matching_challenge_org_setting import DesktopMFAEnforceNumberMatchingChallengeOrgSetting

# TODO update the JSON string below
json = "{}"
# create an instance of DesktopMFAEnforceNumberMatchingChallengeOrgSetting from a JSON string
desktop_mfa_enforce_number_matching_challenge_org_setting_instance = DesktopMFAEnforceNumberMatchingChallengeOrgSetting.from_json(json)
# print the JSON string representation of the object
print(DesktopMFAEnforceNumberMatchingChallengeOrgSetting.to_json())

# convert the object into a dict
desktop_mfa_enforce_number_matching_challenge_org_setting_dict = desktop_mfa_enforce_number_matching_challenge_org_setting_instance.to_dict()
# create an instance of DesktopMFAEnforceNumberMatchingChallengeOrgSetting from a dict
desktop_mfa_enforce_number_matching_challenge_org_setting_from_dict = DesktopMFAEnforceNumberMatchingChallengeOrgSetting.from_dict(desktop_mfa_enforce_number_matching_challenge_org_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


