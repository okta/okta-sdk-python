# OINSaml20ApplicationSettingsSignOn

Contains SAML 2.0 sign-on mode attributes. > **Note:** Set `destinationOverride` to configure any other SAML 2.0 attributes in this section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_statements** | [**List[SamlAttributeStatement]**](SamlAttributeStatement.md) | A list of custom attribute statements for the app&#39;s SAML assertion. See [SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html).  There are two types of attribute statements: | Type | Description | | ---- | ----------- | | EXPRESSION | Generic attribute statement that can be dynamic and supports [Okta Expression Language](https://developer.okta.com/docs/reference/okta-expression-language/) | | GROUP | Group attribute statement |  | [optional] 
**audience_override** | **str** | Audience override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**default_relay_state** | **str** | Identifies a specific application resource in an IdP-initiated SSO scenario | [optional] 
**destination_override** | **str** | Destination override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**recipient_override** | **str** | Recipient override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**saml_assertion_lifetime_seconds** | **int** | Determines the SAML app session lifetimes with Okta | [optional] 
**sso_acs_url_override** | **str** | Assertion Consumer Service (ACS) URL override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 

## Example

```python
from okta.models.oin_saml20_application_settings_sign_on import OINSaml20ApplicationSettingsSignOn

# TODO update the JSON string below
json = "{}"
# create an instance of OINSaml20ApplicationSettingsSignOn from a JSON string
oin_saml20_application_settings_sign_on_instance = OINSaml20ApplicationSettingsSignOn.from_json(json)
# print the JSON string representation of the object
print(OINSaml20ApplicationSettingsSignOn.to_json())

# convert the object into a dict
oin_saml20_application_settings_sign_on_dict = oin_saml20_application_settings_sign_on_instance.to_dict()
# create an instance of OINSaml20ApplicationSettingsSignOn from a dict
oin_saml20_application_settings_sign_on_from_dict = OINSaml20ApplicationSettingsSignOn.from_dict(oin_saml20_application_settings_sign_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


