# BulkGroupMembershipsDeleteRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memberships** | [**List[IdentitySourceGroupMembershipsDeleteProfileInner]**](IdentitySourceGroupMembershipsDeleteProfileInner.md) | Array of group memberships that need to be deleted in Okta | [optional] 

## Example

```python
from okta.models.bulk_group_memberships_delete_request_body import BulkGroupMembershipsDeleteRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGroupMembershipsDeleteRequestBody from a JSON string
bulk_group_memberships_delete_request_body_instance = BulkGroupMembershipsDeleteRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkGroupMembershipsDeleteRequestBody.to_json())

# convert the object into a dict
bulk_group_memberships_delete_request_body_dict = bulk_group_memberships_delete_request_body_instance.to_dict()
# create an instance of BulkGroupMembershipsDeleteRequestBody from a dict
bulk_group_memberships_delete_request_body_from_dict = BulkGroupMembershipsDeleteRequestBody.from_dict(bulk_group_memberships_delete_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


