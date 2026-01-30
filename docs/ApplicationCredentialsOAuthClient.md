# ApplicationCredentialsOAuthClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_key_rotation** | **bool** | Requested key rotation mode | [optional] [default to True]
**client_id** | **str** | Unique identifier for the OAuth 2.0 client app  &gt; **Notes:** &gt; * If you don&#39;t specify the &#x60;client_id&#x60;, this immutable property is populated with the [Application instance ID](/openapi/okta-management/management/tag/Application/#tag/Application/operation/getApplication!c&#x3D;200&amp;path&#x3D;4/id&amp;t&#x3D;response). &gt; * The &#x60;client_id&#x60; must consist of alphanumeric characters or the following special characters: &#x60;$-_.+!*&#39;(),&#x60;. &gt; * You can&#39;t use the reserved word &#x60;ALL_CLIENTS&#x60;. | [optional] 
**client_secret** | **str** | OAuth 2.0 client secret string (used for confidential clients)  &gt; **Notes:** If a &#x60;client_secret&#x60; isn&#39;t provided on creation, and the &#x60;token_endpoint_auth_method&#x60; requires one, Okta generates a random &#x60;client_secret&#x60; for the client app. &gt; The &#x60;client_secret&#x60; is only shown when an OAuth 2.0 client app is created or updated (and only if the &#x60;token_endpoint_auth_method&#x60; requires a client secret). | [optional] 
**pkce_required** | **bool** | Requires Proof Key for Code Exchange (PKCE) for additional verification. If &#x60;token_endpoint_auth_method&#x60; is &#x60;none&#x60;, then &#x60;pkce_required&#x60; must be &#x60;true&#x60;. The default is &#x60;true&#x60; for browser and native app types. | [optional] [default to True]
**token_endpoint_auth_method** | [**OAuthEndpointAuthenticationMethod**](OAuthEndpointAuthenticationMethod.md) |  | [optional] [default to OAuthEndpointAuthenticationMethod.CLIENT_SECRET_BASIC]

## Example

```python
from okta.models.application_credentials_o_auth_client import ApplicationCredentialsOAuthClient

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCredentialsOAuthClient from a JSON string
application_credentials_o_auth_client_instance = ApplicationCredentialsOAuthClient.from_json(json)
# print the JSON string representation of the object
print(ApplicationCredentialsOAuthClient.to_json())

# convert the object into a dict
application_credentials_o_auth_client_dict = application_credentials_o_auth_client_instance.to_dict()
# create an instance of ApplicationCredentialsOAuthClient from a dict
application_credentials_o_auth_client_from_dict = ApplicationCredentialsOAuthClient.from_dict(application_credentials_o_auth_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


