# UserImportRequestDataContextApplication

Details of the app from which the user is being imported

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The app name | [optional] 
**id** | **str** | The app ID | [optional] 
**label** | **str** | The user-defined display name for the app | [optional] 
**status** | **str** | The status of the app | [optional] 

## Example

```python
from okta.models.user_import_request_data_context_application import UserImportRequestDataContextApplication

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequestDataContextApplication from a JSON string
user_import_request_data_context_application_instance = UserImportRequestDataContextApplication.from_json(json)
# print the JSON string representation of the object
print(UserImportRequestDataContextApplication.to_json())

# convert the object into a dict
user_import_request_data_context_application_dict = user_import_request_data_context_application_instance.to_dict()
# create an instance of UserImportRequestDataContextApplication from a dict
user_import_request_data_context_application_from_dict = UserImportRequestDataContextApplication.from_dict(user_import_request_data_context_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


