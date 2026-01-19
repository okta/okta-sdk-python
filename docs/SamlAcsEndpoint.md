# SamlAcsEndpoint

Okta's `SPSSODescriptor` endpoint where the IdP sends a `<SAMLResponse>` message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**ProtocolEndpointBinding**](ProtocolEndpointBinding.md) |  | [optional] 
**type** | [**SamlEndpointType**](SamlEndpointType.md) |  | [optional] [default to SamlEndpointType.INSTANCE]

## Example

```python
from okta.models.saml_acs_endpoint import SamlAcsEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAcsEndpoint from a JSON string
saml_acs_endpoint_instance = SamlAcsEndpoint.from_json(json)
# print the JSON string representation of the object
print(SamlAcsEndpoint.to_json())

# convert the object into a dict
saml_acs_endpoint_dict = saml_acs_endpoint_instance.to_dict()
# create an instance of SamlAcsEndpoint from a dict
saml_acs_endpoint_from_dict = SamlAcsEndpoint.from_dict(saml_acs_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


