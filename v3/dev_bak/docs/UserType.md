# UserType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | A timestamp from when the User Type was created | [optional] [readonly] 
**created_by** | **str** | The user ID of the account that created the User Type | [optional] [readonly] 
**default** | **bool** | A boolean value to indicate if this is the default User Type | [optional] [readonly] 
**description** | **str** | The human-readable description of the User Type | [optional] 
**display_name** | **str** | The human-readable name of the User Type | 
**id** | **str** | The unique key for the User Type | [optional] 
**last_updated** | **datetime** | A timestamp from when the User Type was most recently updated | [optional] [readonly] 
**last_updated_by** | **str** | The user ID of the most recent account to edit the User Type | [optional] [readonly] 
**name** | **str** | The name of the User Type. The name must start with A-Z or a-z and contain only A-Z, a-z, 0-9, or underscore (_) characters.   This value becomes read-only after creation and can&#39;t be updated. | 
**links** | [**UserTypeLinks**](UserTypeLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_type import UserType

# TODO update the JSON string below
json = "{}"
# create an instance of UserType from a JSON string
user_type_instance = UserType.from_json(json)
# print the JSON string representation of the object
print(UserType.to_json())

# convert the object into a dict
user_type_dict = user_type_instance.to_dict()
# create an instance of UserType from a dict
user_type_from_dict = UserType.from_dict(user_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


