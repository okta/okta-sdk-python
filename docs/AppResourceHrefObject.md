# AppResourceHrefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Link URI | [optional] 
**title** | **str** | Link name | [optional] 

## Example

```python
from okta.models.app_resource_href_object import AppResourceHrefObject

# TODO update the JSON string below
json = "{}"
# create an instance of AppResourceHrefObject from a JSON string
app_resource_href_object_instance = AppResourceHrefObject.from_json(json)
# print the JSON string representation of the object
print(AppResourceHrefObject.to_json())

# convert the object into a dict
app_resource_href_object_dict = app_resource_href_object_instance.to_dict()
# create an instance of AppResourceHrefObject from a dict
app_resource_href_object_from_dict = AppResourceHrefObject.from_dict(app_resource_href_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


