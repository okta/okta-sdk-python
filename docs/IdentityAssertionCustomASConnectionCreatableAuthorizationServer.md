# IdentityAssertionCustomASConnectionCreatableAuthorizationServer

Reference to a custom authorization server and its configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the authorization server | 

## Example

```python
from okta.models.identity_assertion_custom_as_connection_creatable_authorization_server import IdentityAssertionCustomASConnectionCreatableAuthorizationServer

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAssertionCustomASConnectionCreatableAuthorizationServer from a JSON string
identity_assertion_custom_as_connection_creatable_authorization_server_instance = IdentityAssertionCustomASConnectionCreatableAuthorizationServer.from_json(json)
# print the JSON string representation of the object
print(IdentityAssertionCustomASConnectionCreatableAuthorizationServer.to_json())

# convert the object into a dict
identity_assertion_custom_as_connection_creatable_authorization_server_dict = identity_assertion_custom_as_connection_creatable_authorization_server_instance.to_dict()
# create an instance of IdentityAssertionCustomASConnectionCreatableAuthorizationServer from a dict
identity_assertion_custom_as_connection_creatable_authorization_server_from_dict = IdentityAssertionCustomASConnectionCreatableAuthorizationServer.from_dict(identity_assertion_custom_as_connection_creatable_authorization_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


