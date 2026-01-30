# ServiceAccountDetailsAppAccountSub

Details for a SaaS app account, which will be managed as a service account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_global_name** | **str** | The name of the SaaS app in the Okta Integration Network catalog | [optional] [readonly] 
**app_instance_name** | **str** | The instance name of the SaaS app | [optional] [readonly] 
**credentials** | [**AppServiceAccountCredentials**](AppServiceAccountCredentials.md) |  | 
**okta_application_id** | **str** | The Okta app instance ID of the SaaS app | 

## Example

```python
from okta.models.service_account_details_app_account_sub import ServiceAccountDetailsAppAccountSub

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountDetailsAppAccountSub from a JSON string
service_account_details_app_account_sub_instance = ServiceAccountDetailsAppAccountSub.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountDetailsAppAccountSub.to_json())

# convert the object into a dict
service_account_details_app_account_sub_dict = service_account_details_app_account_sub_instance.to_dict()
# create an instance of ServiceAccountDetailsAppAccountSub from a dict
service_account_details_app_account_sub_from_dict = ServiceAccountDetailsAppAccountSub.from_dict(service_account_details_app_account_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


