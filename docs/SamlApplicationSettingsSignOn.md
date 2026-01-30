# SamlApplicationSettingsSignOn

SAML 2.0 sign-on attributes. > **Note:** Set either `destinationOverride` or `ssoAcsUrl` to configure any other SAML 2.0 attributes in this section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_endpoints** | [**List[AcsEndpoint]**](AcsEndpoint.md) | An array of ACS endpoints. You can configure a maximum of 100 endpoints. | [optional] 
**allow_multiple_acs_endpoints** | **bool** | Determines whether the app allows you to configure multiple ACS URIs | 
**assertion_encryption** | [**SamlAssertionEncryption**](SamlAssertionEncryption.md) |  | [optional] 
**assertion_signed** | **bool** | Determines whether the SAML assertion is digitally signed | 
**attribute_statements** | [**List[SamlAttributeStatement]**](SamlAttributeStatement.md) | A list of custom attribute statements for the app&#39;s SAML assertion. See [SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0-cd-02.html).  There are two types of attribute statements: | Type | Description | | ---- | ----------- | | EXPRESSION | Generic attribute statement that can be dynamic and supports [Okta Expression Language](https://developer.okta.com/docs/reference/okta-expression-language/) | | GROUP | Group attribute statement |  | [optional] 
**audience** | **str** | The entity ID of the SP. Use the entity ID value exactly as provided by the SP. | 
**audience_override** | **str** | Audience override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**authn_context_class_ref** | **str** | Identifies the SAML authentication context class for the assertion&#39;s authentication statement | 
**configured_attribute_statements** | [**List[SamlAttributeStatement]**](SamlAttributeStatement.md) | The list of dynamic attribute statements for the SAML assertion inherited from app metadata (apps from the OIN) during app creation.  There are two types of attribute statements: &#x60;EXPRESSION&#x60; and &#x60;GROUP&#x60;.  | [optional] 
**default_relay_state** | **str** | Identifies a specific application resource in an IdP-initiated SSO scenario | [optional] 
**destination** | **str** | Identifies the location inside the SAML assertion where the SAML response should be sent | 
**destination_override** | **str** | Destination override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**digest_algorithm** | **str** | Determines the digest algorithm used to digitally sign the SAML assertion and response | 
**honor_force_authn** | **bool** | Set to &#x60;true&#x60; to prompt users for their credentials when a SAML request has the &#x60;ForceAuthn&#x60; attribute set to &#x60;true&#x60; | 
**idp_issuer** | **str** | SAML Issuer ID | 
**inline_hooks** | [**List[SignOnInlineHook]**](SignOnInlineHook.md) | Associates the app with SAML inline hooks. See [the SAML assertion inline hook reference](https://developer.okta.com/docs/reference/saml-hook/). | [optional] 
**participate_slo** | [**SloParticipate**](SloParticipate.md) |  | [optional] 
**recipient** | **str** | The location where the app may present the SAML assertion | 
**recipient_override** | **str** | Recipient override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**request_compressed** | **bool** | Determines whether the SAML request is expected to be compressed | 
**response_signed** | **bool** | Determines whether the SAML authentication response message is digitally signed by the IdP &gt; **Note:** Either (or both) &#x60;responseSigned&#x60; or &#x60;assertionSigned&#x60; must be &#x60;TRUE&#x60;. | 
**saml_assertion_lifetime_seconds** | **int** | Determines the SAML app session lifetimes with Okta | [optional] 
**signature_algorithm** | **str** | Determines the signing algorithm used to digitally sign the SAML assertion and response | 
**slo** | [**SingleLogout**](SingleLogout.md) |  | [optional] 
**sp_certificate** | [**SamlSpCertificate**](SamlSpCertificate.md) |  | [optional] 
**sp_issuer** | **str** | The issuer ID for the Service Provider. This property appears when SLO is enabled. | [optional] 
**sso_acs_url** | **str** | Single Sign-On Assertion Consumer Service (ACS) URL | 
**sso_acs_url_override** | **str** | Assertion Consumer Service (ACS) URL override for CASB configuration. See [CASB config guide](https://help.okta.com/en-us/Content/Topics/Apps/CASB-config-guide.htm). | [optional] 
**subject_name_id_format** | **str** | Identifies the SAML processing rules. Supported values: | 
**subject_name_id_template** | **str** | Template for app user&#39;s username when a user is assigned to the app | 

## Example

```python
from okta.models.saml_application_settings_sign_on import SamlApplicationSettingsSignOn

# TODO update the JSON string below
json = "{}"
# create an instance of SamlApplicationSettingsSignOn from a JSON string
saml_application_settings_sign_on_instance = SamlApplicationSettingsSignOn.from_json(json)
# print the JSON string representation of the object
print(SamlApplicationSettingsSignOn.to_json())

# convert the object into a dict
saml_application_settings_sign_on_dict = saml_application_settings_sign_on_instance.to_dict()
# create an instance of SamlApplicationSettingsSignOn from a dict
saml_application_settings_sign_on_from_dict = SamlApplicationSettingsSignOn.from_dict(saml_application_settings_sign_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


