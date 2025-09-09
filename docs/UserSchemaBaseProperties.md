# UserSchemaBaseProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**cost_center** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**country_code** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**department** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**display_name** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**division** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**email** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**employee_number** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**first_name** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**honorific_prefix** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**honorific_suffix** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**last_name** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**locale** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**login** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**manager** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**manager_id** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**middle_name** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**mobile_phone** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**nick_name** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**organization** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**postal_address** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**preferred_language** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**primary_phone** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**profile_url** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**second_email** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**state** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**street_address** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**timezone** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**title** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**user_type** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 
**zip_code** | [**UserSchemaAttribute**](UserSchemaAttribute.md) |  | [optional] 

## Example

```python
from okta.models.user_schema_base_properties import UserSchemaBaseProperties

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaBaseProperties from a JSON string
user_schema_base_properties_instance = UserSchemaBaseProperties.from_json(json)
# print the JSON string representation of the object
print(UserSchemaBaseProperties.to_json())

# convert the object into a dict
user_schema_base_properties_dict = user_schema_base_properties_instance.to_dict()
# create an instance of UserSchemaBaseProperties from a dict
user_schema_base_properties_from_dict = UserSchemaBaseProperties.from_dict(user_schema_base_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


