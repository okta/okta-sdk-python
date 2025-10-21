# HostedPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**HostedPageType**](HostedPageType.md) |  | 
**url** | **str** |  | [optional] 

## Example

```python
from okta.models.hosted_page import HostedPage

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPage from a JSON string
hosted_page_instance = HostedPage.from_json(json)
# print the JSON string representation of the object
print(HostedPage.to_json())

# convert the object into a dict
hosted_page_dict = hosted_page_instance.to_dict()
# create an instance of HostedPage from a dict
hosted_page_from_dict = HostedPage.from_dict(hosted_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


