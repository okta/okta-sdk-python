# GroupsLink


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
from okta.models.groups_link import GroupsLink

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsLink from a JSON string
groups_link_instance = GroupsLink.from_json(json)
# print the JSON string representation of the object
print(GroupsLink.to_json())

# convert the object into a dict
groups_link_dict = groups_link_instance.to_dict()
# create an instance of GroupsLink from a dict
groups_link_from_dict = GroupsLink.from_dict(groups_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


