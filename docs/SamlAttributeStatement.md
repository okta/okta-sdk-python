# SamlAttributeStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of attribute statements object | [optional] 
**name** | **str** | The name of the group attribute in your app. The attribute name must be unique across all user and group attribute statements. | [optional] 
**namespace** | **str** | The name format of the group attribute. Supported values: | [optional] 
**values** | **List[str]** | The attribute values (supports [Okta Expression Language](https://developer.okta.com/docs/reference/okta-expression-language/)) | [optional] 
**filter_type** | **str** | The operation to filter groups based on &#x60;filterValue&#x60; | [optional] 
**filter_value** | **str** | Filter the groups based on a specific value. | [optional] 

## Example

```python
from okta.models.saml_attribute_statement import SamlAttributeStatement

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAttributeStatement from a JSON string
saml_attribute_statement_instance = SamlAttributeStatement.from_json(json)
# print the JSON string representation of the object
print(SamlAttributeStatement.to_json())

# convert the object into a dict
saml_attribute_statement_dict = saml_attribute_statement_instance.to_dict()
# create an instance of SamlAttributeStatement from a dict
saml_attribute_statement_from_dict = SamlAttributeStatement.from_dict(saml_attribute_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


