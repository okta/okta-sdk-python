# IdentityAssertionAppInstanceConnectionCreatableApp

Reference to an app instance in [ORN](/openapi/okta-management/guides/roles/#okta-resource-name-orn) format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the app instance | 

## Example

```python
from okta.models.identity_assertion_app_instance_connection_creatable_app import IdentityAssertionAppInstanceConnectionCreatableApp

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAssertionAppInstanceConnectionCreatableApp from a JSON string
identity_assertion_app_instance_connection_creatable_app_instance = IdentityAssertionAppInstanceConnectionCreatableApp.from_json(json)
# print the JSON string representation of the object
print(IdentityAssertionAppInstanceConnectionCreatableApp.to_json())

# convert the object into a dict
identity_assertion_app_instance_connection_creatable_app_dict = identity_assertion_app_instance_connection_creatable_app_instance.to_dict()
# create an instance of IdentityAssertionAppInstanceConnectionCreatableApp from a dict
identity_assertion_app_instance_connection_creatable_app_from_dict = IdentityAssertionAppInstanceConnectionCreatableApp.from_dict(identity_assertion_app_instance_connection_creatable_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


