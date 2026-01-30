# LogStreamSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | JSON schema version identifier | [optional] [readonly] 
**error_message** | **object** | A collection of error messages for individual properties in the schema. Okta implements a subset of [ajv-errors](https://github.com/ajv-validator/ajv-errors). | [optional] 
**id** | **str** | URI of log stream schema | [optional] [readonly] 
**one_of** | [**List[UserSchemaAttributeEnum]**](UserSchemaAttributeEnum.md) | Non-empty array of valid JSON schemas.  Okta only supports &#x60;oneOf&#x60; for specifying display names for an &#x60;enum&#x60;. Each schema has the following format:  &#x60;&#x60;&#x60; {   \&quot;const\&quot;: \&quot;enumValue\&quot;,   \&quot;title\&quot;: \&quot;display name\&quot; } &#x60;&#x60;&#x60; | [optional] 
**pattern** | **str** | For &#x60;string&#x60; log stream schema property type, specifies the regular expression used to validate the property | [optional] 
**properties** | **object** | log stream schema properties object | [optional] 
**required** | **List[str]** | Required properties for this log stream schema object | [optional] 
**title** | **str** | Name of the log streaming integration | [optional] 
**type** | **str** | Type of log stream schema property | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.log_stream_schema import LogStreamSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamSchema from a JSON string
log_stream_schema_instance = LogStreamSchema.from_json(json)
# print the JSON string representation of the object
print(LogStreamSchema.to_json())

# convert the object into a dict
log_stream_schema_dict = log_stream_schema_instance.to_dict()
# create an instance of LogStreamSchema from a dict
log_stream_schema_from_dict = LogStreamSchema.from_dict(log_stream_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


