# UserImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[UserImportResponseCommandsInner]**](UserImportResponseCommandsInner.md) | The &#x60;commands&#x60; object is where you can provide commands to Okta. It is an array that allows you to send multiple commands. Each array element needs to consist of a type-value pair. | [optional] 
**error** | [**UserImportResponseError**](UserImportResponseError.md) |  | [optional] 

## Example

```python
from okta.models.user_import_response import UserImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportResponse from a JSON string
user_import_response_instance = UserImportResponse.from_json(json)
# print the JSON string representation of the object
print(UserImportResponse.to_json())

# convert the object into a dict
user_import_response_dict = user_import_response_instance.to_dict()
# create an instance of UserImportResponse from a dict
user_import_response_from_dict = UserImportResponse.from_dict(user_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


