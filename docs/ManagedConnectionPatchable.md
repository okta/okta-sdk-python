# ManagedConnectionPatchable

Update an existing managed connection. All fields are optional for partial updates.  **Field Applicability by Connection Type:** - `resourceIndicator`: Valid for IDENTITY_ASSERTION_APP_INSTANCE, IDENTITY_ASSERTION_CUSTOM_AS, STS_SERVICE_ACCOUNT, and STS_VAULT_SECRET. Set to `null` to reset to the default value (the resource's ORN). - `scopeCondition` and `scopes`: Only valid for IDENTITY_ASSERTION_APP_INSTANCE and IDENTITY_ASSERTION_CUSTOM_AS connections. The server returns a validation error if these fields are sent for STS connection types.  **Validation:** - If `scopeCondition` is provided, `scopes` must also be provided, and vice versa. - For STS_VAULT_SECRET and STS_SERVICE_ACCOUNT connection types, only `resourceIndicator` can be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_indicator** | **str** | Resource indicator used when requesting tokens. Set to &#x60;null&#x60; to reset to the default value based on the connection type (app instance ORN, authorization server ORN, secret ORN, or service account ORN). | [optional] 
**scope_condition** | [**ManagedConnectionPatchableScopeCondition**](ManagedConnectionPatchableScopeCondition.md) |  | [optional] 
**scopes** | **List[str]** | Array of scopes for the connection. For &#x60;ALL_SCOPES&#x60;, this array must contain a single value of &#x60;*&#x60;. For &#x60;INCLUDE_ONLY&#x60;, only these scopes are allowed. For &#x60;EXCLUDE&#x60;, all scopes except these are allowed.  **Restrictions:** - Only valid for IDENTITY_ASSERTION_APP_INSTANCE and IDENTITY_ASSERTION_CUSTOM_AS connection types - Must be provided together with &#x60;scopeCondition&#x60; - Returns a 400 error if sent for STS_VAULT_SECRET or STS_SERVICE_ACCOUNT connection types | [optional] 

## Example

```python
from okta.models.managed_connection_patchable import ManagedConnectionPatchable

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedConnectionPatchable from a JSON string
managed_connection_patchable_instance = ManagedConnectionPatchable.from_json(json)
# print the JSON string representation of the object
print(ManagedConnectionPatchable.to_json())

# convert the object into a dict
managed_connection_patchable_dict = managed_connection_patchable_instance.to_dict()
# create an instance of ManagedConnectionPatchable from a dict
managed_connection_patchable_from_dict = ManagedConnectionPatchable.from_dict(managed_connection_patchable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


