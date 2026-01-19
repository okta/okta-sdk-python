# SamlAttributeStatementExpression

Generic `EXPRESSION` attribute statements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the attribute in your app. The attribute name must be unique across all user and group attribute statements. | [optional] 
**namespace** | **str** | The name format of the attribute. Supported values: | [optional] 
**type** | **str** | The type of attribute statements object | [optional] 
**values** | **List[str]** | The attribute values (supports [Okta Expression Language](https://developer.okta.com/docs/reference/okta-expression-language/)) | [optional] 

## Example

```python
from okta.models.saml_attribute_statement_expression import SamlAttributeStatementExpression

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAttributeStatementExpression from a JSON string
saml_attribute_statement_expression_instance = SamlAttributeStatementExpression.from_json(json)
# print the JSON string representation of the object
print(SamlAttributeStatementExpression.to_json())

# convert the object into a dict
saml_attribute_statement_expression_dict = saml_attribute_statement_expression_instance.to_dict()
# create an instance of SamlAttributeStatementExpression from a dict
saml_attribute_statement_expression_from_dict = SamlAttributeStatementExpression.from_dict(saml_attribute_statement_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


