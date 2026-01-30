# UpdateGroupPushMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GroupPushMappingStatusUpsert**](GroupPushMappingStatusUpsert.md) |  | [default to GroupPushMappingStatusUpsert.ACTIVE]

## Example

```python
from okta.models.update_group_push_mapping_request import UpdateGroupPushMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupPushMappingRequest from a JSON string
update_group_push_mapping_request_instance = UpdateGroupPushMappingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupPushMappingRequest.to_json())

# convert the object into a dict
update_group_push_mapping_request_dict = update_group_push_mapping_request_instance.to_dict()
# create an instance of UpdateGroupPushMappingRequest from a dict
update_group_push_mapping_request_from_dict = UpdateGroupPushMappingRequest.from_dict(update_group_push_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


