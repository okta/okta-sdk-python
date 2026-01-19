# BulkGroupMembershipsUpsertRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memberships** | [**List[IdentitySourceGroupMembershipsUpsertProfileInner]**](IdentitySourceGroupMembershipsUpsertProfileInner.md) | Array of group memberships that need to be inserted or updated in Okta | [optional] 

## Example

```python
from okta.models.bulk_group_memberships_upsert_request_body import BulkGroupMembershipsUpsertRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGroupMembershipsUpsertRequestBody from a JSON string
bulk_group_memberships_upsert_request_body_instance = BulkGroupMembershipsUpsertRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkGroupMembershipsUpsertRequestBody.to_json())

# convert the object into a dict
bulk_group_memberships_upsert_request_body_dict = bulk_group_memberships_upsert_request_body_instance.to_dict()
# create an instance of BulkGroupMembershipsUpsertRequestBody from a dict
bulk_group_memberships_upsert_request_body_from_dict = BulkGroupMembershipsUpsertRequestBody.from_dict(bulk_group_memberships_upsert_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


