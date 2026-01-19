# ProvisioningAction

Specifies the user provisioning action during authentication when an IdP user isn't linked to an existing Okta user. * To successfully provision a new Okta user, you must enable just-in-time (JIT) provisioning in your org security settings. * If the target username isn't unique or the resulting Okta user profile is missing a required profile attribute, JIT provisioning may fail. * New Okta users are provisioned with either a `FEDERATION` or `SOCIAL` authentication provider depending on the IdP type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


