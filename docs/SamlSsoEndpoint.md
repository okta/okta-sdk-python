# SamlSsoEndpoint

IdP's `SingleSignOnService` endpoint where Okta sends an `<AuthnRequest>` message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**ProtocolEndpointBinding**](ProtocolEndpointBinding.md) |  | [optional] 
**destination** | **str** | URI reference that indicates the address to which the &#x60;&lt;AuthnRequest&gt;&#x60; message is sent. The &#x60;destination&#x60; property is required if request signatures are specified. See [SAML 2.0 Request Algorithm object](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/createIdentityProvider!path&#x3D;protocol/0/algorithms/request&amp;t&#x3D;request). | [optional] 
**url** | **str** | URL of the binding-specific endpoint to send an &#x60;&lt;AuthnRequest&gt;&#x60; message to the IdP. The value of &#x60;url&#x60; defaults to the same value as the &#x60;sso&#x60; endpoint if omitted during creation of a new IdP instance. The &#x60;url&#x60; should be the same value as the &#x60;Location&#x60; attribute for a published binding in the IdP&#39;s SAML Metadata &#x60;IDPSSODescriptor&#x60;. | [optional] 

## Example

```python
from okta.models.saml_sso_endpoint import SamlSsoEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of SamlSsoEndpoint from a JSON string
saml_sso_endpoint_instance = SamlSsoEndpoint.from_json(json)
# print the JSON string representation of the object
print(SamlSsoEndpoint.to_json())

# convert the object into a dict
saml_sso_endpoint_dict = saml_sso_endpoint_instance.to_dict()
# create an instance of SamlSsoEndpoint from a dict
saml_sso_endpoint_from_dict = SamlSsoEndpoint.from_dict(saml_sso_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


