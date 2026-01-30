# AppServiceAccountCredentials

Credentials for a SaaS app account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password associated with the service account | [optional] 
**username** | **str** | The username associated with the service account | 

## Example

```python
from okta.models.app_service_account_credentials import AppServiceAccountCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAccountCredentials from a JSON string
app_service_account_credentials_instance = AppServiceAccountCredentials.from_json(json)
# print the JSON string representation of the object
print(AppServiceAccountCredentials.to_json())

# convert the object into a dict
app_service_account_credentials_dict = app_service_account_credentials_instance.to_dict()
# create an instance of AppServiceAccountCredentials from a dict
app_service_account_credentials_from_dict = AppServiceAccountCredentials.from_dict(app_service_account_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


