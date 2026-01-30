# UserSchemaPublic

All custom profile properties are defined in a profile subschema with the resolution scope `#custom`.  > **Notes:** > * When you refer to custom profile attributes that differ only by case, name collisions occur. This includes naming custom profile attributes the same as base profile attributes, for example, `firstName` and `FirstName`. > * Certain attributes are reserved and can't be used for custom user profiles. See [Review reserved attributes](https://help.okta.com/okta_help.htm?type=oie&id=reserved-attributes).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The subschema name | [optional] [readonly] 
**properties** | [**Dict[str, UserSchemaAttribute]**](UserSchemaAttribute.md) | The &#x60;#custom&#x60; object properties | [optional] 
**required** | **List[str]** | A collection indicating required property names | [optional] [readonly] 
**type** | **str** | The object type | [optional] [readonly] 

## Example

```python
from okta.models.user_schema_public import UserSchemaPublic

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaPublic from a JSON string
user_schema_public_instance = UserSchemaPublic.from_json(json)
# print the JSON string representation of the object
print(UserSchemaPublic.to_json())

# convert the object into a dict
user_schema_public_dict = user_schema_public_instance.to_dict()
# create an instance of UserSchemaPublic from a dict
user_schema_public_from_dict = UserSchemaPublic.from_dict(user_schema_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


