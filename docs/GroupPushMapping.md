# GroupPushMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config** | [**AppConfig**](AppConfig.md) |  | [optional] 
**created** | **datetime** | Timestamp when the group push mapping was created | [optional] [readonly] 
**error_summary** | **str** | The error message summary if the latest push failed | [optional] [readonly] 
**id** | **str** | The ID of the group push mapping | [optional] [readonly] 
**last_push** | **datetime** | Timestamp when the group push mapping was pushed | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the group push mapping was last updated | [optional] [readonly] 
**source_group_id** | **str** | The ID of the source group for the group push mapping | [optional] [readonly] 
**status** | [**GroupPushMappingStatus**](GroupPushMappingStatus.md) |  | [optional] 
**target_group_id** | **str** | The ID of the target group for the group push mapping | [optional] [readonly] 
**links** | [**GroupPushMappingLinks**](GroupPushMappingLinks.md) |  | [optional] 

## Example

```python
from okta.models.group_push_mapping import GroupPushMapping

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPushMapping from a JSON string
group_push_mapping_instance = GroupPushMapping.from_json(json)
# print the JSON string representation of the object
print(GroupPushMapping.to_json())

# convert the object into a dict
group_push_mapping_dict = group_push_mapping_instance.to_dict()
# create an instance of GroupPushMapping from a dict
group_push_mapping_from_dict = GroupPushMapping.from_dict(group_push_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


