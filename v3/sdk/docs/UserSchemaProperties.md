# UserSchemaProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserSchemaPropertiesProfile**](UserSchemaPropertiesProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_schema_properties import UserSchemaProperties

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaProperties from a JSON string
user_schema_properties_instance = UserSchemaProperties.from_json(json)
# print the JSON string representation of the object
print(UserSchemaProperties.to_json())

# convert the object into a dict
user_schema_properties_dict = user_schema_properties_instance.to_dict()
# create an instance of UserSchemaProperties from a dict
user_schema_properties_from_dict = UserSchemaProperties.from_dict(user_schema_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


