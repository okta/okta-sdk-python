# TokenPayLoadDataContextAllOfProtocolClient

The client making the token request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the client | [optional] 
**name** | **str** | The name of the client | [optional] 
**type** | **str** | The type of client | [optional] 

## Example

```python
from okta.models.token_pay_load_data_context_all_of_protocol_client import TokenPayLoadDataContextAllOfProtocolClient

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoadDataContextAllOfProtocolClient from a JSON string
token_pay_load_data_context_all_of_protocol_client_instance = TokenPayLoadDataContextAllOfProtocolClient.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoadDataContextAllOfProtocolClient.to_json())

# convert the object into a dict
token_pay_load_data_context_all_of_protocol_client_dict = token_pay_load_data_context_all_of_protocol_client_instance.to_dict()
# create an instance of TokenPayLoadDataContextAllOfProtocolClient from a dict
token_pay_load_data_context_all_of_protocol_client_from_dict = TokenPayLoadDataContextAllOfProtocolClient.from_dict(token_pay_load_data_context_all_of_protocol_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


