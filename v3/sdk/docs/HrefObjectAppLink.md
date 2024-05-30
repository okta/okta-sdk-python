# HrefObjectAppLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefObjectHints**](HrefObjectHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] 
**templated** | **bool** | Indicates whether the Link Object&#39;s \&quot;href\&quot; property is a URI Template. | [optional] 

## Example

```python
from openapi_client.models.href_object_app_link import HrefObjectAppLink

# TODO update the JSON string below
json = "{}"
# create an instance of HrefObjectAppLink from a JSON string
href_object_app_link_instance = HrefObjectAppLink.from_json(json)
# print the JSON string representation of the object
print(HrefObjectAppLink.to_json())

# convert the object into a dict
href_object_app_link_dict = href_object_app_link_instance.to_dict()
# create an instance of HrefObjectAppLink from a dict
href_object_app_link_form_dict = href_object_app_link.from_dict(href_object_app_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


