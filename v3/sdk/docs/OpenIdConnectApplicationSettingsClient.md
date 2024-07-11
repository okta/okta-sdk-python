# OpenIdConnectApplicationSettingsClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_type** | [**OpenIdConnectApplicationType**](OpenIdConnectApplicationType.md) |  | [optional] 
**client_uri** | **str** |  | [optional] 
**consent_method** | [**OpenIdConnectApplicationConsentMethod**](OpenIdConnectApplicationConsentMethod.md) |  | [optional] 
**dpop_bound_access_tokens** | **bool** | Indicates that the client application uses Demonstrating Proof-of-Possession (DPoP) for token requests. If &#x60;true&#x60;, the authorization server rejects token requests from this client that don&#39;t contain the DPoP header. | [optional] [default to False]
**frontchannel_logout_session_required** | **bool** | Include user session details. | [optional] 
**frontchannel_logout_uri** | **str** | URL where Okta sends the logout request. | [optional] 
**grant_types** | [**List[OAuthGrantType]**](OAuthGrantType.md) |  | [optional] 
**idp_initiated_login** | [**OpenIdConnectApplicationIdpInitiatedLogin**](OpenIdConnectApplicationIdpInitiatedLogin.md) |  | [optional] 
**initiate_login_uri** | **str** |  | [optional] 
**issuer_mode** | [**OpenIdConnectApplicationIssuerMode**](OpenIdConnectApplicationIssuerMode.md) |  | [optional] 
**jwks** | [**OpenIdConnectApplicationSettingsClientKeys**](OpenIdConnectApplicationSettingsClientKeys.md) |  | [optional] 
**jwks_uri** | **str** | URL string that references a JSON Web Key Set for validating JWTs presented to Okta. | [optional] 
**logo_uri** | **str** |  | [optional] 
**participate_slo** | **bool** | Allows the app to participate in front-channel single logout. | [optional] 
**policy_uri** | **str** |  | [optional] 
**post_logout_redirect_uris** | **List[str]** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**refresh_token** | [**OpenIdConnectApplicationSettingsRefreshToken**](OpenIdConnectApplicationSettingsRefreshToken.md) |  | [optional] 
**response_types** | [**List[OAuthResponseType]**](OAuthResponseType.md) |  | [optional] 
**tos_uri** | **str** |  | [optional] 
**wildcard_redirect** | **str** |  | [optional] 

## Example

```python
from okta.models.open_id_connect_application_settings_client import OpenIdConnectApplicationSettingsClient

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplicationSettingsClient from a JSON string
open_id_connect_application_settings_client_instance = OpenIdConnectApplicationSettingsClient.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplicationSettingsClient.to_json())

# convert the object into a dict
open_id_connect_application_settings_client_dict = open_id_connect_application_settings_client_instance.to_dict()
# create an instance of OpenIdConnectApplicationSettingsClient from a dict
open_id_connect_application_settings_client_from_dict = OpenIdConnectApplicationSettingsClient.from_dict(open_id_connect_application_settings_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


