# UserSchemaBase

All Okta-defined profile properties are defined in a profile subschema with the resolution scope `#base`. You can't modify these properties, except to update permissions, to change the nullability of `firstName` and `lastName`, or to specify a pattern for `login`. They can't be removed.  The base user profile is based on the [System for Cross-domain Identity Management: Core Schema](https://tools.ietf.org/html/draft-ietf-scim-core-schema-22#section-4.1.1) and has the standard properties detailed below.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The subschema name | [optional] [readonly] 
**properties** | [**UserSchemaBaseProperties**](UserSchemaBaseProperties.md) | The &#x60;#base&#x60; object properties | [optional] 
**required** | **List[str]** | A collection indicating required property names | [optional] [readonly] 
**type** | **str** | The object type | [optional] [readonly] 

## Example

```python
from okta.models.user_schema_base import UserSchemaBase

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaBase from a JSON string
user_schema_base_instance = UserSchemaBase.from_json(json)
# print the JSON string representation of the object
print(UserSchemaBase.to_json())

# convert the object into a dict
user_schema_base_dict = user_schema_base_instance.to_dict()
# create an instance of UserSchemaBase from a dict
user_schema_base_from_dict = UserSchemaBase.from_dict(user_schema_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


