# OINSaml11ApplicationSettingsSignOn

Contains SAML 1.1 sign-on mode attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_override** | **str** | Audience override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**default_relay_state** | **str** | Identifies a specific application resource in an IdP-initiated SSO scenario | [optional] 
**recipient_override** | **str** | Recipient override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**sso_acs_url_override** | **str** | Assertion Consumer Service (ACS) URL override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 

## Example

```python
from okta.models.oin_saml11_application_settings_sign_on import OINSaml11ApplicationSettingsSignOn

# TODO update the JSON string below
json = "{}"
# create an instance of OINSaml11ApplicationSettingsSignOn from a JSON string
oin_saml11_application_settings_sign_on_instance = OINSaml11ApplicationSettingsSignOn.from_json(json)
# print the JSON string representation of the object
print(OINSaml11ApplicationSettingsSignOn.to_json())

# convert the object into a dict
oin_saml11_application_settings_sign_on_dict = oin_saml11_application_settings_sign_on_instance.to_dict()
# create an instance of OINSaml11ApplicationSettingsSignOn from a dict
oin_saml11_application_settings_sign_on_from_dict = OINSaml11ApplicationSettingsSignOn.from_dict(oin_saml11_application_settings_sign_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


