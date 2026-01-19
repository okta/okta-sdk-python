# CreateGroupPushMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_config** | [**AppConfig**](AppConfig.md) |  | [optional] 
**source_group_id** | **str** | The ID of the source group for the group push mapping | 
**status** | [**GroupPushMappingStatusUpsert**](GroupPushMappingStatusUpsert.md) |  | [optional] [default to GroupPushMappingStatusUpsert.ACTIVE]
**target_group_id** | **str** | The ID of the existing target group for the group push mapping. This is used to link to an existing group. Required if &#x60;targetGroupName&#x60; is not provided. | [optional] 
**target_group_name** | **str** | The name of the target group for the group push mapping. This is used when creating a new downstream group. If the group already exists, it links to the existing group. Required if &#x60;targetGroupId&#x60; is not provided. | [optional] 

## Example

```python
from okta.models.create_group_push_mapping_request import CreateGroupPushMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupPushMappingRequest from a JSON string
create_group_push_mapping_request_instance = CreateGroupPushMappingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupPushMappingRequest.to_json())

# convert the object into a dict
create_group_push_mapping_request_dict = create_group_push_mapping_request_instance.to_dict()
# create an instance of CreateGroupPushMappingRequest from a dict
create_group_push_mapping_request_from_dict = CreateGroupPushMappingRequest.from_dict(create_group_push_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


