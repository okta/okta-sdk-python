# OAuthMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_endpoint** | **str** | URL of the authorization server&#39;s authorization endpoint. | [optional] 
**backchannel_authentication_request_signing_alg_values_supported** | [**List[SigningAlgorithm]**](SigningAlgorithm.md) | &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;A list of signing algorithms that this authorization server supports for signed requests. | [optional] 
**backchannel_token_delivery_modes_supported** | [**List[TokenDeliveryMode]**](TokenDeliveryMode.md) | &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;The delivery modes that this authorization server supports for Client-Initiated Backchannel Authentication. | [optional] 
**claims_supported** | **List[str]** | A list of the claims supported by this authorization server. | [optional] 
**code_challenge_methods_supported** | [**List[CodeChallengeMethod]**](CodeChallengeMethod.md) | A list of PKCE code challenge methods supported by this authorization server. | [optional] 
**device_authorization_endpoint** | **str** |  | [optional] 
**dpop_signing_alg_values_supported** | **List[str]** | A list of signing algorithms supported by this authorization server for Demonstrating Proof-of-Possession (DPoP) JWTs. | [optional] 
**end_session_endpoint** | **str** | URL of the authorization server&#39;s logout endpoint. | [optional] 
**grant_types_supported** | [**List[GrantType]**](GrantType.md) | A list of the grant type values that this authorization server supports. | [optional] 
**introspection_endpoint** | **str** | URL of the authorization server&#39;s introspection endpoint. | [optional] 
**introspection_endpoint_auth_methods_supported** | [**List[EndpointAuthMethod]**](EndpointAuthMethod.md) | A list of client authentication methods supported by this introspection endpoint. | [optional] 
**issuer** | **str** | The authorization server&#39;s issuer identifier. In the context of this document, this is your authorization server&#39;s base URL. This becomes the &#x60;iss&#x60; claim in an access token. | [optional] 
**jwks_uri** | **str** | URL of the authorization server&#39;s JSON Web Key Set document. | [optional] 
**pushed_authorization_request_endpoint** | **str** |  | [optional] 
**registration_endpoint** | **str** | URL of the authorization server&#39;s JSON Web Key Set document. | [optional] 
**request_object_signing_alg_values_supported** | [**List[SigningAlgorithm]**](SigningAlgorithm.md) | A list of signing algorithms that this authorization server supports for signed requests. | [optional] 
**request_parameter_supported** | **bool** | Indicates if Request Parameters are supported by this authorization server. | [optional] 
**response_modes_supported** | [**List[ResponseMode]**](ResponseMode.md) | A list of the &#x60;response_mode&#x60; values that this authorization server supports. More information here. | [optional] 
**response_types_supported** | [**List[ResponseTypesSupported]**](ResponseTypesSupported.md) | A list of the &#x60;response_type&#x60; values that this authorization server supports. Can be a combination of &#x60;code&#x60;, &#x60;token&#x60;, and &#x60;id_token&#x60;. | [optional] 
**revocation_endpoint** | **str** | URL of the authorization server&#39;s revocation endpoint. | [optional] 
**revocation_endpoint_auth_methods_supported** | [**List[EndpointAuthMethod]**](EndpointAuthMethod.md) | A list of client authentication methods supported by this revocation endpoint. | [optional] 
**scopes_supported** | **List[str]** | A list of the scope values that this authorization server supports. | [optional] 
**subject_types_supported** | [**List[SubjectType]**](SubjectType.md) | A list of the Subject Identifier types that this authorization server supports. Valid types include &#x60;pairwise&#x60; and &#x60;public&#x60;, but only &#x60;public&#x60; is currently supported. See the [Subject Identifier Types](https://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes) section in the OpenID Connect specification. | [optional] 
**token_endpoint** | **str** | URL of the authorization server&#39;s token endpoint. | [optional] 
**token_endpoint_auth_methods_supported** | [**List[EndpointAuthMethod]**](EndpointAuthMethod.md) | A list of client authentication methods supported by this token endpoint. | [optional] 

## Example

```python
from okta.models.o_auth_metadata import OAuthMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthMetadata from a JSON string
o_auth_metadata_instance = OAuthMetadata.from_json(json)
# print the JSON string representation of the object
print(OAuthMetadata.to_json())

# convert the object into a dict
o_auth_metadata_dict = o_auth_metadata_instance.to_dict()
# create an instance of OAuthMetadata from a dict
o_auth_metadata_from_dict = OAuthMetadata.from_dict(o_auth_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


