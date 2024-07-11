# ProtocolAlgorithmTypeSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  | [optional] 
**scope** | [**ProtocolAlgorithmTypeSignatureScope**](ProtocolAlgorithmTypeSignatureScope.md) |  | [optional] 

## Example

```python
from okta.models.protocol_algorithm_type_signature import ProtocolAlgorithmTypeSignature

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolAlgorithmTypeSignature from a JSON string
protocol_algorithm_type_signature_instance = ProtocolAlgorithmTypeSignature.from_json(json)
# print the JSON string representation of the object
print(ProtocolAlgorithmTypeSignature.to_json())

# convert the object into a dict
protocol_algorithm_type_signature_dict = protocol_algorithm_type_signature_instance.to_dict()
# create an instance of ProtocolAlgorithmTypeSignature from a dict
protocol_algorithm_type_signature_from_dict = ProtocolAlgorithmTypeSignature.from_dict(protocol_algorithm_type_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


