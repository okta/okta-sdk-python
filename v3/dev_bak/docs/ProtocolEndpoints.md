# ProtocolEndpoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 
**authorization** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 
**jwks** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 
**metadata** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 
**slo** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 
**sso** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 
**token** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 
**user_info** | [**ProtocolEndpoint**](ProtocolEndpoint.md) |  | [optional] 

## Example

```python
from openapi_client.models.protocol_endpoints import ProtocolEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolEndpoints from a JSON string
protocol_endpoints_instance = ProtocolEndpoints.from_json(json)
# print the JSON string representation of the object
print(ProtocolEndpoints.to_json())

# convert the object into a dict
protocol_endpoints_dict = protocol_endpoints_instance.to_dict()
# create an instance of ProtocolEndpoints from a dict
protocol_endpoints_from_dict = ProtocolEndpoints.from_dict(protocol_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


