# HrefObjectLogoLink


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
from okta.models.href_object_logo_link import HrefObjectLogoLink

# TODO update the JSON string below
json = "{}"
# create an instance of HrefObjectLogoLink from a JSON string
href_object_logo_link_instance = HrefObjectLogoLink.from_json(json)
# print the JSON string representation of the object
print(HrefObjectLogoLink.to_json())

# convert the object into a dict
href_object_logo_link_dict = href_object_logo_link_instance.to_dict()
# create an instance of HrefObjectLogoLink from a dict
href_object_logo_link_from_dict = HrefObjectLogoLink.from_dict(href_object_logo_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


