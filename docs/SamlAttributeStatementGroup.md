# SamlAttributeStatementGroup

`GROUP` attribute statements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** | The operation to filter groups based on &#x60;filterValue&#x60; | [optional] 
**filter_value** | **str** | Filter the groups based on a specific value. | [optional] 
**name** | **str** | The name of the group attribute in your app. The attribute name must be unique across all user and group attribute statements. | [optional] 
**namespace** | **str** | The name format of the group attribute. Supported values: | [optional] 
**type** | **str** | The type of attribute statements object | [optional] 

## Example

```python
from okta.models.saml_attribute_statement_group import SamlAttributeStatementGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAttributeStatementGroup from a JSON string
saml_attribute_statement_group_instance = SamlAttributeStatementGroup.from_json(json)
# print the JSON string representation of the object
print(SamlAttributeStatementGroup.to_json())

# convert the object into a dict
saml_attribute_statement_group_dict = saml_attribute_statement_group_instance.to_dict()
# create an instance of SamlAttributeStatementGroup from a dict
saml_attribute_statement_group_from_dict = SamlAttributeStatementGroup.from_dict(saml_attribute_statement_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


