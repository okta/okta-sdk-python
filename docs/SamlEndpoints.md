# SamlEndpoints

SAML 2.0 HTTP binding settings for IdP and SP (Okta)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs** | [**SamlAcsEndpoint**](SamlAcsEndpoint.md) |  | [optional] 
**slo** | [**SamlSloEndpoint**](SamlSloEndpoint.md) |  | [optional] 
**sso** | [**SamlSsoEndpoint**](SamlSsoEndpoint.md) |  | [optional] 

## Example

```python
from okta.models.saml_endpoints import SamlEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of SamlEndpoints from a JSON string
saml_endpoints_instance = SamlEndpoints.from_json(json)
# print the JSON string representation of the object
print(SamlEndpoints.to_json())

# convert the object into a dict
saml_endpoints_dict = saml_endpoints_instance.to_dict()
# create an instance of SamlEndpoints from a dict
saml_endpoints_from_dict = SamlEndpoints.from_dict(saml_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


