# SAMLPayLoadDataContextAllOfProtocol

Details of the assertion protocol being used

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of authentication protocol being used for the assertion | [optional] 
**issuer** | [**SAMLPayLoadDataContextAllOfProtocolIssuer**](SAMLPayLoadDataContextAllOfProtocolIssuer.md) |  | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_context_all_of_protocol import SAMLPayLoadDataContextAllOfProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataContextAllOfProtocol from a JSON string
saml_pay_load_data_context_all_of_protocol_instance = SAMLPayLoadDataContextAllOfProtocol.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataContextAllOfProtocol.to_json())

# convert the object into a dict
saml_pay_load_data_context_all_of_protocol_dict = saml_pay_load_data_context_all_of_protocol_instance.to_dict()
# create an instance of SAMLPayLoadDataContextAllOfProtocol from a dict
saml_pay_load_data_context_all_of_protocol_from_dict = SAMLPayLoadDataContextAllOfProtocol.from_dict(saml_pay_load_data_context_all_of_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


