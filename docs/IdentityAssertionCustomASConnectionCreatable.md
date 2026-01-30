# IdentityAssertionCustomASConnectionCreatable

Create an identity assertion connection for a custom authorization server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_server** | [**IdentityAssertionCustomASConnectionCreatableAuthorizationServer**](IdentityAssertionCustomASConnectionCreatableAuthorizationServer.md) |  | 
**connection_type** | **str** | Type of connection authentication method | 
**protocol_type** | **str** | The authentication protocol type used for the connection | [optional] 
**scope_condition** | [**ScopeCondition**](ScopeCondition.md) |  | 
**scopes** | **List[str]** | Array of scopes. Required for all &#x60;scopeCondition&#x60; values. For &#x60;ALL_SCOPES&#x60;, this array is required with a single value of &#x60;*&#x60;. For &#x60;INCLUDE_ONLY&#x60;, only these scopes are allowed. For &#x60;EXCLUDE&#x60;, all scopes except these are allowed. | 

## Example

```python
from okta.models.identity_assertion_custom_as_connection_creatable import IdentityAssertionCustomASConnectionCreatable

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAssertionCustomASConnectionCreatable from a JSON string
identity_assertion_custom_as_connection_creatable_instance = IdentityAssertionCustomASConnectionCreatable.from_json(json)
# print the JSON string representation of the object
print(IdentityAssertionCustomASConnectionCreatable.to_json())

# convert the object into a dict
identity_assertion_custom_as_connection_creatable_dict = identity_assertion_custom_as_connection_creatable_instance.to_dict()
# create an instance of IdentityAssertionCustomASConnectionCreatable from a dict
identity_assertion_custom_as_connection_creatable_from_dict = IdentityAssertionCustomASConnectionCreatable.from_dict(identity_assertion_custom_as_connection_creatable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


