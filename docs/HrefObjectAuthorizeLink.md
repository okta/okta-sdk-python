# HrefObjectAuthorizeLink

Link to authorize scopes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHintsGuidanceObject**](HrefHintsGuidanceObject.md) |  | [optional] 
**href** | **str** | Link URI | 

## Example

```python
from okta.models.href_object_authorize_link import HrefObjectAuthorizeLink

# TODO update the JSON string below
json = "{}"
# create an instance of HrefObjectAuthorizeLink from a JSON string
href_object_authorize_link_instance = HrefObjectAuthorizeLink.from_json(json)
# print the JSON string representation of the object
print(HrefObjectAuthorizeLink.to_json())

# convert the object into a dict
href_object_authorize_link_dict = href_object_authorize_link_instance.to_dict()
# create an instance of HrefObjectAuthorizeLink from a dict
href_object_authorize_link_from_dict = HrefObjectAuthorizeLink.from_dict(href_object_authorize_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


