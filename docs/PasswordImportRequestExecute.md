# PasswordImportRequestExecute

Password import inline hook request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_event_version** | **str** | The inline hook cloud version | [optional] 
**content_type** | **str** | The inline hook request header content | [optional] 
**event_id** | **str** | The individual inline hook request ID | [optional] 
**event_time** | **str** | The time the inline hook request was sent | [optional] 
**event_type_version** | **str** | The inline hook version | [optional] 
**data** | [**PasswordImportRequestData**](PasswordImportRequestData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The password import inline hook type is &#x60;com.okta.user.credential.password.import&#x60;. | [optional] 
**source** | **str** | The ID and URL of the password import inline hook | [optional] 

## Example

```python
from okta.models.password_import_request_execute import PasswordImportRequestExecute

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportRequestExecute from a JSON string
password_import_request_execute_instance = PasswordImportRequestExecute.from_json(json)
# print the JSON string representation of the object
print(PasswordImportRequestExecute.to_json())

# convert the object into a dict
password_import_request_execute_dict = password_import_request_execute_instance.to_dict()
# create an instance of PasswordImportRequestExecute from a dict
password_import_request_execute_from_dict = PasswordImportRequestExecute.from_dict(password_import_request_execute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


