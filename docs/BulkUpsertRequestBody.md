# BulkUpsertRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of data to upsert into the session. Currently, only &#x60;USERS&#x60; is supported. | [optional] 
**profiles** | [**List[BulkUpsertRequestBodyProfilesInner]**](BulkUpsertRequestBodyProfilesInner.md) | Array of user profiles to be uploaded | [optional] 

## Example

```python
from okta.models.bulk_upsert_request_body import BulkUpsertRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpsertRequestBody from a JSON string
bulk_upsert_request_body_instance = BulkUpsertRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkUpsertRequestBody.to_json())

# convert the object into a dict
bulk_upsert_request_body_dict = bulk_upsert_request_body_instance.to_dict()
# create an instance of BulkUpsertRequestBody from a dict
bulk_upsert_request_body_from_dict = BulkUpsertRequestBody.from_dict(bulk_upsert_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


