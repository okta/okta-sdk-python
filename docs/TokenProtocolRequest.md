# TokenProtocolRequest

Details of the token request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The ID of the client associated with the token | [optional] 
**grant_type** | [**GrantType**](GrantType.md) |  | [optional] 
**redirect_uri** | **str** | Specifies the callback location where the authorization was sent | [optional] 
**response_mode** | **str** | The authorization response mode | [optional] 
**response_type** | **str** | The authorization response type | [optional] 
**scope** | **str** | The scopes requested | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from okta.models.token_protocol_request import TokenProtocolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenProtocolRequest from a JSON string
token_protocol_request_instance = TokenProtocolRequest.from_json(json)
# print the JSON string representation of the object
print(TokenProtocolRequest.to_json())

# convert the object into a dict
token_protocol_request_dict = token_protocol_request_instance.to_dict()
# create an instance of TokenProtocolRequest from a dict
token_protocol_request_from_dict = TokenProtocolRequest.from_dict(token_protocol_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


