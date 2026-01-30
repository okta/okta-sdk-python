# ProtocolMtls

Protocol settings for the [MTLS Protocol](https://tools.ietf.org/html/rfc5246#section-7.4.4)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**MtlsCredentials**](MtlsCredentials.md) |  | [optional] 
**endpoints** | [**MtlsEndpoints**](MtlsEndpoints.md) |  | [optional] 
**type** | **str** | Mutual TLS | [optional] 

## Example

```python
from okta.models.protocol_mtls import ProtocolMtls

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolMtls from a JSON string
protocol_mtls_instance = ProtocolMtls.from_json(json)
# print the JSON string representation of the object
print(ProtocolMtls.to_json())

# convert the object into a dict
protocol_mtls_dict = protocol_mtls_instance.to_dict()
# create an instance of ProtocolMtls from a dict
protocol_mtls_from_dict = ProtocolMtls.from_dict(protocol_mtls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


