# UserImportRequestDataContextJob

The details of the running import job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID number of the import job | [optional] 
**type** | **str** | The type of import job | [optional] 

## Example

```python
from okta.models.user_import_request_data_context_job import UserImportRequestDataContextJob

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequestDataContextJob from a JSON string
user_import_request_data_context_job_instance = UserImportRequestDataContextJob.from_json(json)
# print the JSON string representation of the object
print(UserImportRequestDataContextJob.to_json())

# convert the object into a dict
user_import_request_data_context_job_dict = user_import_request_data_context_job_instance.to_dict()
# create an instance of UserImportRequestDataContextJob from a dict
user_import_request_data_context_job_from_dict = UserImportRequestDataContextJob.from_dict(user_import_request_data_context_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


