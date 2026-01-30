# LinksSelfAndFullUsersLifecycle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**activate** | [**HrefObjectActivateLink**](HrefObjectActivateLink.md) |  | [optional] 
**deactivate** | [**HrefObjectDeactivateLink**](HrefObjectDeactivateLink.md) |  | [optional] 
**suspend** | [**HrefObjectSuspendLink**](HrefObjectSuspendLink.md) |  | [optional] 
**unsuspend** | [**HrefObjectUnsuspendLink**](HrefObjectUnsuspendLink.md) |  | [optional] 
**users** | [**HrefObject**](HrefObject.md) | Link to device users | [optional] 

## Example

```python
from okta.models.links_self_and_full_users_lifecycle import LinksSelfAndFullUsersLifecycle

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSelfAndFullUsersLifecycle from a JSON string
links_self_and_full_users_lifecycle_instance = LinksSelfAndFullUsersLifecycle.from_json(json)
# print the JSON string representation of the object
print(LinksSelfAndFullUsersLifecycle.to_json())

# convert the object into a dict
links_self_and_full_users_lifecycle_dict = links_self_and_full_users_lifecycle_instance.to_dict()
# create an instance of LinksSelfAndFullUsersLifecycle from a dict
links_self_and_full_users_lifecycle_from_dict = LinksSelfAndFullUsersLifecycle.from_dict(links_self_and_full_users_lifecycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


