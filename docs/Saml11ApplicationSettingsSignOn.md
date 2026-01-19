# Saml11ApplicationSettingsSignOn

SAML 1.1 sign-on mode attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_override** | **str** | The intended audience of the SAML assertion. This is usually the Entity ID of your application. | [optional] 
**default_relay_state** | **str** | The URL of the resource to direct users after they successfully sign in to the SP using SAML. See the SP documentation to check if you need to specify a RelayState. In most instances, you can leave this field blank. | [optional] 
**recipient_override** | **str** | The location where the application can present the SAML assertion. This is usually the Single Sign-On (SSO) URL. | [optional] 
**sso_acs_url_override** | **str** | Assertion Consumer Services (ACS) URL value for the Service Provider (SP). This URL is always used for Identity Provider (IdP) initiated sign-on requests. | [optional] 

## Example

```python
from okta.models.saml11_application_settings_sign_on import Saml11ApplicationSettingsSignOn

# TODO update the JSON string below
json = "{}"
# create an instance of Saml11ApplicationSettingsSignOn from a JSON string
saml11_application_settings_sign_on_instance = Saml11ApplicationSettingsSignOn.from_json(json)
# print the JSON string representation of the object
print(Saml11ApplicationSettingsSignOn.to_json())

# convert the object into a dict
saml11_application_settings_sign_on_dict = saml11_application_settings_sign_on_instance.to_dict()
# create an instance of Saml11ApplicationSettingsSignOn from a dict
saml11_application_settings_sign_on_from_dict = Saml11ApplicationSettingsSignOn.from_dict(saml11_application_settings_sign_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


