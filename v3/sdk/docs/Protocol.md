# Protocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithms** | [**ProtocolAlgorithms**](ProtocolAlgorithms.md) |  | [optional] 
**credentials** | [**IdentityProviderCredentials**](IdentityProviderCredentials.md) |  | [optional] 
**endpoints** | [**ProtocolEndpoints**](ProtocolEndpoints.md) |  | [optional] 
**issuer** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 
**relay_state** | [**ProtocolRelayState**](ProtocolRelayState.md) |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**settings** | [**ProtocolSettings**](ProtocolSettings.md) |  | [optional] 
**type** | [**ProtocolType**](ProtocolType.md) |  | [optional] 

## Example

```python
from openapi_client.models.protocol import Protocol

# TODO update the JSON string below
json = "{}"
# create an instance of Protocol from a JSON string
protocol_instance = Protocol.from_json(json)
# print the JSON string representation of the object
print(Protocol.to_json())

# convert the object into a dict
protocol_dict = protocol_instance.to_dict()
# create an instance of Protocol from a dict
protocol_form_dict = protocol.from_dict(protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


