# TestInfo

Integration Testing Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**escalation_support_contact** | **str** | An email for Okta to contact your company about your integration. This email isn&#39;t shared with customers. | 
**oidc_test_configuration** | [**TestInfoOidcTestConfiguration**](TestInfoOidcTestConfiguration.md) |  | [optional] 
**saml_test_configuration** | [**TestInfoSamlTestConfiguration**](TestInfoSamlTestConfiguration.md) |  | [optional] 
**scim_test_configuration** | [**TestInfoScimTestConfiguration**](TestInfoScimTestConfiguration.md) |  | [optional] 
**test_account** | [**TestInfoTestAccount**](TestInfoTestAccount.md) |  | [optional] 

## Example

```python
from okta.models.test_info import TestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TestInfo from a JSON string
test_info_instance = TestInfo.from_json(json)
# print the JSON string representation of the object
print(TestInfo.to_json())

# convert the object into a dict
test_info_dict = test_info_instance.to_dict()
# create an instance of TestInfo from a dict
test_info_from_dict = TestInfo.from_dict(test_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


