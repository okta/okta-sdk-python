# UserImportRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**UserImportRequestDataAction**](UserImportRequestDataAction.md) |  | [optional] 
**app_user** | [**UserImportRequestDataAppUser**](UserImportRequestDataAppUser.md) |  | [optional] 
**context** | [**UserImportRequestDataContext**](UserImportRequestDataContext.md) |  | [optional] 
**user** | [**UserImportRequestDataUser**](UserImportRequestDataUser.md) |  | [optional] 

## Example

```python
from okta.models.user_import_request_data import UserImportRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequestData from a JSON string
user_import_request_data_instance = UserImportRequestData.from_json(json)
# print the JSON string representation of the object
print(UserImportRequestData.to_json())

# convert the object into a dict
user_import_request_data_dict = user_import_request_data_instance.to_dict()
# create an instance of UserImportRequestData from a dict
user_import_request_data_from_dict = UserImportRequestData.from_dict(user_import_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


