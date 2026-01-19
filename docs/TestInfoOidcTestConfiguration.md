# TestInfoOidcTestConfiguration

OIDC test details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp** | **bool** | Read only.&lt;br&gt;Indicates if your integration supports IdP-initiated sign-in flows. If [&#x60;sso.oidc.initiateLoginUri&#x60;](/openapi/okta-management/management/tag/YourOinIntegrations/#tag/YourOinIntegrations/operation/createSubmission!path&#x3D;sso/oidc/initiateLoginUri&amp;t&#x3D;request) is specified, this property is set to &#x60;true&#x60;. If [&#x60;sso.oidc.initiateLoginUri&#x60;](/openapi/okta-management/management/tag/YourOinIntegrations/#tag/YourOinIntegrations/operation/createSubmission!path&#x3D;sso/oidc/initiateLoginUri&amp;t&#x3D;request) isn&#39;t set for the integration submission, this property is set to &#x60;false&#x60; | [optional] [readonly] 
**sp** | **bool** | Read only.&lt;br&gt;Indicates if your integration supports SP-initiated sign-in flows and is always set to &#x60;true&#x60; for OIDC SSO | [optional] [readonly] 
**jit** | **bool** | Indicates if your integration supports Just-In-Time (JIT) provisioning | [optional] 
**sp_initiate_url** | **str** | URL for SP-initiated sign-in flows (required if &#x60;sp &#x3D; true&#x60;) | 

## Example

```python
from okta.models.test_info_oidc_test_configuration import TestInfoOidcTestConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TestInfoOidcTestConfiguration from a JSON string
test_info_oidc_test_configuration_instance = TestInfoOidcTestConfiguration.from_json(json)
# print the JSON string representation of the object
print(TestInfoOidcTestConfiguration.to_json())

# convert the object into a dict
test_info_oidc_test_configuration_dict = test_info_oidc_test_configuration_instance.to_dict()
# create an instance of TestInfoOidcTestConfiguration from a dict
test_info_oidc_test_configuration_from_dict = TestInfoOidcTestConfiguration.from_dict(test_info_oidc_test_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


