# UserSchemaPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**properties** | [**Dict[str, UserSchemaAttribute]**](UserSchemaAttribute.md) |  | [optional] 
**required** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_schema_public import UserSchemaPublic

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaPublic from a JSON string
user_schema_public_instance = UserSchemaPublic.from_json(json)
# print the JSON string representation of the object
print(UserSchemaPublic.to_json())

# convert the object into a dict
user_schema_public_dict = user_schema_public_instance.to_dict()
# create an instance of UserSchemaPublic from a dict
user_schema_public_form_dict = user_schema_public.from_dict(user_schema_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


