# AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints

Constraints for the authenticator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aaguid_groups** | **List[str]** | The list of FIDO2 WebAuthn authenticator groups allowed for enrollment. The authenticators in the group are based on FIDO Alliance Metadata Service that&#39;s identified by name or the Authenticator Attestation Global Unique Identifier ([AAGUID](https://support.yubico.com/hc/en-us/articles/360016648959-YubiKey-Hardware-FIDO2-AAGUIDs)) number. These groups are defined in the [WebAuthn authenticator method settings](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Authenticator/#tag/Authenticator/operation/listAuthenticatorMethods). | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_authenticator_settings_constraints import AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints from a JSON string
authenticator_enrollment_policy_authenticator_settings_constraints_instance = AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints.to_json())

# convert the object into a dict
authenticator_enrollment_policy_authenticator_settings_constraints_dict = authenticator_enrollment_policy_authenticator_settings_constraints_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints from a dict
authenticator_enrollment_policy_authenticator_settings_constraints_from_dict = AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints.from_dict(authenticator_enrollment_policy_authenticator_settings_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


