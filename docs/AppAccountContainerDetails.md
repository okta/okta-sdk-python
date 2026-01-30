# AppAccountContainerDetails

Container details for resource type APP_ACCOUNT

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | The application name | [optional] [readonly] 
**container_id** | **str** | The app ID associated with the privileged resource | 
**display_name** | **str** | Human-readable name of the container that owns the privileged resource | [optional] [readonly] 
**global_app_id** | **str** | The application global ID | [optional] [readonly] 
**password_push_supported** | **bool** | Indicates if the application supports password push | [optional] [readonly] 
**provisioning_enabled** | **bool** | Indicates if provisioning is enabled for this application | [optional] [readonly] 
**status** | [**AppInstanceContainerStatus**](AppInstanceContainerStatus.md) |  | [optional] 
**links** | [**AppAccountContainerLink**](AppAccountContainerLink.md) |  | [optional] 

## Example

```python
from okta.models.app_account_container_details import AppAccountContainerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccountContainerDetails from a JSON string
app_account_container_details_instance = AppAccountContainerDetails.from_json(json)
# print the JSON string representation of the object
print(AppAccountContainerDetails.to_json())

# convert the object into a dict
app_account_container_details_dict = app_account_container_details_instance.to_dict()
# create an instance of AppAccountContainerDetails from a dict
app_account_container_details_from_dict = AppAccountContainerDetails.from_dict(app_account_container_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


