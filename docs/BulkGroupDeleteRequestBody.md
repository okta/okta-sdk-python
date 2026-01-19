# BulkGroupDeleteRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ids** | **List[str]** | Array of external IDs of groups that need to be deleted in Okta | [optional] 

## Example

```python
from okta.models.bulk_group_delete_request_body import BulkGroupDeleteRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGroupDeleteRequestBody from a JSON string
bulk_group_delete_request_body_instance = BulkGroupDeleteRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkGroupDeleteRequestBody.to_json())

# convert the object into a dict
bulk_group_delete_request_body_dict = bulk_group_delete_request_body_instance.to_dict()
# create an instance of BulkGroupDeleteRequestBody from a dict
bulk_group_delete_request_body_from_dict = BulkGroupDeleteRequestBody.from_dict(bulk_group_delete_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


