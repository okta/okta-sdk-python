# UserSchemaPropertiesProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_of** | [**List[UserSchemaPropertiesProfileItem]**](UserSchemaPropertiesProfileItem.md) |  | [optional] 

## Example

```python
from okta.models.user_schema_properties_profile import UserSchemaPropertiesProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaPropertiesProfile from a JSON string
user_schema_properties_profile_instance = UserSchemaPropertiesProfile.from_json(json)
# print the JSON string representation of the object
print(UserSchemaPropertiesProfile.to_json())

# convert the object into a dict
user_schema_properties_profile_dict = user_schema_properties_profile_instance.to_dict()
# create an instance of UserSchemaPropertiesProfile from a dict
user_schema_properties_profile_from_dict = UserSchemaPropertiesProfile.from_dict(user_schema_properties_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


