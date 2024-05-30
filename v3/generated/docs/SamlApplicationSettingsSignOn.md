# SamlApplicationSettingsSignOn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_endpoints** | [**List[AcsEndpoint]**](AcsEndpoint.md) |  | [optional] 
**allow_multiple_acs_endpoints** | **bool** |  | [optional] 
**assertion_signed** | **bool** |  | [optional] 
**attribute_statements** | [**List[SamlAttributeStatement]**](SamlAttributeStatement.md) |  | [optional] 
**audience** | **str** |  | [optional] 
**audience_override** | **str** |  | [optional] 
**authn_context_class_ref** | **str** |  | [optional] 
**configured_attribute_statements** | [**List[SamlAttributeStatement]**](SamlAttributeStatement.md) |  | [optional] 
**default_relay_state** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 
**destination_override** | **str** |  | [optional] 
**digest_algorithm** | **str** |  | [optional] 
**honor_force_authn** | **bool** |  | [optional] 
**idp_issuer** | **str** |  | [optional] 
**inline_hooks** | [**List[SignOnInlineHook]**](SignOnInlineHook.md) |  | [optional] 
**participate_slo** | [**SloParticipate**](SloParticipate.md) |  | [optional] 
**recipient** | **str** |  | [optional] 
**recipient_override** | **str** |  | [optional] 
**request_compressed** | **bool** |  | [optional] 
**response_signed** | **bool** |  | [optional] 
**signature_algorithm** | **str** |  | [optional] 
**slo** | [**SingleLogout**](SingleLogout.md) |  | [optional] 
**sp_certificate** | [**SpCertificate**](SpCertificate.md) |  | [optional] 
**sp_issuer** | **str** |  | [optional] 
**sso_acs_url** | **str** |  | [optional] 
**sso_acs_url_override** | **str** |  | [optional] 
**subject_name_id_format** | **str** |  | [optional] 
**subject_name_id_template** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.saml_application_settings_sign_on import SamlApplicationSettingsSignOn

# TODO update the JSON string below
json = "{}"
# create an instance of SamlApplicationSettingsSignOn from a JSON string
saml_application_settings_sign_on_instance = SamlApplicationSettingsSignOn.from_json(json)
# print the JSON string representation of the object
print(SamlApplicationSettingsSignOn.to_json())

# convert the object into a dict
saml_application_settings_sign_on_dict = saml_application_settings_sign_on_instance.to_dict()
# create an instance of SamlApplicationSettingsSignOn from a dict
saml_application_settings_sign_on_form_dict = saml_application_settings_sign_on.from_dict(saml_application_settings_sign_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


