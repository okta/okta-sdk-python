# HrefObjectClientLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.href_object_client_link import HrefObjectClientLink

# TODO update the JSON string below
json = "{}"
# create an instance of HrefObjectClientLink from a JSON string
href_object_client_link_instance = HrefObjectClientLink.from_json(json)
# print the JSON string representation of the object
print(HrefObjectClientLink.to_json())

# convert the object into a dict
href_object_client_link_dict = href_object_client_link_instance.to_dict()
# create an instance of HrefObjectClientLink from a dict
href_object_client_link_from_dict = HrefObjectClientLink.from_dict(href_object_client_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


