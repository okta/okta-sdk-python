# ProtocolAlgorithms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ProtocolAlgorithmType**](ProtocolAlgorithmType.md) |  | [optional] 
**response** | [**ProtocolAlgorithmType**](ProtocolAlgorithmType.md) |  | [optional] 

## Example

```python
from openapi_client.models.protocol_algorithms import ProtocolAlgorithms

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolAlgorithms from a JSON string
protocol_algorithms_instance = ProtocolAlgorithms.from_json(json)
# print the JSON string representation of the object
print(ProtocolAlgorithms.to_json())

# convert the object into a dict
protocol_algorithms_dict = protocol_algorithms_instance.to_dict()
# create an instance of ProtocolAlgorithms from a dict
protocol_algorithms_form_dict = protocol_algorithms.from_dict(protocol_algorithms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


