# TestInfoTestAccount

An account on a test instance of your app with admin privileges. A test admin account is required by Okta for integration testing. During OIN QA testing, an Okta analyst uses this admin account to configure your app for the various test case flows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The sign-in URL to a test instance of your app | 
**username** | **str** | The username for your app admin account | 
**password** | **str** | The password for your app admin account | 
**instructions** | **str** | Additional instructions to test the app integration, including instructions for obtaining test accounts | [optional] 

## Example

```python
from okta.models.test_info_test_account import TestInfoTestAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TestInfoTestAccount from a JSON string
test_info_test_account_instance = TestInfoTestAccount.from_json(json)
# print the JSON string representation of the object
print(TestInfoTestAccount.to_json())

# convert the object into a dict
test_info_test_account_dict = test_info_test_account_instance.to_dict()
# create an instance of TestInfoTestAccount from a dict
test_info_test_account_from_dict = TestInfoTestAccount.from_dict(test_info_test_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


