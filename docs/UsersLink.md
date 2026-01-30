# UsersLink


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
from okta.models.users_link import UsersLink

# TODO update the JSON string below
json = "{}"
# create an instance of UsersLink from a JSON string
users_link_instance = UsersLink.from_json(json)
# print the JSON string representation of the object
print(UsersLink.to_json())

# convert the object into a dict
users_link_dict = users_link_instance.to_dict()
# create an instance of UsersLink from a dict
users_link_from_dict = UsersLink.from_dict(users_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


