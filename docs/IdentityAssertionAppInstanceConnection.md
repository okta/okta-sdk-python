# IdentityAssertionAppInstanceConnection

Identity assertion connection for an app instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**ManagedConnectionAppInstance**](ManagedConnectionAppInstance.md) |  | 
**authorization_server** | [**AppInstanceAuthorizationServer**](AppInstanceAuthorizationServer.md) |  | [optional] 
**connection_type** | **str** | Type of connection authentication method | 
**id** | **str** | Unique identifier for the managed connection. Only present for managed connections. | [optional] 
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the managed connection | [optional] 
**protocol_type** | **str** | The authentication protocol type used for the connection | [optional] 
**resource_indicator** | **str** | Resource indicator used when requesting tokens. | 
**scope_condition** | [**ScopeCondition**](ScopeCondition.md) |  | [optional] 
**scopes** | **List[str]** | Array of scopes. Required for all &#x60;scopeCondition&#x60; values. For &#x60;ALL_SCOPES&#x60;, this array is required with a single value of &#x60;*&#x60;. For &#x60;INCLUDE_ONLY&#x60;, only these scopes are allowed. For &#x60;EXCLUDE&#x60;, all scopes except these are allowed. | [optional] 
**status** | [**ManagedConnectionStatus**](ManagedConnectionStatus.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.identity_assertion_app_instance_connection import IdentityAssertionAppInstanceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAssertionAppInstanceConnection from a JSON string
identity_assertion_app_instance_connection_instance = IdentityAssertionAppInstanceConnection.from_json(json)
# print the JSON string representation of the object
print(IdentityAssertionAppInstanceConnection.to_json())

# convert the object into a dict
identity_assertion_app_instance_connection_dict = identity_assertion_app_instance_connection_instance.to_dict()
# create an instance of IdentityAssertionAppInstanceConnection from a dict
identity_assertion_app_instance_connection_from_dict = IdentityAssertionAppInstanceConnection.from_dict(identity_assertion_app_instance_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


