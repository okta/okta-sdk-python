# UserImportRequestExecute

User import inline hook request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_event_version** | **str** | The inline hook cloud version | [optional] 
**content_type** | **str** | The inline hook request header content | [optional] 
**event_id** | **str** | The individual inline hook request ID | [optional] 
**event_time** | **str** | The time the inline hook request was sent | [optional] 
**event_type_version** | **str** | The inline hook version | [optional] 
**data** | [**UserImportRequestData**](UserImportRequestData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The user import inline hook type is &#x60;com.okta.import.transform&#x60;. | [optional] 
**source** | **str** | The ID of the user import inline hook | [optional] 

## Example

```python
from okta.models.user_import_request_execute import UserImportRequestExecute

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequestExecute from a JSON string
user_import_request_execute_instance = UserImportRequestExecute.from_json(json)
# print the JSON string representation of the object
print(UserImportRequestExecute.to_json())

# convert the object into a dict
user_import_request_execute_dict = user_import_request_execute_instance.to_dict()
# create an instance of UserImportRequestExecute from a dict
user_import_request_execute_from_dict = UserImportRequestExecute.from_dict(user_import_request_execute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


