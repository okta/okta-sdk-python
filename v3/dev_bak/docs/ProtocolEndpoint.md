# ProtocolEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**ProtocolEndpointBinding**](ProtocolEndpointBinding.md) |  | [optional] 
**destination** | **str** |  | [optional] 
**type** | [**ProtocolEndpointType**](ProtocolEndpointType.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.protocol_endpoint import ProtocolEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolEndpoint from a JSON string
protocol_endpoint_instance = ProtocolEndpoint.from_json(json)
# print the JSON string representation of the object
print(ProtocolEndpoint.to_json())

# convert the object into a dict
protocol_endpoint_dict = protocol_endpoint_instance.to_dict()
# create an instance of ProtocolEndpoint from a dict
protocol_endpoint_from_dict = ProtocolEndpoint.from_dict(protocol_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


