# UserSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | JSON schema version identifier | [optional] [readonly] 
**created** | **str** | Timestamp when the schema was created | [optional] [readonly] 
**definitions** | [**UserSchemaDefinitions**](UserSchemaDefinitions.md) | User profile subschemas  The profile object for a user is defined by a composite schema of base and custom properties using a JSON path to reference subschemas. The &#x60;#base&#x60; properties are defined and versioned by Okta, while &#x60;#custom&#x60; properties are extensible. Custom property names for the profile object must be unique and can&#39;t conflict with a property name defined in the &#x60;#base&#x60; subschema. | [optional] 
**id** | **str** | URI of user schema | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the schema was last updated | [optional] [readonly] 
**name** | **str** | Name of the schema | [optional] [readonly] 
**properties** | [**UserSchemaProperties**](UserSchemaProperties.md) | User Object Properties | [optional] 
**title** | **str** | User-defined display name for the schema | [optional] 
**type** | **str** | Type of [root schema](https://tools.ietf.org/html/draft-zyp-json-schema-04#section-3.4) | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.user_schema import UserSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchema from a JSON string
user_schema_instance = UserSchema.from_json(json)
# print the JSON string representation of the object
print(UserSchema.to_json())

# convert the object into a dict
user_schema_dict = user_schema_instance.to_dict()
# create an instance of UserSchema from a dict
user_schema_from_dict = UserSchema.from_dict(user_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


