# UserSchemaAttributeMaster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**List[UserSchemaAttributeMasterPriority]**](UserSchemaAttributeMasterPriority.md) |  | [optional] 
**type** | [**UserSchemaAttributeMasterType**](UserSchemaAttributeMasterType.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_schema_attribute_master import UserSchemaAttributeMaster

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaAttributeMaster from a JSON string
user_schema_attribute_master_instance = UserSchemaAttributeMaster.from_json(json)
# print the JSON string representation of the object
print(UserSchemaAttributeMaster.to_json())

# convert the object into a dict
user_schema_attribute_master_dict = user_schema_attribute_master_instance.to_dict()
# create an instance of UserSchemaAttributeMaster from a dict
user_schema_attribute_master_form_dict = user_schema_attribute_master.from_dict(user_schema_attribute_master_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


