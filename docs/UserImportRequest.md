# UserImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserImportRequestData**](UserImportRequestData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The user import inline hook type is &#x60;com.okta.import.transform&#x60;. | [optional] 
**source** | **str** | The ID of the user import inline hook | [optional] 

## Example

```python
from okta.models.user_import_request import UserImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequest from a JSON string
user_import_request_instance = UserImportRequest.from_json(json)
# print the JSON string representation of the object
print(UserImportRequest.to_json())

# convert the object into a dict
user_import_request_dict = user_import_request_instance.to_dict()
# create an instance of UserImportRequest from a dict
user_import_request_from_dict = UserImportRequest.from_dict(user_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


