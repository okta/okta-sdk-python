# AuthenticatorEnrollmentPolicySettings

Specifies the policy level settings  > **Note:** In Identity Engine, the Multifactor (MFA) Enrollment policy name has changed to authenticator enrollment policy. The policy type of `MFA_ENROLL` remains unchanged. However, the `settings` data is updated for authenticators. Policy `settings` are included only for those authenticators that are enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticators** | [**List[AuthenticatorEnrollmentPolicyAuthenticatorSettings]**](AuthenticatorEnrollmentPolicyAuthenticatorSettings.md) | List of authenticator policy settings  &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt; For orgs with the Authenticator enrollment policy feature enabled, the new default authenticator enrollment policy created by Okta contains the &#x60;authenticators&#x60; property in the policy settings. Existing default authenticator enrollment policies from a migrated Classic Engine org remain unchanged. The policies still use the &#x60;factors&#x60; property in their settings. The &#x60;authenticators&#x60; parameter allows you to configure all available authenticators, including authentication and recovery. The &#x60;factors&#x60; parameter only allows you to configure multifactor authentication.  | [optional] 
**type** | [**AuthenticatorEnrollmentPolicySettingsType**](AuthenticatorEnrollmentPolicySettingsType.md) |  | [optional] [default to AuthenticatorEnrollmentPolicySettingsType.FACTORS]

## Example

```python
from okta.models.authenticator_enrollment_policy_settings import AuthenticatorEnrollmentPolicySettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicySettings from a JSON string
authenticator_enrollment_policy_settings_instance = AuthenticatorEnrollmentPolicySettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicySettings.to_json())

# convert the object into a dict
authenticator_enrollment_policy_settings_dict = authenticator_enrollment_policy_settings_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicySettings from a dict
authenticator_enrollment_policy_settings_from_dict = AuthenticatorEnrollmentPolicySettings.from_dict(authenticator_enrollment_policy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


