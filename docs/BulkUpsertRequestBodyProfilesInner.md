# BulkUpsertRequestBodyProfilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The external ID of the entity that needs to be created or updated in Okta | [optional] 
**profile** | [**IdentitySourceUserProfileForUpsert**](IdentitySourceUserProfileForUpsert.md) |  | [optional] 

## Example

```python
from okta.models.bulk_upsert_request_body_profiles_inner import BulkUpsertRequestBodyProfilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpsertRequestBodyProfilesInner from a JSON string
bulk_upsert_request_body_profiles_inner_instance = BulkUpsertRequestBodyProfilesInner.from_json(json)
# print the JSON string representation of the object
print(BulkUpsertRequestBodyProfilesInner.to_json())

# convert the object into a dict
bulk_upsert_request_body_profiles_inner_dict = bulk_upsert_request_body_profiles_inner_instance.to_dict()
# create an instance of BulkUpsertRequestBodyProfilesInner from a dict
bulk_upsert_request_body_profiles_inner_from_dict = BulkUpsertRequestBodyProfilesInner.from_dict(bulk_upsert_request_body_profiles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


