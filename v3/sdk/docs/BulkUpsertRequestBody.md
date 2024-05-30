# BulkUpsertRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | [optional] 
**profiles** | [**List[IdentitySourceUserProfileForUpsert]**](IdentitySourceUserProfileForUpsert.md) |  | [optional] 

## Example

```python
from openapi_client.models.bulk_upsert_request_body import BulkUpsertRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpsertRequestBody from a JSON string
bulk_upsert_request_body_instance = BulkUpsertRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkUpsertRequestBody.to_json())

# convert the object into a dict
bulk_upsert_request_body_dict = bulk_upsert_request_body_instance.to_dict()
# create an instance of BulkUpsertRequestBody from a dict
bulk_upsert_request_body_form_dict = bulk_upsert_request_body.from_dict(bulk_upsert_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


