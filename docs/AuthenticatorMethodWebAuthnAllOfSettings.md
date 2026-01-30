# AuthenticatorMethodWebAuthnAllOfSettings

The settings for the WebAuthn authenticator method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aaguid_groups** | [**List[AAGUIDGroupObject]**](AAGUIDGroupObject.md) | The FIDO2 Authenticator Attestation Global Unique Identifiers (AAGUID) groups available to the WebAuthn authenticator | [optional] 
**user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) |  | [optional] 
**attachment** | [**WebAuthnAttachmentEnum**](WebAuthnAttachmentEnum.md) |  | [optional] 
**rp_id** | [**WebAuthnRpId**](WebAuthnRpId.md) |  | [optional] 
**enable_autofill_ui** | **bool** | &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;Enables the passkeys autofill UI to display available WebAuthn discoverable credentials (\&quot;resident key\&quot;) from the Sign-In Widget username field | [optional] [default to False]

## Example

```python
from okta.models.authenticator_method_web_authn_all_of_settings import AuthenticatorMethodWebAuthnAllOfSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodWebAuthnAllOfSettings from a JSON string
authenticator_method_web_authn_all_of_settings_instance = AuthenticatorMethodWebAuthnAllOfSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodWebAuthnAllOfSettings.to_json())

# convert the object into a dict
authenticator_method_web_authn_all_of_settings_dict = authenticator_method_web_authn_all_of_settings_instance.to_dict()
# create an instance of AuthenticatorMethodWebAuthnAllOfSettings from a dict
authenticator_method_web_authn_all_of_settings_from_dict = AuthenticatorMethodWebAuthnAllOfSettings.from_dict(authenticator_method_web_authn_all_of_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


