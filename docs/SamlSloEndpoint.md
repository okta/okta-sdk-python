# SamlSloEndpoint

IdP's `SingleLogoutService` endpoint where Okta sends a `<LogoutRequest>` message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**ProtocolEndpointBinding**](ProtocolEndpointBinding.md) |  | [optional] 
**url** | **str** | URL of the binding-specific IdP endpoint where Okta sends a &#x60;&lt;LogoutRequest&gt;&#x60; | [optional] 

## Example

```python
from okta.models.saml_slo_endpoint import SamlSloEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of SamlSloEndpoint from a JSON string
saml_slo_endpoint_instance = SamlSloEndpoint.from_json(json)
# print the JSON string representation of the object
print(SamlSloEndpoint.to_json())

# convert the object into a dict
saml_slo_endpoint_dict = saml_slo_endpoint_instance.to_dict()
# create an instance of SamlSloEndpoint from a dict
saml_slo_endpoint_from_dict = SamlSloEndpoint.from_dict(saml_slo_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


