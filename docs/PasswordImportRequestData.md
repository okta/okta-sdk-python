# PasswordImportRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**PasswordImportRequestDataAction**](PasswordImportRequestDataAction.md) |  | [optional] 
**context** | [**PasswordImportRequestDataContext**](PasswordImportRequestDataContext.md) |  | [optional] 

## Example

```python
from okta.models.password_import_request_data import PasswordImportRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportRequestData from a JSON string
password_import_request_data_instance = PasswordImportRequestData.from_json(json)
# print the JSON string representation of the object
print(PasswordImportRequestData.to_json())

# convert the object into a dict
password_import_request_data_dict = password_import_request_data_instance.to_dict()
# create an instance of PasswordImportRequestData from a dict
password_import_request_data_from_dict = PasswordImportRequestData.from_dict(password_import_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


