# TestInfoSamlTestConfiguration

SAML test details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp** | **bool** | Indicates if your integration supports IdP-initiated sign-in | [optional] 
**sp** | **bool** | Indicates if your integration supports SP-initiated sign-in | [optional] 
**jit** | **bool** | Indicates if your integration supports Just-In-Time (JIT) provisioning | [optional] 
**sp_initiate_url** | **str** | URL for SP-initiated sign-in flows (required if &#x60;sp &#x3D; true&#x60;) | 
**sp_initiate_description** | **str** | Instructions on how to sign in to your app using the SP-initiated flow (required if &#x60;sp &#x3D; true&#x60;) | [optional] 

## Example

```python
from okta.models.test_info_saml_test_configuration import TestInfoSamlTestConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TestInfoSamlTestConfiguration from a JSON string
test_info_saml_test_configuration_instance = TestInfoSamlTestConfiguration.from_json(json)
# print the JSON string representation of the object
print(TestInfoSamlTestConfiguration.to_json())

# convert the object into a dict
test_info_saml_test_configuration_dict = test_info_saml_test_configuration_instance.to_dict()
# create an instance of TestInfoSamlTestConfiguration from a dict
test_info_saml_test_configuration_from_dict = TestInfoSamlTestConfiguration.from_dict(test_info_saml_test_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


