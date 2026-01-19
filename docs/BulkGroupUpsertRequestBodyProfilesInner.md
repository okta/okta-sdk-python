# BulkGroupUpsertRequestBodyProfilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The external ID of the group that needs to be created or updated in Okta | [optional] 
**profile** | [**IdentitySourceGroupProfileForUpsert**](IdentitySourceGroupProfileForUpsert.md) |  | [optional] 

## Example

```python
from okta.models.bulk_group_upsert_request_body_profiles_inner import BulkGroupUpsertRequestBodyProfilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGroupUpsertRequestBodyProfilesInner from a JSON string
bulk_group_upsert_request_body_profiles_inner_instance = BulkGroupUpsertRequestBodyProfilesInner.from_json(json)
# print the JSON string representation of the object
print(BulkGroupUpsertRequestBodyProfilesInner.to_json())

# convert the object into a dict
bulk_group_upsert_request_body_profiles_inner_dict = bulk_group_upsert_request_body_profiles_inner_instance.to_dict()
# create an instance of BulkGroupUpsertRequestBodyProfilesInner from a dict
bulk_group_upsert_request_body_profiles_inner_from_dict = BulkGroupUpsertRequestBodyProfilesInner.from_dict(bulk_group_upsert_request_body_profiles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


