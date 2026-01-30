# MtlsEndpoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso** | [**MtlsSsoEndpoint**](MtlsSsoEndpoint.md) |  | [optional] 

## Example

```python
from okta.models.mtls_endpoints import MtlsEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of MtlsEndpoints from a JSON string
mtls_endpoints_instance = MtlsEndpoints.from_json(json)
# print the JSON string representation of the object
print(MtlsEndpoints.to_json())

# convert the object into a dict
mtls_endpoints_dict = mtls_endpoints_instance.to_dict()
# create an instance of MtlsEndpoints from a dict
mtls_endpoints_from_dict = MtlsEndpoints.from_dict(mtls_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


