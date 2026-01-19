# ServiceAccountForUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the service account | [optional] 
**name** | **str** | The human-readable name for the service account | [optional] 
**owner_group_ids** | **List[str]** | A list of IDs of the Okta groups who own the service account | [optional] 
**owner_user_ids** | **List[str]** | A list of IDs of the Okta users who own the service account | [optional] 

## Example

```python
from okta.models.service_account_for_update import ServiceAccountForUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountForUpdate from a JSON string
service_account_for_update_instance = ServiceAccountForUpdate.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountForUpdate.to_json())

# convert the object into a dict
service_account_for_update_dict = service_account_for_update_instance.to_dict()
# create an instance of ServiceAccountForUpdate from a dict
service_account_for_update_from_dict = ServiceAccountForUpdate.from_dict(service_account_for_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


