# UserSchemaAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **object** | If specified, assigns the value as the default value for the custom attribute. This is a nullable property. If you don&#39;t specify a value for this custom attribute during user creation or update, the &#x60;default&#x60; is used instead of setting the value to &#x60;null&#x60; or empty. | [optional] 
**description** | **str** | Description of the property | [optional] 
**enum** | [**List[GroupSchemaAttributeEnumInner]**](GroupSchemaAttributeEnumInner.md) | Enumerated value of the property.  The value of the property is limited to one of the values specified in the enum definition. The list of values for the enum must consist of unique elements. | [optional] 
**external_name** | **str** | Name of the property as it exists in an external application  **NOTE**: When you add a custom property, only Identity Provider app user schemas require &#x60;externalName&#x60; to be included in the request body. If an existing custom Identity Provider app user schema property has an empty &#x60;externalName&#x60;, requests aren&#39;t allowed to update other properties until the &#x60;externalName&#x60; is defined. | [optional] 
**external_namespace** | **str** | Namespace from the external application | [optional] 
**format** | [**UserSchemaAttributeFormat**](UserSchemaAttributeFormat.md) | Identifies the type of data represented by the string | [optional] 
**master** | [**UserSchemaAttributeMaster**](UserSchemaAttributeMaster.md) | Identifies where the property is mastered | [optional] 
**max_length** | **int** | Maximum character length of a string property | [optional] 
**min_length** | **int** | Minimum character length of a string property | [optional] 
**mutability** | [**UserSchemaAttributeMutabilityString**](UserSchemaAttributeMutabilityString.md) | Defines the mutability of the property | [optional] 
**one_of** | [**List[UserSchemaAttributeEnum]**](UserSchemaAttributeEnum.md) | Non-empty array of valid JSON schemas.  The &#x60;oneOf&#x60; key is only supported in conjunction with &#x60;enum&#x60; and provides a mechanism to return a display name for the &#x60;enum&#x60; value.&lt;br&gt; Each schema has the following format:  &#x60;&#x60;&#x60; {   \&quot;const\&quot;: \&quot;enumValue\&quot;,   \&quot;title\&quot;: \&quot;display name\&quot; } &#x60;&#x60;&#x60;  When &#x60;enum&#x60; is used in conjunction with &#x60;oneOf&#x60;, you must keep the set of enumerated values and their order.&lt;br&gt; For example:  &#x60;&#x60;&#x60; \&quot;enum\&quot;: [\&quot;S\&quot;,\&quot;M\&quot;,\&quot;L\&quot;,\&quot;XL\&quot;], \&quot;oneOf\&quot;: [     {\&quot;const\&quot;: \&quot;S\&quot;, \&quot;title\&quot;: \&quot;Small\&quot;},     {\&quot;const\&quot;: \&quot;M\&quot;, \&quot;title\&quot;: \&quot;Medium\&quot;},     {\&quot;const\&quot;: \&quot;L\&quot;, \&quot;title\&quot;: \&quot;Large\&quot;},     {\&quot;const\&quot;: \&quot;XL\&quot;, \&quot;title\&quot;: \&quot;Extra Large\&quot;}   ] &#x60;&#x60;&#x60; | [optional] 
**pattern** | **str** | For &#x60;string&#x60; property types, specifies the regular expression used to validate the property | [optional] 
**permissions** | [**List[UserSchemaAttributePermission]**](UserSchemaAttributePermission.md) | Access control permissions for the property | [optional] 
**required** | **bool** | Determines whether the property is required | [optional] 
**scope** | [**UserSchemaAttributeScope**](UserSchemaAttributeScope.md) |  | [optional] 
**title** | **str** | User-defined display name for the property | [optional] 
**type** | [**UserSchemaAttributeType**](UserSchemaAttributeType.md) | Type of property | [optional] 
**unique** | **bool** | Determines whether property values must be unique | [optional] 

## Example

```python
from okta.models.user_schema_attribute import UserSchemaAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaAttribute from a JSON string
user_schema_attribute_instance = UserSchemaAttribute.from_json(json)
# print the JSON string representation of the object
print(UserSchemaAttribute.to_json())

# convert the object into a dict
user_schema_attribute_dict = user_schema_attribute_instance.to_dict()
# create an instance of UserSchemaAttribute from a dict
user_schema_attribute_from_dict = UserSchemaAttribute.from_dict(user_schema_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


