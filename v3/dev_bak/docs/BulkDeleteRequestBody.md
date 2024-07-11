# BulkDeleteRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | [optional] 
**profiles** | [**List[IdentitySourceUserProfileForDelete]**](IdentitySourceUserProfileForDelete.md) |  | [optional] 

## Example

```python
from openapi_client.models.bulk_delete_request_body import BulkDeleteRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteRequestBody from a JSON string
bulk_delete_request_body_instance = BulkDeleteRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteRequestBody.to_json())

# convert the object into a dict
bulk_delete_request_body_dict = bulk_delete_request_body_instance.to_dict()
# create an instance of BulkDeleteRequestBody from a dict
bulk_delete_request_body_from_dict = BulkDeleteRequestBody.from_dict(bulk_delete_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


