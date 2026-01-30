# GroupPushMappingLinks

Discoverable resources related to the group push mapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**HrefObjectAppLink**](HrefObjectAppLink.md) |  | [optional] 
**source_group** | [**HrefObjectGroupLink**](HrefObjectGroupLink.md) |  | [optional] 
**target_group** | [**HrefObjectGroupLink**](HrefObjectGroupLink.md) |  | [optional] 

## Example

```python
from okta.models.group_push_mapping_links import GroupPushMappingLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPushMappingLinks from a JSON string
group_push_mapping_links_instance = GroupPushMappingLinks.from_json(json)
# print the JSON string representation of the object
print(GroupPushMappingLinks.to_json())

# convert the object into a dict
group_push_mapping_links_dict = group_push_mapping_links_instance.to_dict()
# create an instance of GroupPushMappingLinks from a dict
group_push_mapping_links_from_dict = GroupPushMappingLinks.from_dict(group_push_mapping_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


