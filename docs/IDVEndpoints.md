# IDVEndpoints

Contains endpoints for the IDV vendor. When you create an `IDV_STANDARD` IdP, you must include the `par`, `authorization`, `token`, and `jwks` endpoints in the request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**IDVAuthorizationEndpoint**](IDVAuthorizationEndpoint.md) |  | 
**jwks** | [**OidcJwksEndpoint**](OidcJwksEndpoint.md) |  | 
**par** | [**IDVParEndpoint**](IDVParEndpoint.md) |  | 
**token** | [**IDVTokenEndpoint**](IDVTokenEndpoint.md) |  | 

## Example

```python
from okta.models.idv_endpoints import IDVEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of IDVEndpoints from a JSON string
idv_endpoints_instance = IDVEndpoints.from_json(json)
# print the JSON string representation of the object
print(IDVEndpoints.to_json())

# convert the object into a dict
idv_endpoints_dict = idv_endpoints_instance.to_dict()
# create an instance of IDVEndpoints from a dict
idv_endpoints_from_dict = IDVEndpoints.from_dict(idv_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


