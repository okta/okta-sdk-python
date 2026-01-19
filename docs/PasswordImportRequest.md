# PasswordImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PasswordImportRequestData**](PasswordImportRequestData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The password import inline hook type is &#x60;com.okta.user.credential.password.import&#x60;. | [optional] 
**source** | **str** | The ID and URL of the password import inline hook | [optional] 

## Example

```python
from okta.models.password_import_request import PasswordImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportRequest from a JSON string
password_import_request_instance = PasswordImportRequest.from_json(json)
# print the JSON string representation of the object
print(PasswordImportRequest.to_json())

# convert the object into a dict
password_import_request_dict = password_import_request_instance.to_dict()
# create an instance of PasswordImportRequest from a dict
password_import_request_from_dict = PasswordImportRequest.from_dict(password_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


