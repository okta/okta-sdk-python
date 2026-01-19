# PasswordImportRequestDataContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**InlineHookRequestObject**](InlineHookRequestObject.md) |  | [optional] 
**credential** | [**PasswordImportRequestDataContextCredential**](PasswordImportRequestDataContextCredential.md) |  | [optional] 

## Example

```python
from okta.models.password_import_request_data_context import PasswordImportRequestDataContext

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportRequestDataContext from a JSON string
password_import_request_data_context_instance = PasswordImportRequestDataContext.from_json(json)
# print the JSON string representation of the object
print(PasswordImportRequestDataContext.to_json())

# convert the object into a dict
password_import_request_data_context_dict = password_import_request_data_context_instance.to_dict()
# create an instance of PasswordImportRequestDataContext from a dict
password_import_request_data_context_from_dict = PasswordImportRequestDataContext.from_dict(password_import_request_data_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


