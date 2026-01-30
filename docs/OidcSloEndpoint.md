# OidcSloEndpoint

OIDC IdP logout endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | IdP logout endpoint URL | [optional] 

## Example

```python
from okta.models.oidc_slo_endpoint import OidcSloEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of OidcSloEndpoint from a JSON string
oidc_slo_endpoint_instance = OidcSloEndpoint.from_json(json)
# print the JSON string representation of the object
print(OidcSloEndpoint.to_json())

# convert the object into a dict
oidc_slo_endpoint_dict = oidc_slo_endpoint_instance.to_dict()
# create an instance of OidcSloEndpoint from a dict
oidc_slo_endpoint_from_dict = OidcSloEndpoint.from_dict(oidc_slo_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


