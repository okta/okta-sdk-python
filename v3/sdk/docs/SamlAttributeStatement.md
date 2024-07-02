# SamlAttributeStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** |  | [optional] 
**filter_value** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.saml_attribute_statement import SamlAttributeStatement

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


