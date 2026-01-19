# OktaSupportCaseImpersonation

Allows the Okta Support team to sign in to your org as an admin and troubleshoot issues

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OktaSupportAccessStatus**](OktaSupportAccessStatus.md) |  | [optional] 
**expiration** | **datetime** | Expiration date of Okta Support access | [optional] 

## Example

```python
from okta.models.okta_support_case_impersonation import OktaSupportCaseImpersonation

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSupportCaseImpersonation from a JSON string
okta_support_case_impersonation_instance = OktaSupportCaseImpersonation.from_json(json)
# print the JSON string representation of the object
print(OktaSupportCaseImpersonation.to_json())

# convert the object into a dict
okta_support_case_impersonation_dict = okta_support_case_impersonation_instance.to_dict()
# create an instance of OktaSupportCaseImpersonation from a dict
okta_support_case_impersonation_from_dict = OktaSupportCaseImpersonation.from_dict(okta_support_case_impersonation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


