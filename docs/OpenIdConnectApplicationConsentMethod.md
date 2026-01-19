# OpenIdConnectApplicationConsentMethod

Indicates whether user consent is required or implicit. A consent dialog appears for the end user depending on the values of three elements:  * [prompt](/openapi/okta-oauth/oauth/tag/OrgAS/#tag/OrgAS/operation/authorize!in=query&path=prompt&t=request): A query parameter that is used in requests to `/authorize` * `consent_method` (this property) * [consent](/openapi/okta-management/management/tag/AuthorizationServerScopes/#tag/AuthorizationServerScopes/operation/createOAuth2Scope!path=consent&t=request): A [Scope](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/AuthorizationServerScopes/) property that allows you to enable or disable user consent for an individual scope  | `prompt` | `consent_method` | `consent` | Result | ---------- | ----------- | ---------- | ----------- | | CONSENT | TRUSTED or REQUIRED | REQUIRED | Prompted | | CONSENT | TRUSTED or REQUIRED | FLEXIBLE | Prompted | | CONSENT | TRUSTED | IMPLICIT | Not prompted | | NONE | TRUSTED | FLEXIBLE, IMPLICIT, or REQUIRED | Not prompted | | NONE | REQUIRED | FLEXIBLE or REQUIRED | Prompted | | NONE | REQUIRED | IMPLICIT | Not prompted |  > **Notes:** > * If you request a scope that requires consent while using the `client_credentials` flow, an error is returned because the flow doesn't support user consent. > * If the `prompt` value is set to `NONE`, but the `consent_method` and the consent values are set to `REQUIRED`, then an error occurs. > * When a scope is requested during a Client Credentials grant flow and `consent` is set to `FLEXIBLE`, the scope is granted in the access token with no consent prompt. This occurs because there is no user involved in a two-legged OAuth 2.0 [Client Credentials](https://developer.okta.com/docs/guides/implement-grant-type/clientcreds/main/) grant flow. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


