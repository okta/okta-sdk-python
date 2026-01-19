# TestInfoScimTestConfiguration

SCIM test details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_test_results** | **str** | The Runscope URL to your SCIM server specification test results. See [Test your SCIM API](https://developer.okta.com/docs/guides/build-provisioning-integration/test-scim-api/). | 
**crud_test_results** | **str** | The Runscope URL to your Okta SCIM CRUD test results. See [Test your Okta SCIM integration](https://developer.okta.com/docs/guides/scim-provisioning-integration-test/main/). | 
**entitlements_test_results** | **str** | The Runscope URL to your entitlements test results | [optional] 

## Example

```python
from okta.models.test_info_scim_test_configuration import TestInfoScimTestConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TestInfoScimTestConfiguration from a JSON string
test_info_scim_test_configuration_instance = TestInfoScimTestConfiguration.from_json(json)
# print the JSON string representation of the object
print(TestInfoScimTestConfiguration.to_json())

# convert the object into a dict
test_info_scim_test_configuration_dict = test_info_scim_test_configuration_instance.to_dict()
# create an instance of TestInfoScimTestConfiguration from a dict
test_info_scim_test_configuration_from_dict = TestInfoScimTestConfiguration.from_dict(test_info_scim_test_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


