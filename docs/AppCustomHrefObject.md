# AppCustomHrefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**AppCustomHrefObjectHints**](AppCustomHrefObjectHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**title** | **str** | Link name | [optional] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] 

## Example

```python
from okta.models.app_custom_href_object import AppCustomHrefObject

# TODO update the JSON string below
json = "{}"
# create an instance of AppCustomHrefObject from a JSON string
app_custom_href_object_instance = AppCustomHrefObject.from_json(json)
# print the JSON string representation of the object
print(AppCustomHrefObject.to_json())

# convert the object into a dict
app_custom_href_object_dict = app_custom_href_object_instance.to_dict()
# create an instance of AppCustomHrefObject from a dict
app_custom_href_object_from_dict = AppCustomHrefObject.from_dict(app_custom_href_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


