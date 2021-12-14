# SamlApplicationSettingsSignOn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple_acs_endpoints** | **bool** |  | [optional] 
**acs_endpoints** | [**list[AcsEndpoint]**](AcsEndpoint.md) |  | [optional] 
**assertion_signed** | **bool** |  | [optional] 
**attribute_statements** | [**list[SamlAttributeStatement]**](SamlAttributeStatement.md) |  | [optional] 
**audience** | **str** |  | [optional] 
**audience_override** | **str** |  | [optional] 
**authn_context_class_ref** | **str** |  | [optional] 
**default_relay_state** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 
**destination_override** | **str** |  | [optional] 
**digest_algorithm** | **str** |  | [optional] 
**honor_force_authn** | **bool** |  | [optional] 
**idp_issuer** | **str** |  | [optional] 
**inline_hooks** | [**list[SignOnInlineHook]**](SignOnInlineHook.md) |  | [optional] 
**recipient** | **str** |  | [optional] 
**recipient_override** | **str** |  | [optional] 
**request_compressed** | **bool** |  | [optional] 
**response_signed** | **bool** |  | [optional] 
**signature_algorithm** | **str** |  | [optional] 
**slo** | [**SingleLogout**](SingleLogout.md) |  | [optional] 
**sp_issuer** | **str** |  | [optional] 
**sso_acs_url** | **str** |  | [optional] 
**sso_acs_url_override** | **str** |  | [optional] 
**sp_certificate** | [**SpCertificate**](SpCertificate.md) |  | [optional] 
**subject_name_id_format** | **str** |  | [optional] 
**subject_name_id_template** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

