# UserTypeRef

The user type that determines the schema for the user's profile...

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user type | [optional] 

## Example

```python
from okta.models.user_type_ref import UserTypeRef

# TODO update the JSON string below
json = "{}"
# create an instance of UserTypeRef from a JSON string
user_type_ref_instance = UserTypeRef.from_json(json)
# print the JSON string representation of the object
print(UserTypeRef.to_json())

# convert the object into a dict
user_type_ref_dict = user_type_ref_instance.to_dict()
# create an instance of UserTypeRef from a dict
user_type_ref_from_dict = UserTypeRef.from_dict(user_type_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


