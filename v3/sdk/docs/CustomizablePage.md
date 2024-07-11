# CustomizablePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_content** | **str** |  | [optional] 

## Example

```python
from okta.models.customizable_page import CustomizablePage

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizablePage from a JSON string
customizable_page_instance = CustomizablePage.from_json(json)
# print the JSON string representation of the object
print(CustomizablePage.to_json())

# convert the object into a dict
customizable_page_dict = customizable_page_instance.to_dict()
# create an instance of CustomizablePage from a dict
customizable_page_from_dict = CustomizablePage.from_dict(customizable_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


