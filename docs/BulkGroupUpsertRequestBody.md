# BulkGroupUpsertRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**List[BulkGroupUpsertRequestBodyProfilesInner]**](BulkGroupUpsertRequestBodyProfilesInner.md) | Array of group profiles that needs to be inserted or updated in Okta | [optional] 

## Example

```python
from okta.models.bulk_group_upsert_request_body import BulkGroupUpsertRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGroupUpsertRequestBody from a JSON string
bulk_group_upsert_request_body_instance = BulkGroupUpsertRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkGroupUpsertRequestBody.to_json())

# convert the object into a dict
bulk_group_upsert_request_body_dict = bulk_group_upsert_request_body_instance.to_dict()
# create an instance of BulkGroupUpsertRequestBody from a dict
bulk_group_upsert_request_body_from_dict = BulkGroupUpsertRequestBody.from_dict(bulk_group_upsert_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


