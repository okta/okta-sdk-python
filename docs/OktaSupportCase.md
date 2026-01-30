# OktaSupportCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_number** | **str** | Okta Support case number | [optional] [readonly] 
**impersonation** | [**OktaSupportCaseImpersonation**](OktaSupportCaseImpersonation.md) |  | [optional] 
**self_assigned** | [**OktaSupportCaseSelfAssigned**](OktaSupportCaseSelfAssigned.md) |  | [optional] 
**subject** | **str** | Subject of the support case | [optional] [readonly] 

## Example

```python
from okta.models.okta_support_case import OktaSupportCase

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSupportCase from a JSON string
okta_support_case_instance = OktaSupportCase.from_json(json)
# print the JSON string representation of the object
print(OktaSupportCase.to_json())

# convert the object into a dict
okta_support_case_dict = okta_support_case_instance.to_dict()
# create an instance of OktaSupportCase from a dict
okta_support_case_from_dict = OktaSupportCase.from_dict(okta_support_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


