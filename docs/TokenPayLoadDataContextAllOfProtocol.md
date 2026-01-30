# TokenPayLoadDataContextAllOfProtocol

Details of the authentication protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of authentication protocol used | [optional] 
**request** | [**TokenProtocolRequest**](TokenProtocolRequest.md) |  | [optional] 
**original_grant** | [**TokenPayLoadDataContextAllOfProtocolOriginalGrant**](TokenPayLoadDataContextAllOfProtocolOriginalGrant.md) |  | [optional] 
**issuer** | [**TokenPayLoadDataContextAllOfProtocolIssuer**](TokenPayLoadDataContextAllOfProtocolIssuer.md) |  | [optional] 
**client** | [**TokenPayLoadDataContextAllOfProtocolClient**](TokenPayLoadDataContextAllOfProtocolClient.md) |  | [optional] 

## Example

```python
from okta.models.token_pay_load_data_context_all_of_protocol import TokenPayLoadDataContextAllOfProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoadDataContextAllOfProtocol from a JSON string
token_pay_load_data_context_all_of_protocol_instance = TokenPayLoadDataContextAllOfProtocol.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoadDataContextAllOfProtocol.to_json())

# convert the object into a dict
token_pay_load_data_context_all_of_protocol_dict = token_pay_load_data_context_all_of_protocol_instance.to_dict()
# create an instance of TokenPayLoadDataContextAllOfProtocol from a dict
token_pay_load_data_context_all_of_protocol_from_dict = TokenPayLoadDataContextAllOfProtocol.from_dict(token_pay_load_data_context_all_of_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


