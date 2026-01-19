# AppServiceAccountForUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the app service account | [optional] 
**name** | **str** | The user-defined name for the app service account | [optional] 
**owner_group_ids** | **List[str]** | A list of IDs of the Okta groups who own the app service account | [optional] 
**owner_user_ids** | **List[str]** | A list of IDs of the Okta users who own the app service account | [optional] 

## Example

```python
from okta.models.app_service_account_for_update import AppServiceAccountForUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAccountForUpdate from a JSON string
app_service_account_for_update_instance = AppServiceAccountForUpdate.from_json(json)
# print the JSON string representation of the object
print(AppServiceAccountForUpdate.to_json())

# convert the object into a dict
app_service_account_for_update_dict = app_service_account_for_update_instance.to_dict()
# create an instance of AppServiceAccountForUpdate from a dict
app_service_account_for_update_from_dict = AppServiceAccountForUpdate.from_dict(app_service_account_for_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


