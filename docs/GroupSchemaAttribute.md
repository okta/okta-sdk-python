# GroupSchemaAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the property | [optional] 
**enum** | [**List[GroupSchemaAttributeEnumInner]**](GroupSchemaAttributeEnumInner.md) | Enumerated value of the property.  The value of the property is limited to one of the values specified in the enum definition. The list of values for the enum must consist of unique elements. | [optional] 
**external_name** | **str** | Name of the property as it exists in an external application | [optional] 
**external_namespace** | **str** | Namespace from the external application | [optional] 
**format** | [**UserSchemaAttributeFormat**](UserSchemaAttributeFormat.md) | Identifies the type of data represented by the string | [optional] 
**items** | [**UserSchemaAttributeItems**](UserSchemaAttributeItems.md) |  | [optional] 
**master** | [**UserSchemaAttributeMaster**](UserSchemaAttributeMaster.md) | Identifies where the property is mastered | [optional] 
**max_length** | **int** | Maximum character length of a string property | [optional] 
**min_length** | **int** | Minimum character length of a string property | [optional] 
**mutability** | [**UserSchemaAttributeMutabilityString**](UserSchemaAttributeMutabilityString.md) | Defines the mutability of the property | [optional] 
**one_of** | [**List[UserSchemaAttributeEnum]**](UserSchemaAttributeEnum.md) | Non-empty array of valid JSON schemas.  The &#x60;oneOf&#x60; key is only supported in conjunction with &#x60;enum&#x60; and provides a mechanism to return a display name for the &#x60;enum&#x60; value.&lt;br&gt; Each schema has the following format:  &#x60;&#x60;&#x60; {   \&quot;const\&quot;: \&quot;enumValue\&quot;,   \&quot;title\&quot;: \&quot;display name\&quot; } &#x60;&#x60;&#x60;  When &#x60;enum&#x60; is used in conjunction with &#x60;oneOf&#x60;, you must keep the set of enumerated values and their order.&lt;br&gt; For example:  &#x60;&#x60;&#x60; \&quot;enum\&quot;: [\&quot;S\&quot;,\&quot;M\&quot;,\&quot;L\&quot;,\&quot;XL\&quot;], \&quot;oneOf\&quot;: [     {\&quot;const\&quot;: \&quot;S\&quot;, \&quot;title\&quot;: \&quot;Small\&quot;},     {\&quot;const\&quot;: \&quot;M\&quot;, \&quot;title\&quot;: \&quot;Medium\&quot;},     {\&quot;const\&quot;: \&quot;L\&quot;, \&quot;title\&quot;: \&quot;Large\&quot;},     {\&quot;const\&quot;: \&quot;XL\&quot;, \&quot;title\&quot;: \&quot;Extra Large\&quot;}   ] &#x60;&#x60;&#x60; | [optional] 
**permissions** | [**List[UserSchemaAttributePermission]**](UserSchemaAttributePermission.md) | Access control permissions for the property | [optional] 
**required** | **bool** | Determines whether the property is required | [optional] 
**scope** | [**UserSchemaAttributeScope**](UserSchemaAttributeScope.md) | Determines whether a group attribute can be set at the individual or group level | [optional] 
**title** | **str** | User-defined display name for the property | [optional] 
**type** | [**UserSchemaAttributeType**](UserSchemaAttributeType.md) | Type of property | [optional] 
**unique** | **bool** | Determines whether property values must be unique | [optional] 

## Example

```python
from okta.models.group_schema_attribute import GroupSchemaAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchemaAttribute from a JSON string
group_schema_attribute_instance = GroupSchemaAttribute.from_json(json)
# print the JSON string representation of the object
print(GroupSchemaAttribute.to_json())

# convert the object into a dict
group_schema_attribute_dict = group_schema_attribute_instance.to_dict()
# create an instance of GroupSchemaAttribute from a dict
group_schema_attribute_from_dict = GroupSchemaAttribute.from_dict(group_schema_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


