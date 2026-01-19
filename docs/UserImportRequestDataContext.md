# UserImportRequestDataContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicts** | **List[Dict[str, object]]** | An array of user profile attributes that are in conflict | [optional] 
**application** | [**UserImportRequestDataContextApplication**](UserImportRequestDataContextApplication.md) |  | [optional] 
**job** | [**UserImportRequestDataContextJob**](UserImportRequestDataContextJob.md) |  | [optional] 
**matches** | **List[Dict[str, object]]** | The list of Okta users currently matched to the app user based on import matching. There can be more than one match. | [optional] 
**policy** | **List[Dict[str, object]]** | The list of any policies that apply to the import matching | [optional] 

## Example

```python
from okta.models.user_import_request_data_context import UserImportRequestDataContext

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequestDataContext from a JSON string
user_import_request_data_context_instance = UserImportRequestDataContext.from_json(json)
# print the JSON string representation of the object
print(UserImportRequestDataContext.to_json())

# convert the object into a dict
user_import_request_data_context_dict = user_import_request_data_context_instance.to_dict()
# create an instance of UserImportRequestDataContext from a dict
user_import_request_data_context_from_dict = UserImportRequestDataContext.from_dict(user_import_request_data_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


