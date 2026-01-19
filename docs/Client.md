# Client


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_type** | [**ApplicationType**](ApplicationType.md) |  | [optional] 
**client_id** | **str** | Unique key for the client application. The &#x60;client_id&#x60; is immutable. When you create a client Application, you can&#39;t specify the &#x60;client_id&#x60; because Okta uses the application ID for the &#x60;client_id&#x60;. | [optional] [readonly] 
**client_id_issued_at** | **int** | Time at which the &#x60;client_id&#x60; was issued (measured in unix seconds) | [optional] [readonly] 
**client_name** | **str** | Human-readable string name of the client application | [optional] 
**client_secret** | **str** | OAuth 2.0 client secret string (used for confidential clients). The &#x60;client_secret&#x60; is shown only on the response of the creation or update of a client Application (and only if the &#x60;token_endpoint_auth_method&#x60; is one that requires a client secret). You can&#39;t specify the &#x60;client_secret&#x60;. If the &#x60;token_endpoint_auth_method&#x60; requires one, Okta generates a random &#x60;client_secret&#x60; for the client Application. | [optional] [readonly] 
**client_secret_expires_at** | **int** | Time at which the &#x60;client_secret&#x60; expires or 0 if it doesn&#39;t expire (measured in unix seconds) | [optional] [readonly] 
**frontchannel_logout_session_required** | **bool** | Include user session details | [optional] 
**frontchannel_logout_uri** | **str** | URL where Okta sends the logout request | [optional] 
**grant_types** | [**List[GrantType]**](GrantType.md) | Array of OAuth 2.0 grant type strings. Default value: &#x60;[authorization_code]&#x60; | [optional] 
**initiate_login_uri** | **str** | URL that a third party can use to initiate a login by the client | [optional] 
**jwks_uri** | **str** | URL string that references a [JSON Web Key Set](https://tools.ietf.org/html/rfc7517#section-5) for validating JWTs presented to Okta | [optional] 
**logo_uri** | **str** | URL string that references a logo for the client consent dialog (not the sign-in dialog) | [optional] 
**policy_uri** | **str** | URL string of a web page providing the client&#39;s policy document | [optional] 
**post_logout_redirect_uris** | **List[str]** | Array of redirection URI strings for use for relying party initiated logouts | [optional] 
**redirect_uris** | **List[str]** | Array of redirection URI strings for use in redirect-based flows. All redirect URIs must be absolute URIs and must not include a fragment component. At least one redirect URI and response type is required for all client types, with the following exceptions: If the client uses the Resource Owner Password flow (if &#x60;grant_type&#x60; contains the value password) or the Client Credentials flow (if &#x60;grant_type&#x60; contains the value &#x60;client_credentials&#x60;), then no redirect URI or response type is necessary. In these cases, you can pass either null or an empty array for these attributes. | [optional] 
**request_object_signing_alg** | [**List[SigningAlgorithm]**](SigningAlgorithm.md) | The type of [JSON Web Key Set](https://tools.ietf.org/html/rfc7517#section-5) algorithm that must be used for signing request objects | [optional] 
**response_types** | [**List[ResponseType]**](ResponseType.md) | Array of OAuth 2.0 response type strings. Default value: &#x60;[code]&#x60; | [optional] 
**token_endpoint_auth_method** | [**EndpointAuthMethod**](EndpointAuthMethod.md) |  | [optional] 
**tos_uri** | **str** | URL string of a web page providing the client&#39;s terms of service document | [optional] 

## Example

```python
from okta.models.client import Client

# TODO update the JSON string below
json = "{}"
# create an instance of Client from a JSON string
client_instance = Client.from_json(json)
# print the JSON string representation of the object
print(Client.to_json())

# convert the object into a dict
client_dict = client_instance.to_dict()
# create an instance of Client from a dict
client_from_dict = Client.from_dict(client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


