# WorkflowsValidationDetailProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**WorkflowsValidationErrorType**](WorkflowsValidationErrorType.md) |  | 

## Example

```python
from okta.models.workflows_validation_detail_provider import WorkflowsValidationDetailProvider

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowsValidationDetailProvider from a JSON string
workflows_validation_detail_provider_instance = WorkflowsValidationDetailProvider.from_json(json)
# print the JSON string representation of the object
print(WorkflowsValidationDetailProvider.to_json())

# convert the object into a dict
workflows_validation_detail_provider_dict = workflows_validation_detail_provider_instance.to_dict()
# create an instance of WorkflowsValidationDetailProvider from a dict
workflows_validation_detail_provider_from_dict = WorkflowsValidationDetailProvider.from_dict(workflows_validation_detail_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


