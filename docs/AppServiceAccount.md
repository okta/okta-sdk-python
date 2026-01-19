# AppServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_global_name** | **str** | The key name of the app in the Okta Integration Network (OIN) | [optional] [readonly] 
**container_instance_name** | **str** | The app instance label | [optional] [readonly] 
**container_orn** | **str** | The [ORN](/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the relevant resource.  Use the specific app ORN format (&#x60;orn:{partition}:idp:{yourOrgId}:apps:{appType}:{appId}&#x60;) to identify an Okta app instance in your org. | 
**created** | **datetime** | Timestamp when the app service account was created | [optional] [readonly] 
**description** | **str** | The description of the app service account | [optional] 
**id** | **str** | The UUID of the app service account | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the app service account was last updated | [optional] [readonly] 
**name** | **str** | The user-defined name for the app service account | 
**owner_group_ids** | **List[str]** | A list of IDs of the Okta groups who own the app service account | [optional] 
**owner_user_ids** | **List[str]** | A list of IDs of the Okta users who own the app service account | [optional] 
**password** | **str** | The app service account password. Required for apps that don&#39;t have provisioning enabled or don&#39;t support password synchronization. | [optional] 
**status** | [**ServiceAccountStatus**](ServiceAccountStatus.md) |  | [optional] 
**status_detail** | [**ServiceAccountStatusDetail**](ServiceAccountStatusDetail.md) |  | [optional] 
**username** | **str** | The username that serves as the direct link to your managed app account. Ensure that this value precisely matches the identifier of the target app account. | 

## Example

```python
from okta.models.app_service_account import AppServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAccount from a JSON string
app_service_account_instance = AppServiceAccount.from_json(json)
# print the JSON string representation of the object
print(AppServiceAccount.to_json())

# convert the object into a dict
app_service_account_dict = app_service_account_instance.to_dict()
# create an instance of AppServiceAccount from a dict
app_service_account_from_dict = AppServiceAccount.from_dict(app_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


