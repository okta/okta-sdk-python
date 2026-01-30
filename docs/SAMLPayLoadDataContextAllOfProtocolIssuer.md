# SAMLPayLoadDataContextAllOfProtocolIssuer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the issuer that provided the SAML assertion | [optional] 
**name** | **str** | The name of the issuer that provided the SAML assertion | [optional] 
**uri** | **str** | The base URI of the SAML endpoint that&#39;s used to assert the authorization | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_context_all_of_protocol_issuer import SAMLPayLoadDataContextAllOfProtocolIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataContextAllOfProtocolIssuer from a JSON string
saml_pay_load_data_context_all_of_protocol_issuer_instance = SAMLPayLoadDataContextAllOfProtocolIssuer.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataContextAllOfProtocolIssuer.to_json())

# convert the object into a dict
saml_pay_load_data_context_all_of_protocol_issuer_dict = saml_pay_load_data_context_all_of_protocol_issuer_instance.to_dict()
# create an instance of SAMLPayLoadDataContextAllOfProtocolIssuer from a dict
saml_pay_load_data_context_all_of_protocol_issuer_from_dict = SAMLPayLoadDataContextAllOfProtocolIssuer.from_dict(saml_pay_load_data_context_all_of_protocol_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


