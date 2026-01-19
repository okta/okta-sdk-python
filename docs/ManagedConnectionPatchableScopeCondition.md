# ManagedConnectionPatchableScopeCondition

Determines how Okta evaluates requested scopes for the connection.  **Restrictions:** - Only valid for IDENTITY_ASSERTION_APP_INSTANCE and IDENTITY_ASSERTION_CUSTOM_AS connection types - Must be provided together with `scopes` - Returns a 400 error if sent for STS_VAULT_SECRET or STS_SERVICE_ACCOUNT connection types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


