# OktaSupportCases


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**support_cases** | [**List[OktaSupportCase]**](OktaSupportCase.md) |  | [optional] 

## Example

```python
from okta.models.okta_support_cases import OktaSupportCases

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSupportCases from a JSON string
okta_support_cases_instance = OktaSupportCases.from_json(json)
# print the JSON string representation of the object
print(OktaSupportCases.to_json())

# convert the object into a dict
okta_support_cases_dict = okta_support_cases_instance.to_dict()
# create an instance of OktaSupportCases from a dict
okta_support_cases_from_dict = OktaSupportCases.from_dict(okta_support_cases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


