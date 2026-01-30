# TokenPayLoadDataContextAllOfProtocolOriginalGrant

Information about the original token request used to get the refresh token being used, when in a refresh token request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**TokenProtocolRequest**](TokenProtocolRequest.md) |  | [optional] 
**refresh_token** | [**RefreshToken**](RefreshToken.md) |  | [optional] 

## Example

```python
from okta.models.token_pay_load_data_context_all_of_protocol_original_grant import TokenPayLoadDataContextAllOfProtocolOriginalGrant

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoadDataContextAllOfProtocolOriginalGrant from a JSON string
token_pay_load_data_context_all_of_protocol_original_grant_instance = TokenPayLoadDataContextAllOfProtocolOriginalGrant.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoadDataContextAllOfProtocolOriginalGrant.to_json())

# convert the object into a dict
token_pay_load_data_context_all_of_protocol_original_grant_dict = token_pay_load_data_context_all_of_protocol_original_grant_instance.to_dict()
# create an instance of TokenPayLoadDataContextAllOfProtocolOriginalGrant from a dict
token_pay_load_data_context_all_of_protocol_original_grant_from_dict = TokenPayLoadDataContextAllOfProtocolOriginalGrant.from_dict(token_pay_load_data_context_all_of_protocol_original_grant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


