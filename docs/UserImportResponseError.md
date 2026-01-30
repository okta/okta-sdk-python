# UserImportResponseError

An object to return an error. Returning an error causes Okta to record a failure event in the Okta System Log. The string supplied in the `errorSummary` property is recorded in the System Log event.  >**Note:** If a response to an import inline hook request is not received from your external service within three seconds, a timeout occurs. In this scenario, the Okta import process continues and the user is created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_summary** | **str** | A human-readable summary of the error | [optional] 

## Example

```python
from okta.models.user_import_response_error import UserImportResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportResponseError from a JSON string
user_import_response_error_instance = UserImportResponseError.from_json(json)
# print the JSON string representation of the object
print(UserImportResponseError.to_json())

# convert the object into a dict
user_import_response_error_dict = user_import_response_error_instance.to_dict()
# create an instance of UserImportResponseError from a dict
user_import_response_error_from_dict = UserImportResponseError.from_dict(user_import_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


