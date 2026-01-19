# OpenIdConnectApplicationSettingsClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_type** | [**OpenIdConnectApplicationType**](OpenIdConnectApplicationType.md) |  | [optional] 
**backchannel_authentication_request_signing_alg** | **str** | The signing algorithm for Client-Initiated Backchannel Authentication (CIBA) signed requests using JWT. If this value isn&#39;t set and a JWT-signed request is sent, the request fails. &gt; **Note:** This property appears for clients with &#x60;urn:openid:params:grant-type:ciba&#x60; defined as one of the &#x60;grant_types&#x60;.  | [optional] 
**backchannel_custom_authenticator_id** | **str** | The ID of the custom authenticator that authenticates the user &gt; **Note:** This property appears for clients with &#x60;urn:openid:params:grant-type:ciba&#x60; defined as one of the &#x60;grant_types&#x60;.  | [optional] 
**backchannel_token_delivery_mode** | **str** | The delivery mode for Client-Initiated Backchannel Authentication (CIBA).  Currently, only &#x60;poll&#x60; is supported. &gt; **Note:** This property appears for clients with &#x60;urn:openid:params:grant-type:ciba&#x60; defined as one of the &#x60;grant_types&#x60;.  | [optional] 
**client_uri** | **str** | URL string of a web page providing information about the client | [optional] 
**consent_method** | [**OpenIdConnectApplicationConsentMethod**](OpenIdConnectApplicationConsentMethod.md) |  | [optional] [default to OpenIdConnectApplicationConsentMethod.TRUSTED]
**dpop_bound_access_tokens** | **bool** | Indicates that the client application uses Demonstrating Proof-of-Possession (DPoP) for token requests. If &#x60;true&#x60;, the authorization server rejects token requests from this client that don&#39;t contain the DPoP header. &gt; **Note:** If &#x60;dpop_bound_access_tokens&#x60; is true, then &#x60;client_credentials&#x60; and &#x60;implicit&#x60; aren&#39;t allowed in &#x60;grant_types&#x60;.  | [optional] [default to False]
**frontchannel_logout_session_required** | **bool** | &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;Determines whether Okta sends &#x60;sid&#x60; and &#x60;iss&#x60; in the logout request | [optional] 
**frontchannel_logout_uri** | **str** | &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;URL where Okta sends the logout request | [optional] 
**grant_types** | [**List[GrantType]**](GrantType.md) |  | 
**id_token_encrypted_response_alg** | [**IdTokenKeyEncryptionAlgorithm**](IdTokenKeyEncryptionAlgorithm.md) |  | [optional] 
**idp_initiated_login** | [**OpenIdConnectApplicationIdpInitiatedLogin**](OpenIdConnectApplicationIdpInitiatedLogin.md) |  | [optional] 
**initiate_login_uri** | **str** | URL string that a third party can use to initiate the sign-in flow by the client | [optional] 
**issuer_mode** | [**OpenIdConnectApplicationIssuerMode**](OpenIdConnectApplicationIssuerMode.md) |  | [optional] 
**jwks** | [**OpenIdConnectApplicationSettingsClientKeys**](OpenIdConnectApplicationSettingsClientKeys.md) |  | [optional] 
**jwks_uri** | **str** | URL string that references a JSON Web Key Set for validating JWTs presented to Okta or for encrypting ID tokens minted by Okta for the client | [optional] 
**logo_uri** | **str** | The URL string that references a logo for the client. This logo appears on the client tile in the End-User Dashboard. It also appears on the client consent dialog during the client consent flow. | [optional] 
**network** | [**OpenIdConnectApplicationNetwork**](OpenIdConnectApplicationNetwork.md) |  | [optional] 
**participate_slo** | **bool** | &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;Allows the app to participate in front-channel Single Logout  &gt; **Note:** You can only enable &#x60;participate_slo&#x60; for &#x60;web&#x60; and &#x60;browser&#x60; application types (&#x60;application_type&#x60;).  | [optional] 
**policy_uri** | **str** | URL string of a web page providing the client&#39;s policy document | [optional] 
**post_logout_redirect_uris** | **List[str]** | Array of redirection URI strings for relying party-initiated logouts | [optional] 
**redirect_uris** | **List[str]** | Array of redirection URI strings for use in redirect-based flows. &gt; **Note:** At least one &#x60;redirect_uris&#x60; and &#x60;response_types&#x60; are required for all client types, with exceptions: if the client uses the [Resource Owner Password ](https://tools.ietf.org/html/rfc6749#section-4.3)flow (&#x60;grant_types&#x60; contains &#x60;password&#x60;) or [Client Credentials](https://tools.ietf.org/html/rfc6749#section-4.4)flow (&#x60;grant_types&#x60; contains &#x60;client_credentials&#x60;), then no &#x60;redirect_uris&#x60; or &#x60;response_types&#x60; is necessary. In these cases, you can pass either null or an empty array for these attributes. | [optional] 
**refresh_token** | [**OpenIdConnectApplicationSettingsRefreshToken**](OpenIdConnectApplicationSettingsRefreshToken.md) |  | [optional] 
**request_object_signing_alg** | **str** | The type of JSON Web Key Set (JWKS) algorithm that must be used for signing request objects | [optional] 
**response_types** | [**List[OAuthResponseType]**](OAuthResponseType.md) | Array of OAuth 2.0 response type strings | [optional] 
**sector_identifier_uri** | **str** | The sector identifier used for pairwise &#x60;subject_type&#x60;. See [OIDC Pairwise Identifier Algorithm](https://openid.net/specs/openid-connect-messages-1_0-20.html#idtype.pairwise.alg) | [optional] 
**subject_type** | **str** | Type of the subject | [optional] 
**tos_uri** | **str** | URL string of a web page providing the client&#39;s terms of service document | [optional] 
**wildcard_redirect** | **str** | Indicates if the client is allowed to use wildcard matching of &#x60;redirect_uris&#x60; | [optional] 

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


