# SAMLPayLoadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**SAMLPayLoadDataContext**](SAMLPayLoadDataContext.md) |  | [optional] 
**assertion** | [**SAMLPayLoadDataAssertion**](SAMLPayLoadDataAssertion.md) |  | [optional] 

## Example

```python
from okta.models.saml_pay_load_data import SAMLPayLoadData

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadData from a JSON string
saml_pay_load_data_instance = SAMLPayLoadData.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadData.to_json())

# convert the object into a dict
saml_pay_load_data_dict = saml_pay_load_data_instance.to_dict()
# create an instance of SAMLPayLoadData from a dict
saml_pay_load_data_from_dict = SAMLPayLoadData.from_dict(saml_pay_load_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


